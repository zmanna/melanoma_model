# Roadmap

## Phase 0: Preserve And Clean

Goal: make the repository understandable and safe to review.

- archive previous documentation
- create current operating docs
- add `.gitignore`
- remove tracked caches and OS metadata
- review uploaded images for privacy and licensing
- document model artifact provenance
- identify thresholds and current behavior

## Phase 1: Stabilize The Prototype

Goal: make the demo predictable.

- pin Python dependencies
- add a repeatable setup command
- move upload storage outside source-controlled paths
- add Flask route smoke tests
- add preprocessing unit tests
- rename raw score fields honestly
- align threshold constants or document separate threshold policies

## Phase 2: Reproduce The Model

Goal: make model results auditable.

- define dataset source and permitted use
- create split manifests
- save training environment details
- set random seeds where possible
- generate evaluation artifacts
- fix version logging
- compare baseline CNN against transfer-learning models

## Phase 3: Govern The Model

Goal: prepare for serious review.

- create model-card release templates
- add threshold-selection rationale
- analyze false negatives and false positives
- evaluate calibration
- test across image quality conditions
- document subgroup performance where data supports it
- establish model approval gates

## Phase 4: Product Discovery

Goal: find a responsible workflow.

- interview dermatology stakeholders
- map user risks and incentives
- design clinician-in-the-loop flows
- avoid autonomous diagnosis UX
- define user consent and warning copy
- test whether the product solves a real workflow problem

## Phase 5: Compliance And Pilot Planning

Goal: determine whether commercialization is justified.

- obtain legal and regulatory review
- perform privacy and security design
- define data retention policy
- prepare pilot protocol
- establish clinical oversight
- define success and stop criteria

## Non-Negotiables

- no patient-facing diagnostic claims without proper validation and regulatory review
- no private image uploads in the current app
- no use of unlicensed datasets or sample assets
- no performance claims that cannot be reproduced

