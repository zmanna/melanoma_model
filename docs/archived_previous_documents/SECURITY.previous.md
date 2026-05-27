# Security and Privacy

## Status

This project is an academic prototype. It does not implement privacy or security controls required for real health data.

Do not deploy this repository as a public medical-image service without a full security, privacy, legal, and clinical review.

## Do Not Upload

- private medical images
- personally identifying images
- patient data
- protected health information
- images that should not be stored on disk

## Current Risks

- Uploaded files are written to `backend/uploads/`.
- There is no authentication.
- There is no encryption or access-control layer.
- There is no data retention policy.
- The app is not HIPAA-compliant.
- The repository contains sample uploaded images.
- File extension checks are present, but the app does not provide production-grade malware scanning, image validation, rate limiting, or abuse controls.

## Repository Hygiene

Before heavily featuring or deploying this project, remove:

- `__pycache__/`
- `.DS_Store`
- non-essential uploaded images
- any private or identifying images

Keep only redacted, licensed, or clearly permitted sample assets.

## Safer Future Direction

Before any public demo or deployment:

- store uploads outside the repository
- delete uploads after inference or define a retention policy
- add size limits and stricter content validation
- remove private, identifying, or unlicensed images
- document the dataset license and permitted sample assets
- add explicit user-facing warnings before upload
