# Surface Certification: [Platform]

- **Status:** Unsupported
- **Product version:** Not tested
- **Build or commit:** Not tested
- **Anthology revision:** Not tested
- **Test date:** Not tested
- **Browser / version:** Not tested
- **Operating system:** Not tested
- **Reviewer:** Not assigned

## Claimed scope

State exactly which editors and workflows are included. Do not let a platform name silently imply support for adjacent products.

## Required flows

### Editor discovery

- [ ] Editor present on initial page load
- [ ] Dynamically loaded editor
- [ ] Editor reopened after close
- [ ] Editor rediscovered after in-app navigation
- [ ] Multiple editors on one page

### Input paths

- [ ] Typed secret
- [ ] Pasted secret
- [ ] Multiline paste
- [ ] Harmless secret lookalike
- [ ] Behavioral PAUSE case
- [ ] Harmless behavioral control

### Submission paths

- [ ] Plain Enter
- [ ] Modified Enter, when supported
- [ ] Mouse click
- [ ] Touch or pointer activation
- [ ] Platform-specific keyboard shortcut
- [ ] Draft restored and submitted

### Warning behavior

- [ ] STOP prevents submission
- [ ] PAUSE preserves user agency
- [ ] Dismissal behavior works
- [ ] Edited text can be rescanned
- [ ] Warning identifies the reason without exposing the matched secret
- [ ] Repeated warnings do not trap the user

### Privacy

- [ ] Message text remains local
- [ ] No secret value enters logs
- [ ] No secret value enters analytics
- [ ] No secret value enters network requests
- [ ] Only approved aggregate metadata is emitted, if any

## Results

| Test area | Passed | Failed | Blocked | Notes |
| --- | ---: | ---: | ---: | --- |
| Editor discovery | 0 | 0 | 0 | |
| Input paths | 0 | 0 | 0 | |
| Submission paths | 0 | 0 | 0 | |
| Warning behavior | 0 | 0 | 0 | |
| Privacy | 0 | 0 | 0 | |

## Known limitations

List every known limitation that could affect the public claim.

## Certification decision

- [ ] Unsupported
- [ ] Experimental
- [ ] Beta
- [ ] Certified

**Decision rationale:**

**Approver:**
