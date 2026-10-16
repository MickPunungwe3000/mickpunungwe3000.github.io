# Repository assessment and proposed direction

17 October 2026. Scope: local source inspection of all 12 posts, three project pages, root pages, configuration, layouts, styles, navigation, gemspec and build workflow. Initial Git working tree was clean. No live-site, remote Pages-settings, external-link, browser or deployment check was performed. Ruby/Bundler are absent from this environment; build results remain unverified.

## What to preserve

Jekyll and the vendored Minimal Mistakes architecture fit a fast, static writing platform. Keep the theme's responsive layouts, semantic article structure, code highlighting, author information, RSS, sitemap and social metadata templates. Preserve article bodies, publication dates and URL-generating categories/slugs, including the historical jave-streams filename. Keep all three project pages and the personal reflections. No framework migration is justified.

The early technical writing is conversational, direct, sometimes irreverent, with concrete Java examples, short sections and recurring LinkedIn sign-offs. Logging has a natural personal opening. The career and family essays are more reflective and provide an authentic account of developing judgement. Future articles should retain specificity and warmth while developing fewer claims in greater depth; do not mechanically remove humour or personal material.

## Findings and priorities

| Priority | Evidence | Proposed action |
| --- | --- | --- |
| P0 | No draft system or persistent publication guidance | Implement private draft directory, unpublished post defaults, creation tool and excluded editorial workspace. Explicitly opt historical posts in without changing bodies. |
| P0 | Workflow builds only when repository equals mmistakes/minimal-mistakes and targets docs/ | Confirm actual Pages settings before proposing a separate validation pipeline and approval-controlled deployment. Do not silently change live deployment. |
| P1 | Site URL/repository unset; description only covers tutorials | Confirm canonical origin, add accurate positioning and per-page descriptions after direction approval. Existing SEO template/feed/sitemap plugins provide a sound base. |
| P1 | Contact uses email.com while About/config use gmail.com | Confirm and consolidate contact address; remove unsupported response-time promise. |
| P1 | category_archive/tag_archive point to absent pages; _pages is empty | Add category/tag archives preserving existing category names and URLs. |
| P1 | Three project banners reference nonexistent assets/images files | Supply real images or remove banner references after review. Do not fabricate product screenshots. |
| P1 | SOLID opens a Java code fence without closing it | Propose a formatting-only correction separately from article revisions. |
| P1 | CSS forces mobile root font to 12px; shared banner is about 2.25 MB | Prototype readable mobile type, bounded line length, restrained headers and optimized imagery; verify in browser. No measured performance/contrast score yet. |
| P2 | Homepage/About say seven years; broad billboard market claims; projects include strong metrics | Review current biography against the supplied eight-plus years. Confirm product naming, contribution scope and evidence before promoting claims. |
| P2 | Markdown list markers often lack spaces; examples vary in code formatting | Review formatting per article without changing meaning. Add relevant cross-links after author approval. |
| P2 | Homepage is index.md while paginate is configured | Verify actual pagination during build; do not assume the paginator works from configuration alone. |

## Historical article review

These are source-review observations and research questions, not a verified technical errata list. Reproduce examples and consult authoritative documentation before revising claims.

| Article | Review opportunity and natural continuation |
| --- | --- |
| Why Clean Code Matters | Preserve opening series context; review nested code/list rendering and qualify method-size rules. Follow with costs of competing design choices. |
| The Real Signs You Need SOLID Principles in Your Code | Unclosed code fence; review list rendering. Explain when introducing abstractions costs more than it saves. |
| How to Use Java Streams Effectively | Revisit one-liner advice, flatMap example described as nesting and side-effect discussion; add measured trade-offs rather than generic performance claims. |
| Layered Architecture Simplified | Example dependencies are illustrative/incomplete. Discuss transaction boundaries and cases where extra layers add little value. |
| What Makes a Good API | Extend beyond endpoint conventions to compatibility, retries, idempotency and error contracts; qualify always-JSON recommendation. |
| Non-functional Development | Good bridge into operational writing; turn tool lists into requirements and measurable acceptance criteria. |
| Approaching load balancing | Strong operational angle; review developer/operations ownership framing, retry amplification and health semantics. |
| Event-Driven Architecture with Spring Boot | Review Kafka generic-type mismatch, missing consumer/deserializer setup, annotation/class naming collision and misleading transaction-publish comment. Reproduce with explicit dependencies before edits. Distinguish in-process events from durable messaging. |
| Make Logging Work for You | Preserve personal opening. Verify logging API levels and kv dependency; examine exception swallowing and payment-value representation in sample. Add privacy, retention and cost constraints. |
| How I am using AI Responsibly to chase 10x Engineering | Preserve stated scepticism and responsibility; avoid another generic AI productivity article. A later piece could assess a specific workflow with evidence. |
| Starting a New Chapter as a Senior Developer & Reflections | Preserve date/title as career history. Natural follow-up: mentoring questions that improved judgement, with author-provided examples. |
| Balancing Engineering, Growth, and Family Life | Preserve personal voice and family context. Robotics torque constraints offer a concrete industrial-engineering continuation; no invented build outcomes. |

Project review: ChromaSign needs confirmation of product identity relative to Polycloud and evidence for frame-perfect playback/zero-major-crash claims. PAYG solar mixes historical implementation and modernization plans; clarify current status and qualify PHP scalability claims. Sun tracker contains a component-name placeholder, describes LDRs as diodes, and states up-to-30-percent yield without measurement context. Preserve originals pending approval and evidence.

## Proposed information architecture and design

Keep Home / Writing (existing /blog/) / Projects / About / Contact. Add Topics as an archive view, retaining legacy categories for routing. Use a separate editorial-topic field for the five new pillars so organizing historical content does not break URLs. Empty pillars should be described as future coverage rather than populated with invented articles.

Proposed homepage: concise identity as Senior Software Engineer; Java/distributed systems and industrial roots; selected writing; selected product work; invitation to professional discussion. Use only confirmed experience. The user-supplied Polycloud R10m-plus over approximately five years is a candidate proof point, subject to confirmation that it is suitable for public disclosure and clarification of personal contribution. Do not present business revenue as personal revenue.

Retain the air skin as a base. Prototype charcoal text, a restrained blue accent, generous whitespace, readable system fonts, a 65–75-character reading measure, visible keyboard focus, responsive code overflow and smaller article headers. Prefer real engineering diagrams where they clarify a specific argument. No animation or decorative imagery is needed.

## Incremental delivery and review gates

1. Foundation (local changes prepared): documentation, audit, backlog, private draft creation and conservative defaults. Validate source rules; obtain a real Jekyll build before merging.
2. Quick wins after direction approval: contact correction, missing archives, project-banner fallback, SOLID fence fix, canonical configuration after confirmation. Keep formatting fixes separate from factual revisions.
3. Design prototype: homepage and reading styles using existing layouts; inspect desktop/mobile, keyboard access, contrast, code and image layouts. Present screenshots and diff before commit approval.
4. Content depth: one researched outline at a time, author input, raw draft, author revision, final checks, explicit publication approval and separate LinkedIn review.
5. Deployment: inspect actual Pages settings, introduce meaningful CI without publishing unapproved drafts, validate generated links/metadata/draft isolation, then request exact commit/push approval.

Unresolved checks: YAML parsing, full build/doctor, generated navigation and links, feeds/sitemap/search isolation, external HTTP links, responsive rendering, accessibility and performance measurements. Source findings must not be represented as completed runtime checks.
