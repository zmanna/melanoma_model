# Security and Privacy

## Current Posture

DermaScan is an academic prototype and should be treated as unsafe for real medical or personally identifying images.

The current app:

- accepts user-uploaded image files
- writes uploads to local disk
- does not authenticate users
- does not encrypt or isolate uploaded files
- does not define retention or deletion behavior
- does not implement HIPAA-grade controls
- does not perform production-grade abuse prevention

## Do Not Upload

Do not upload:

- private medical images
- patient images
- protected health information
- personally identifying photos
- images that should not be stored on disk
- images without clear usage rights

## Commercialization Requirement

Before any public demo, pilot, or commercial product work, the project needs a security and privacy redesign.

Minimum future requirements:

- upload size limits
- strict content validation
- malware scanning or equivalent file safety controls
- storage outside the source repository
- encryption in transit and at rest
- explicit retention/deletion policy
- user consent flow
- audit logging
- access controls
- privacy review
- legal review
- incident response plan

## Repository Hygiene Risks

The repository has historically included generated caches, `.DS_Store` files, a packaged model artifact, and uploaded images. Historical uploaded files now live under `artifacts/sample_inputs/legacy_uploads/`; runtime uploads belong under `var/uploads/`.

A commercialization track should review all committed assets for licensing, privacy, and necessity.

Keep only assets that are:

- licensed for public use
- non-identifying
- intentionally documented
- necessary for reproducibility or demonstration
