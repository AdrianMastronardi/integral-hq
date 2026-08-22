# Contributing

Issues and pull requests are welcome. Participation is governed by the [Code of Conduct](CODE_OF_CONDUCT.md).

## Scope

Integral is a framework for covering the software product lifecycle from discovery to verified capability operating in production, preserving a digital thread from the original intent to what actually runs. Contributions should preserve that purpose.

The project is at scaffolding stage: the conceptual model is still being drafted and no implementation exists yet. Until it lands, open an issue before anything beyond a typo or a small clarification, so that the change and the model do not diverge.

## Authorship

Agents draft in this repository by design, so agent authorship is the normal case rather than an exception to disclose. What a contribution needs is not a note about what wrote it, but someone who stands behind it: you have exercised the change, you can explain why it is needed and how it fits the project, and you can defend it in review.

A contribution that no one has run, that answers no stated need, or that arrives in bulk with no sign of review will be closed regardless of what produced it.

## Working in this repository

Repository artifacts — documentation, instructions, examples, and user-facing messages — are written in English.

Keep each Markdown paragraph and list item on one logical source line. Hard-wrapped prose turns a one-word edit into a reflowed paragraph, which is why line length is not enforced and manually aligned tables are not required.

Install the commit gate once:

```sh
uvx pre-commit install
```

It checks merge-conflict markers, end-of-file and trailing-whitespace normalization, oversized files, private keys, and hardcoded secrets, lints Markdown, and verifies that `CLAUDE.md` holds nothing but its import and an HTML comment explaining the arrangement. Run it over the whole tree with:

```sh
uvx pre-commit run --all-files
```

The same hooks run on every pull request, so the gate holds whether or not it was installed locally.

## Pull requests

`main` is protected and takes no direct pushes: every change arrives as a pull request from a branch. The rules apply to everyone, maintainers included, so the history of the default branch is the history of what went through review.

A pull request merges once the `pre-commit-gate` check is green and the branch is up to date with `main`. An approving review from a second person is not required — the gate is the check, not a queue for someone else's attention — so a contributor is never blocked waiting on availability, only on a red check. History on `main` stays linear: merge with squash or rebase rather than a merge commit.

Every commit that reaches `main` must be signed. Configure signing once, then register the key with GitHub as a *signing* key, which is a different list from the authentication keys:

```sh
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true
```

## Agent instructions

Instructions for coding agents live in [AGENTS.md](AGENTS.md), which every agent reads directly. `CLAUDE.md` is only the bridge that imports it, and a commit hook rejects anything there beyond that import and an HTML comment explaining the arrangement. Every change to how agents work in this repository goes in `AGENTS.md`.

## Changelog

Add notable changes to the `Unreleased` section of [CHANGELOG.md](CHANGELOG.md). What counts as notable, how entries are sorted, and how a release is cut are documented in [AGENTS.md](AGENTS.md): the same brief applies whether a person or an agent writes the entry.

Repository upkeep — formatting rules, editor configuration, commit-time checks — is deliberately not itemized there.

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE) that covers this project.
