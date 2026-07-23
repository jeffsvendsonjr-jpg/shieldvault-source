# ShieldVault Detection Report — [Version]

## Build identity

- **Product version:**
- **Build or commit:**
- **Test date:**
- **Browser / version:**
- **Operating system:**
- **Anthology revision:**
- **Private holdout revision:** Recorded privately / not used
- **Reviewer:**
- **Approver:**

## Executive decision

- [ ] PASS — commercially ready within documented scope
- [ ] CONDITIONAL PASS — limitations documented and accepted
- [ ] FAIL — release blockers remain

**Decision rationale:**

## Secret detection

| Measure | Result |
| --- | ---: |
| Required STOP cases | 0 / 0 |
| Harmless ALLOW controls | 0 / 0 |
| False negatives | 0 |
| False positives | 0 |
| Release-blocking misses | 0 |

### Secret failures

List each failed case by ID, observed outcome, expected outcome, severity, and remediation status.

## Behavioral protection

| Measure | Result |
| --- | ---: |
| Required outcomes matched | 0 / 0 |
| Acceptable-range outcomes matched | 0 / 0 |
| Prohibited outcomes produced | 0 |
| Harmless controls allowed | 0 / 0 |
| Nuisance pauses on controls | 0 |

### Behavioral disagreements and failures

Document ambiguous cases rather than forcing them into a single accuracy score.

## Surface certification

| Surface | Status | Input paths | Submission paths | Privacy | Notes |
| --- | --- | --- | --- | --- | --- |
| ChatGPT | Unsupported | Not tested | Not tested | Not tested | |
| Claude | Unsupported | Not tested | Not tested | Not tested | |
| Facebook | Beta candidate | Not tested | Not tested | Not tested | Messenger excluded |
| Reddit | Unsupported | Not tested | Not tested | Not tested | |
| X | Unsupported | Not tested | Not tested | Not tested | |
| LinkedIn | Unsupported | Not tested | Not tested | Not tested | |
| Gmail | Unsupported | Not tested | Not tested | Not tested | |
| Outlook | Unsupported | Not tested | Not tested | Not tested | |

## Submission-path results

| Path | Passed | Failed | Blocked | Notes |
| --- | ---: | ---: | ---: | --- |
| Typing | 0 | 0 | 0 | |
| Paste | 0 | 0 | 0 | |
| Plain Enter | 0 | 0 | 0 | |
| Modified Enter | 0 | 0 | 0 | |
| Mouse / pointer click | 0 | 0 | 0 | |
| Platform-specific shortcut | 0 | 0 | 0 | |
| Dynamic editor / navigation | 0 | 0 | 0 | |

## Privacy verification

- [ ] Message text remained local during every tested flow
- [ ] Secret values did not enter logs
- [ ] Secret values did not enter analytics
- [ ] Secret values did not enter network requests
- [ ] Warning UI did not unnecessarily repeat secret values

## Release blockers

1. None recorded.

## Known limitations

1. None recorded.

## Changes since prior report

Describe detector, interception, warning, or supported-surface changes that required retesting.

## Evidence attachments

List automated output, screenshots, screen recordings, browser logs, and manual test notes. Do not attach real user content or live credentials.
