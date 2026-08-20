# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog 2.0.0](https://keepachangelog.com/en/2.0.0/), and the project adheres to [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).

How entries are written — what counts as notable, how they are sorted, how an entry states the boundary of a change in behavior — is recorded in `AGENTS.md`, where the agents that draft them read it.

## [Unreleased]

## [0.0.1] - 2026-08-20

Initial scaffolding for ProductFoundry, a framework intended to cover the software product lifecycle from discovery to verified capability operating in production, preserving a digital thread from the original intent to what actually runs.

This release contains no implementation. It establishes licensing, the terms of contribution, the documentation entry point, the Markdown and line-ending rules the repository is written to, the editor configuration and ignore rules that keep those rules from depending on a per-contributor setup, the brief coding agents draft from, and the commit-time checks that every later change is expected to pass. The implementation stack is deliberately still undecided, so the line-ending rules, diff drivers, and lockfile declarations already cover the common source and package-manager formats: choosing a stack later does not mean revisiting repository plumbing.

The commit gate is adopted now rather than later, while it is still cheap. With the history at two commits, the whitespace and end-of-file hooks rewrite nothing and the secret scan has almost nothing to cover; the same hooks adopted against a grown tree produce a first commit of pure noise that hides the real change. Installing it locally is opt-in, so the same hooks run in continuous integration on every pull request as well: the gate holds whether or not a contributor installed it.

### Added

- `AGENTS.md`: records the brief agents draft the changelog from — what counts as notable, why a git log is not a changelog, how entries are sorted, and how an entry states the boundary of a change in behavior — together with the commit gate every change is expected to pass.
- `CHANGELOG.md`: starts the release log, following the Keep a Changelog types and pointing at the brief its entries are written from.
- `CLAUDE.md`: bridges Claude Code to `AGENTS.md`, which Codex and other agents read directly. It carries that import and an HTML comment explaining the arrangement, and a commit hook rejects anything else, so the two cannot drift.
- `CODE_OF_CONDUCT.md`: adopts the Contributor Covenant 2.1 verbatim, with reports going to <adrian@mastronardi.xyz>. It does nothing while the project has one contributor; it is added now because adding it after an incident reads as a reaction to that incident.
- `CONTRIBUTING.md`: states the project's scope, the English and Markdown conventions, the commit gate to install, and where the changelog brief lives, so a contributor is not expected to reconstruct them from the configuration files. Agent authorship is treated as the normal case: what a contribution needs is someone who stands behind it, not a disclosure of what wrote it.
- `LICENSE`: licenses the project under the MIT License, with copyright held by ProductFoundry Contributors.
- `README.md`: names the project and states its purpose in a single line.

[Unreleased]: https://github.com/AdrianMastronardi/product-foundry-hq/compare/v0.0.1...HEAD
[0.0.1]: https://github.com/AdrianMastronardi/product-foundry-hq/releases/tag/v0.0.1
