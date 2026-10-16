# Development and editorial guidance

This is Maverik Punungwe's existing Jekyll / Minimal Mistakes blog. Preserve historical article bodies, dates, attribution and URLs. Do not change categories on published posts without a URL migration plan: categories form part of the permalink.

Read README.md and editorial/audit-and-plan.md before making changes. Keep technical changes and article edits reviewable separately. Retain upstream theme attribution and licensing.

## Authorization

Local edits and validation are authorized. Never commit, push, deploy, or publish content without Maverik's explicit approval after a meaningful change summary and validation results. Outline approval and draft approval are not publication approval. Never send or publish LinkedIn posts.

## Content

Create new articles through scripts/new_draft.py. Keep raw drafts in _drafts with published: false. New _posts entries also default to unpublished; historical posts explicitly use published: true. Do not enable unpublished, show_drafts or future in production. editorial/ and scripts/ must remain excluded from production. Preview output must never be uploaded.

Follow Idea -> Research and outline -> Raw draft -> Author review -> Final editorial review -> Explicit publication approval. Store source links, research assumptions and author questions with the outline. Each approved article gets a separately reviewed LinkedIn draft under editorial/linkedin/.

AI assists the author's voice. Do not invent achievements, titles, metrics, anecdotes, opinions, sources, project details or confidential professional information. Use [AUTHOR INPUT REQUIRED: ...], [VERIFY: ...] and [AUTHOR OPINION REQUIRED: ...]. Separate facts, assumptions, opinions and predictions. Prefer direct language and worked examples; avoid motivational filler, jargon, formulaic conclusions and unnecessary em dashes. Author editing decisions prevail.

## Validation

Run python scripts/check_content.py for source checks. Once Ruby and Bundler are available, run bundle install, bundle exec jekyll build --strict_front_matter and bundle exec jekyll doctor. Check generated internal links, metadata, sitemap, feed and draft isolation before publication. Perform responsive and keyboard checks in a browser. Report only checks actually executed and disclose missing tooling. Do not use the upstream rake preview task for the personal site; it builds theme fixtures.

The canonical origin is confirmed as https://mickpunungwe3000.github.io. Keep Gemfile.lock tracked for reproducible Windows/Linux resolution. The tag archive includes posts and project tags. Generated-site validation: python scripts/check_site.py _site --origin https://mickpunungwe3000.github.io. Run bundle exec ruby scripts/verify_draft_isolation.rb for the isolated production/preview regression check. The validate.yml Actions workflow has no deployment step; do not add one without publication/deployment approval. On Windows use scripts/preview.ps1 with -Drafts and an optional -RubyBin path.
