# Codebase Discovery Guide

## Detection Heuristics

### Monorepo Detection
- Multiple `package.json` files in different directories
- `workspaces` field in root package.json
- Turborepo/Nx/Lerna configuration files
- Shared packages directory (packages/, libs/, apps/)

### Project Type Detection
Examine dependencies and directory structure:
- **Frontend**: React/Vue/Angular deps, components/ directory
- **Backend**: Express/Fastify deps, routes/ or controllers/
- **Fullstack**: Next.js/Remix, API routes in same codebase
- **Monorepo**: Multiple packages with shared configuration
