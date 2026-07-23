# Detection Anthology Methodology

## Purpose

The anthology exists to make ShieldVault's recognition claims inspectable and repeatable.

It is designed to answer four separate questions:

1. Does ShieldVault recognize high-confidence secrets?
2. Does it avoid interrupting harmless lookalikes?
3. Does behavioral protection offer useful pauses without pretending to know intent?
4. Does the complete intervention flow work on each claimed platform and submission method?

## Evidence classes

### Secret detection

Secret cases use objective expected outcomes wherever possible.

- `STOP` is expected for a high-confidence synthetic credential, private key, validated financial identifier, or similarly concrete risk.
- `ALLOW` is expected for a harmless lookalike or invalid control.

A high-confidence secret miss is a release blocker unless explicitly waived with a written limitation and rationale.

### Behavioral protection

Behavioral cases are context-sensitive. They may define:

- one required outcome;
- an acceptable outcome range;
- an outcome that must never occur.

For example, an ambiguous sarcastic statement may reasonably produce `PAUSE` or `ALLOW`, but must not produce `STOP`.

Behavioral protection is evaluated as a guardrail, not a truth engine.

## Case requirements

Every case must include:

- a stable unique ID;
- a category;
- synthetic text;
- the expected outcome;
- a reason;
- confirmation that no real secret or personal data is present.

Behavioral cases should include context when context materially changes interpretation.

## Corpus rules

- Never copy real user text into the anthology.
- Never commit live credentials, even if revoked.
- Use unmistakably synthetic placeholders.
- Include positive cases and negative controls.
- Preserve historical regression cases after a bug is fixed.
- Do not tune the detector only against the public corpus; maintain a private holdout set.

## Metrics

Report these separately:

### Secrets

- true positives;
- false negatives;
- true negatives;
- false positives;
- release-blocking misses.

### Behavior

- required outcomes matched;
- acceptable-range outcomes matched;
- prohibited outcomes produced;
- nuisance pause rate on harmless controls;
- reviewer disagreement rate, when human review is used.

### Surfaces

- editor discovery;
- typing interception;
- paste interception;
- keyboard submission interception;
- mouse or touch submission interception;
- dynamically loaded editor support;
- navigation and editor-reopen behavior;
- privacy verification.

Do not combine all classes into one headline percentage. A debatable sarcasm classification is not equivalent to a missed private key.

## Surface status

- **Unsupported** — not claimed or not tested.
- **Experimental** — implementation exists but is incomplete or unstable.
- **Beta** — major flows work, but certification is incomplete or limitations remain.
- **Certified** — required flows passed on an exact release candidate and evidence is recorded.

A domain match alone does not qualify as support.

## Release gates

A release report must identify:

- product version;
- commit or immutable build identifier;
- test date;
- browser and operating-system versions;
- corpus revision;
- results by evidence class;
- surface status;
- unresolved release blockers;
- known limitations;
- reviewer or approver.

Any code change that can affect detection, editor discovery, interception, or warning behavior invalidates the relevant prior result and requires retesting.

## Disclosure policy

Active bypass details belong in the private adversarial suite until fixed. Public reports should state that a release blocker exists without publishing a usable exploit recipe.

After correction, add a sanitized regression case and record the fixed version.
