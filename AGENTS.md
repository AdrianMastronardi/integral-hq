# AGENTS.md

Instructions for coding agents working in this repository. Claude Code reads `CLAUDE.md`, which imports this file; Codex and other agents read this file directly.

## Commit gate

Every change is expected to pass the hooks in `.pre-commit-config.yaml`: merge-conflict markers, end-of-file and trailing-whitespace normalization, oversized files, private keys, hardcoded secrets, and Markdown linting. Install them once with `uvx pre-commit install`.

Do not add a hook that requires a changelog edit on every change. It teaches contributors to add a line to pass the check, which is how a changelog fills with noise. Automation handles mechanics; judgment stays with people.

## Writing the changelog

`CHANGELOG.md` is curated, not accumulated. A model may draft it, but a person decides what is notable and reads the result before anyone else does.

- Summarize notable changes. Repository upkeep — formatting rules, editor configuration, commit-time checks — is rarely notable enough to list; when it changes what a contribution must satisfy, say so in the release summary instead.
- Never paste a git log. A commit and a changelog entry are written for different readers, and the changes that matter often span several commits and need to be described from the reader's point of view.
- Sort each change into one of the six Keep a Changelog types — Added, Changed, Deprecated, Removed, Fixed, Security — and do not invent a seventh. What kind of change it is goes in the type; why it matters goes in the wording of the entry. Within a type, order entries in case-insensitive alphabetical order by filename, and omit types with no entries.
- Explain the reason in the entry, not only the mechanism.
- An entry that changes existing behavior states the boundary of that change: in the positive where possible — the condition under which the new behavior applies — and as a negation only where the entry itself leaves a neighboring case in doubt. One sentence at most, and only where existing behavior moved: a first appearance has no prior behavior to bound.
- Mark a breaking change with a **Breaking:** marker, kept with the entry it belongs to. The version number already signals it, but the number is easy to miss.
- Remove anything not worth reading. Then read what is left.

A release may open with a short summary before the type sections. Use it when the release is worth introducing — it is the right place for reasoning that would be noise as a per-file entry.

The drafting brief above follows the automation guidance in [Keep a Changelog 2.0.0](https://keepachangelog.com/en/2.0.0/). The alphabetical ordering and the boundary rule are this project's own.

## Cutting a release

A version heading and its reference definition at the bottom of `CHANGELOG.md` are two halves of the same link, and both move at release time.

1. Move everything under `## [Unreleased]` into a new `## [X.Y.Z] - YYYY-MM-DD` heading.
2. Rename the `[Unreleased]` definition to `[X.Y.Z]` and point it at a comparison with the version before it (`compare/vW.V.U...vX.Y.Z`). The oldest version links to its tag instead, since there is nothing earlier to compare it with.
3. Add a fresh, empty `## [Unreleased]` heading, with a definition pointing at `compare/vX.Y.Z...HEAD`.
4. Commit, tag that commit `vX.Y.Z`, and push the branch and the tag. The links resolve to nothing until the tag exists.
