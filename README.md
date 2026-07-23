# ShieldVault — Source Repository

This repository fulfils the **source-availability requirement** of the
[Business Source License (BSL)](https://mariadb.com/bsl11/) under which
ShieldVault is distributed.

## Source downloads

| File | Contents |
| --- | --- |
| [`shieldvaultmirrorupdate.zip`](shieldvaultmirrorupdate.zip) | Full extension source |

Download the zip to read, audit, or build ShieldVault from source.

## Detection Anthology

The [`anthology/`](anthology/) directory is ShieldVault's public, versioned
"show your work" evidence layer.

It separates:

- objective secret detections that should **STOP** submission;
- behavioral risks that should invite a **PAUSE** without pretending to know intent;
- harmless controls that should be **ALLOWED**;
- per-platform certification against an exact release candidate.

Run the zero-dependency corpus validator with:

```bash
python scripts/validate_anthology.py
```

The public corpus contains only synthetic examples. Active bypass details and
proprietary adversarial cases remain private until they can be safely disclosed
as fixed regression cases.

## License

ShieldVault is source-available under the **Business Source License**.
See the `LICENSE` file inside each zip for the full terms.

The BSL allows you to read, audit, and build from source for personal
verification. Redistribution and competing commercial use are restricted
per the license terms.

---

*ShieldVault — Detection without possession.*
