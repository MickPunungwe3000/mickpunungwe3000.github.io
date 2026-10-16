# Run with: bundle exec ruby scripts/verify_draft_isolation.rb
# Uses an isolated source copy; never adds test posts to the working blog.
require "jekyll"
require "tmpdir"
require "fileutils"

root = File.expand_path("..", __dir__)
Dir.mktmpdir("maverik-blog-isolation-") do |workspace|
  source = File.join(workspace, "source")
  FileUtils.mkdir_p(source)
  names = %w[_config.yml _data _includes _layouts _sass _pages _posts _projects assets]
  names += Dir.children(root).select { |name| name.end_with?(".md") }
  names.each { |name| FileUtils.cp_r(File.join(root, name), source) }
  FileUtils.mkdir_p(File.join(source, "_drafts"))
  FileUtils.mkdir_p(File.join(source, "editorial"))
  fixtures = {
    "_drafts/isolation-draft.md" => ["ISOLATION_DRAFT_TOKEN", "published: false"],
    "_posts/2000-01-01-isolation-default.md" => ["ISOLATION_DEFAULT_TOKEN", ""],
    "_posts/2000-01-02-isolation-unpublished.md" => ["ISOLATION_UNPUBLISHED_TOKEN", "published: false"],
    "_posts/2099-01-01-isolation-future.md" => ["ISOLATION_FUTURE_TOKEN", "published: true"]
  }
  fixtures.each do |name, (token, status)|
    File.write(File.join(source, name), "---\ntitle: #{token}\n#{status}\nlayout: single\n---\n\n#{token}\n")
  end
  private_token = "ISOLATION_EDITORIAL_TOKEN"
  File.write(File.join(source, "editorial", "private.md"), private_token)
  tokens = fixtures.values.map(&:first)
  %w[production preview].each do |mode|
    destination = File.join(workspace, mode)
    options = {"source" => source, "destination" => destination, "quiet" => true, "strict_front_matter" => true}
    if mode == "preview"
      options.merge!({"show_drafts" => true, "unpublished" => true, "future" => true})
    end
    Jekyll::Site.new(Jekyll.configuration(options)).process
    output = Dir.glob(File.join(destination, "**", "*" )).select { |path| File.file?(path) && %w[.html .xml .json .js .md .txt].include?(File.extname(path)) }.map { |path| File.read(path, encoding: "UTF-8", invalid: :replace, undef: :replace) }.join("\n")
    raise "Private editorial notes leaked in #{mode}" if output.include?(private_token)
    tokens.each do |token|
      visible = output.include?(token)
      raise "#{token}: unexpected visibility in #{mode}" unless visible == (mode == "preview")
    end
    puts "PASS #{mode}: all four draft/default/unpublished/future visibility cases; editorial notes excluded."
  end
end
