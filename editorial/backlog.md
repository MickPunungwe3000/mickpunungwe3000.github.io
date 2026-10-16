# Proposed editorial roadmap

Status: ideas for author review, not approved articles. Aim for two substantive articles per month after the first outline is approved; do not impose publication dates before evidence and author review are ready. Every article and associated LinkedIn draft requires its own approval. No publishing automation.

Topic pillars: Software Engineering & Architecture; Product Engineering & Building; Industrial Technology & Infrastructure; Business, Technology & Strategy; Engineering Leadership & Professional Growth.

## First three months

| Slot / proposed title | Main argument or research question | Audience / category | Why it matters and existing connection | Supporting material and author input | LinkedIn angle |
| --- | --- | --- | --- | --- | --- |
| Month 1 A: Building Software Is Not the Same as Building a Product | What work remains after software functions correctly? | Senior engineers and founders / Product Engineering & Building | Extends non-functional development into customer value, operations and commercial constraints | Author-provided product decision; outline lifecycle costs; distinguish hypotheses from experience | One decision that looked technical but depended on customer workflow |
| Month 1 B: What Happens When an Event Is Delivered Twice? | How should a consumer handle duplicate delivery and partial failure? | Backend engineers / Software Engineering & Architecture | Deepens the existing EDA article rather than repeating definitions | Reproducible Java example, broker documentation, explicit delivery assumptions, failure injection; no employer internals | Ask where teams place deduplication responsibility |
| Month 2 A: A Robotic Arm That Could Not Lift Itself | How do torque and geometry constrain a design before code runs? | Software and embedded engineers / Industrial Technology & Infrastructure | Continues the author's May 2026 reflection with an actual engineering question | AUTHOR INPUT REQUIRED: dimensions, motor specifications, calculations, photographs and current status; verify units and payload assumptions | A concrete design constraint that changed the build |
| Month 2 B: Architecture or Added Complexity? | When does another abstraction reduce change cost, and when does it increase it? | Senior engineers / Software Engineering & Architecture | Builds on SOLID and layered architecture | Two bounded worked examples; maintenance scenarios; author judgement on acceptable duplication | Invite examples of abstractions a team later removed |
| Month 3 A: Operational Software for African Businesses | Which workflows make viable software opportunities, and what limits adoption? | Founders and product engineers / Business, Technology & Strategy | Broadens product/industrial work into a testable market question | Pick a country, industry and workflow; primary statistics, customer interviews with permission, payment/support constraints; avoid continent-wide generalizations | One narrow operational bottleneck and an open research question |
| Month 3 B: The Questions That Make Mentoring Useful | Which questions help another engineer develop independent judgement? | Senior engineers and mentors / Engineering Leadership & Professional Growth | Continues the November career reflection | AUTHOR INPUT REQUIRED: anonymised real examples, what changed and what did not; no invented conversations | Share one author-confirmed review question and invite alternatives |

## Later candidates

| Proposed title | Argument / audience / category | Why it matters and overlap | Required evidence or research | LinkedIn angle |
| --- | --- | --- | --- | --- |
| Lessons from a Commercial Digital Signage Platform | How reliability, operator needs and cost interact / engineers and founders / Product Engineering & Building | Develops project pages into an evidence-backed case study | Confirm Polycloud versus ChromaSign, personal contribution, publishable revenue basis and period; choose one real decision | A product constraint that changed an engineering choice |
| Retries Can Turn a Slow Dependency into an Outage | Retry budgets affect system load / backend engineers / Software Engineering & Architecture | Continuation of load-balancing and reliability posts | Reproducible load experiment, backoff/jitter documentation, assumptions and measurements | Show one measured retry amplification result |
| When Automation Is Worth More Than a New Product | Compare savings, adoption cost and maintenance burden / operators and founders / Business, Technology & Strategy | Connects business process quality to commercial engineering | One specific workflow; transparent cost model and sensitivity analysis; author opinion | Ask what repeated work is still done manually |
| What Embedded Systems Taught Me About Backend Reliability | Which principles transfer across physical and enterprise systems? / cross-domain engineers / Industrial Technology & Infrastructure | Uses distinctive experience without retelling a CV | Author-confirmed examples; separate analogy from actual equivalent failure behaviour | One cross-domain lesson and where it stops applying |
| Engineers Should Understand the Economics of Their Systems | How operating costs change a design decision / senior engineers / Product Engineering & Building | Adds cost reasoning to non-functional requirements | Explicit workload, verified dated prices, scenario model, maintenance assumptions | A cost trade-off with stated assumptions |
| Financial Infrastructure and Industrial Operations | What integration problem is worth solving in a specific market? / engineers and founders / Business, Technology & Strategy | A research-led longer-term piece, not a broad prediction | Narrow geography/use case; authoritative payment/industry sources; separate regulatory facts, assumptions and opinion | Present the research question before making predictions |

## Workflow for each slot

1. Idea: approve or adjust the argument, audience and category above.
2. Research and outline: store source URLs, dates, reproducible examples and counterarguments in editorial/. No source has yet been verified for these proposed articles.
3. Raw draft: use scripts/new_draft.py; expand only from evidence. Mark personal gaps with [AUTHOR INPUT REQUIRED: ...], uncertain facts with [VERIFY: ...], and positions with [AUTHOR OPINION REQUIRED: ...].
4. Author review: Maverik rewrites, adds experience, challenges the argument and decides the voice.
5. Final review: check facts, examples, citations, grammar, layout, metadata and publication isolation without changing opinions silently.
6. Publication approval: present final blog content and a separate LinkedIn draft. Explicit approval is required before publication and before any commit/push. A LinkedIn draft introduces one idea, invites substantive discussion and uses the approved canonical article link where useful. Never publish directly.
