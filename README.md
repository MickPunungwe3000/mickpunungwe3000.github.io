# Maverik Punungwe — engineering and product writing

A personal platform for software architecture, product building, industrial technology, business strategy and engineering growth. This is an existing GitHub Pages blog, built on the locally vendored Minimal Mistakes theme (MIT). Historical writing is preserved.

## Architecture

Jekyll renders Markdown and Liquid using _layouts/, _includes/, _sass/ and assets/. _posts/ contains historical published articles; _projects/ is an output collection. Root pages provide Home, About, Blog, Projects and Contact. _data/navigation.yml controls navigation. _config.yml contains site metadata, permalink rules, defaults and plugin settings. docs/ and test/ are upstream theme documentation and fixtures, excluded from the personal site.

Plugins: jekyll-paginate, jekyll-sitemap, jekyll-gist, jekyll-feed and jekyll-include-cache. Gemfile loads the local gemspec. package.json describes the upstream theme's JavaScript tooling; it has no application build or test command.

## Setup and preview

Install Ruby 3.3 with its development tools and Bundler (Ruby+Devkit on Windows), then run from the repository root. Gemfile.lock pins dependencies for Windows and Linux; Windows timezone gems are declared in Gemfile:

```powershell
bundle install
bundle exec jekyll serve --host 127.0.0.1
```

Open http://127.0.0.1:4000. Restart after configuration changes. For a private local preview including unpublished work:

```powershell
bundle exec jekyll serve --config _config.yml,_config.preview.yml --host 127.0.0.1
```

On Windows, the helper keeps PATH changes scoped to the preview process:

```powershell
./scripts/preview.ps1 -Drafts
# If Ruby is outside PATH:
./scripts/preview.ps1 -Drafts -RubyBin "C:/path/to/ruby/bin"
```

The task's temporary tool setup can be used with `-RubyBin "$env:LOCALAPPDATA/Temp/maverik-blog-ruby/devtools/bin"`. Prefer a normal Ruby+Devkit installation for long-term use; temporary folders can be cleaned by Windows.

Preview output goes to _site-preview/ and must never be deployed. This mode can expose drafts to anyone able to access the preview server. Keep it bound to localhost. The upstream `rake preview` builds test fixtures, not this blog.

## Writing and review

```powershell
python scripts/new_draft.py product-versus-software "Building Software Is Not the Same as Building a Product"
python scripts/check_content.py
```

New articles live in _drafts/ with published: false. All new _posts entries also default to unpublished. Existing posts explicitly opt in to preserve their publication status. Never use production flags that include drafts or unpublished posts.

Follow the six stages in AGENTS.md. See editorial/backlog.md for proposed topics and editorial/audit-and-plan.md for the site assessment. Keep sources and outlines in editorial/. Use author-input annotations rather than inventing personal evidence. LinkedIn drafts live in editorial/linkedin/ and require separate review.

Only after explicit publication approval: move the reviewed draft into _posts/YYYY-MM-DD-slug.md, set its approved date and published: true, confirm its URL and metadata, run validation, then request commit/push approval with the exact diff and results. Changing existing categories changes URLs under /:categories/:title/; preserve them or arrange redirects. Revert approved changes through reviewed Git commits; never rewrite shared history.

## Validation

```powershell
python scripts/check_content.py
bundle exec jekyll build --strict_front_matter
bundle exec jekyll doctor
python scripts/check_site.py _site --origin https://mickpunungwe3000.github.io
bundle exec ruby scripts/verify_draft_isolation.rb
```

The Python checker has no third-party dependencies. It checks publication flags, basic frontmatter boundaries, Markdown fence balance and referenced local assets; it is not a YAML parser or full Markdown linter. Known historical formatting and asset problems are warnings pending author review. Run a production build and inspect generated pages, feed.xml, sitemap.xml and any search index for draft titles, slugs and editorial annotations. Verify internal links and canonical URLs in the built site. Test mobile, desktop, keyboard navigation and contrast in a browser. The generated-site checker verifies local references, metadata, feed/sitemap XML and private-source exclusions. The isolation test builds a temporary source copy containing four private-content cases and confirms production exclusion plus preview visibility. test/ contains upstream theme fixtures. The separate validate.yml Actions workflow runs checks for pull requests or manual runs; it has no deployment step and has not been executed on GitHub yet.

## Current local design changes

The approved direction is implemented locally: a dedicated homepage layout, broader About copy, Writing/Topics navigation, category/tag archives and revised reading styles. See editorial/implementation-review.md for the exact scope and executed checks. Article URLs remain unchanged. Local production builds, Jekyll diagnostics, generated-site checks, draft-isolation tests and representative desktop/mobile browser checks passed. The canonical GitHub Pages origin is confirmed; actual remote Pages deployment settings remain unverified. See the review notes for scope and residual warnings.

## SEO and deployment

SEO is rendered by _includes/seo.html; sitemap and feed come from plugins. The confirmed canonical site URL is https://mickpunungwe3000.github.io and the repository is MickPunungwe3000/mickpunungwe3000.github.io. Supply per-article descriptions and a real social image where appropriate.

The Git remote points to MickPunungwe3000/mickpunungwe3000.github.io. The existing build workflow only runs for mmistakes/minimal-mistakes and indexes upstream docs; it is not a deployment pipeline for this blog. Confirm the repository's actual Pages source/settings before changing deployment. Local repository files cannot establish the live Pages configuration. The added validate.yml workflow performs validation only. No deployment has been added or triggered. Never upload _site-preview/ or include _config.preview.yml in production builds.

Do not commit, push or deploy without explicit approval. Technical updates and publication content should be reviewed separately.
