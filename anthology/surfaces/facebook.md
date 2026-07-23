# Surface Certification: Facebook

- **Status:** Beta candidate — not certified
- **Product version:** Pending release candidate
- **Build or commit:** Pending
- **Anthology revision:** `1.0` starter corpus
- **Test date:** Not tested
- **Browser / version:** Not tested
- **Operating system:** Not tested
- **Reviewer:** Not assigned

## Claimed scope

This checklist covers Facebook on the desktop web at `facebook.com` only:

- Create Post composer;
- comments;
- replies.

It does **not** include Messenger, mobile applications, Facebook Lite, Marketplace messages, Groups-specific moderation tools, or Meta Business Suite unless those surfaces are separately tested and recorded.

A Facebook host permission or successful content-script injection does not by itself qualify as support.

## Required flows

### Editor discovery

- [ ] Create Post composer discovered after opening
- [ ] Create Post composer rediscovered after closing and reopening
- [ ] Comment editor discovered on initial feed items
- [ ] Comment editor discovered on dynamically loaded feed items
- [ ] Reply editor discovered after expanding a thread
- [ ] Editors rediscovered after Facebook in-app navigation
- [ ] Multiple visible composers do not share or corrupt state

### Input paths

- [ ] Typed high-confidence synthetic secret
- [ ] Pasted high-confidence synthetic secret
- [ ] Multiline private-key fixture
- [ ] Harmless secret lookalike
- [ ] Behavioral PAUSE case
- [ ] Ambiguous behavioral case
- [ ] Harmless strong-language control
- [ ] Text edited after an initial warning

### Submission paths

- [ ] Create Post — mouse click on Post
- [ ] Create Post — supported keyboard submission path
- [ ] Comment — Enter submission
- [ ] Comment — mouse or pointer submission where available
- [ ] Reply — Enter submission
- [ ] Reply — mouse or pointer submission where available
- [ ] Submission immediately after typing
- [ ] Submission immediately after paste
- [ ] Submission after draft restoration or composer reopen

### Warning behavior

- [ ] STOP prevents the exact attempted submission
- [ ] PAUSE interrupts without claiming certainty about intent
- [ ] User can revise and rescan
- [ ] User can deliberately proceed from a PAUSE
- [ ] Secret value is not repeated in the warning UI
- [ ] Warning attaches to the correct Facebook composer
- [ ] Repeated warnings do not lock the composer
- [ ] Facebook draft text remains intact after intervention

### Privacy

- [ ] Message text remains local
- [ ] No secret value enters console or extension logs
- [ ] No secret value enters analytics or telemetry
- [ ] No secret value appears in network requests
- [ ] DOM inspection is limited to what is needed for editor and submission handling

## Results

| Test area | Passed | Failed | Blocked | Notes |
| --- | ---: | ---: | ---: | --- |
| Editor discovery | 0 | 0 | 0 | Not executed |
| Input paths | 0 | 0 | 0 | Not executed |
| Submission paths | 0 | 0 | 0 | Not executed |
| Warning behavior | 0 | 0 | 0 | Not executed |
| Privacy | 0 | 0 | 0 | Not executed |

## Known limitations

- Facebook support has not yet been verified against an exact ShieldVault release candidate.
- Messenger is explicitly outside this certification scope.
- Facebook frequently changes dynamic editor markup; selector resilience and in-app navigation must be tested rather than assumed.
- Mouse-click Post/Comment interception is a release blocker until demonstrated against the candidate build.

## Certification decision

- [ ] Unsupported
- [ ] Experimental
- [x] Beta candidate
- [ ] Certified

**Decision rationale:** Facebook is a confirmed target surface, but no public evidence currently supports a Certified claim.

**Approver:** Pending
