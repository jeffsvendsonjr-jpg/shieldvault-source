# ShieldVault Detection Anthology

The Detection Anthology is ShieldVault's public, versioned body of evidence.

It documents what the detector is expected to stop, what it should merely pause, what it should allow, and which product surfaces have been tested against an exact release candidate.

This is not a claim that human intent can be known with certainty. Secret detection and behavioral judgment are measured separately because they have different standards of evidence.

## Outcomes

- **STOP** — high-confidence, objective risk such as a credential or private key.
- **PAUSE** — potentially regrettable or context-sensitive language that deserves a second look.
- **ALLOW** — no intervention is expected.
- **AMBIGUOUS** — reasonable reviewers may disagree; a hard stop is not permitted.

## Principles

1. No real credentials, private information, or user content may enter this repository.
2. Every example must be synthetic or safely redacted.
3. Secret misses and false positives are reported separately.
4. Behavioral cases may define an acceptable outcome range.
5. A platform is not called **Certified** merely because a content script loads there.
6. Known, unpatched bypass details remain private until corrected and safely documented.
7. A release report must name the exact build or commit tested.

## Layout

```text
anthology/
├── README.md
├── METHODOLOGY.md
├── schema/
│   └── case.schema.json
├── cases/
│   ├── secrets.json
│   └── behavior.json
├── surfaces/
│   ├── SURFACE_TEMPLATE.md
│   └── facebook.md
└── reports/
    └── REPORT_TEMPLATE.md
```

## Validate the corpus

The starter validator uses only Python's standard library:

```bash
python scripts/validate_anthology.py
```

The validator checks structure and safety invariants. It does **not** yet execute the production detector. Connecting the production detector to this corpus is the next implementation step and should happen in the private product repository.

## Public versus private testing

The public anthology contains representative synthetic cases, methodology, surface status, aggregate results, historical regressions, and known limitations.

A private adversarial suite may contain active bypass details, fragile selectors, proprietary tuning cases, and exploit reproduction steps. Once fixed, a sanitized regression case should be promoted into the public anthology.

## Release rule

A release candidate may not be described as commercially ready until:

- the corpus validates;
- all release-blocking secret cases pass;
- required submission paths pass on every Certified surface;
- behavioral results are reported without being combined into a misleading single accuracy score;
- known limitations are documented.
