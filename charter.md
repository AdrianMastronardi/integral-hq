---
type: Charter
title: Integral
description: Constitutional authority for Integral, an operating system for agentic product development.
resource: https://github.com/AdrianMastronardi/integral-hq/blob/main/charter.md
tags: [governance, product-development, agentic-systems]
---

# Integral

**Change without losing intent.**

An operating system for agentic product development.

Self-contained reference for the Discovery → Design → Build process: what it is, what it fixes, how it works, and the exact meaning of every term it coins.

Audience: engineers, architects, and the coding agents that read this as context. It assumes familiarity with version control, continuous integration and multi-repository systems. It assumes no prior exposure to Integral, and no particular delivery methodology.

## Contents

1. [Overview](#1-overview)
2. [The problem](#2-the-problem)
3. [How Integral solves it](#3-how-integral-solves-it)
4. [Theoretical framework](#4-theoretical-framework)
5. [Definitions](#5-definitions)
6. [The artifact model](#6-the-artifact-model)
7. [Identity and the graph](#7-identity-and-the-graph)
8. [Promotion and gates](#8-promotion-and-gates)
9. [The execution model](#9-the-execution-model)
10. [Constitutional principles](#10-constitutional-principles)
11. [Intellectual lineage](#11-intellectual-lineage)
12. [Open questions](#12-open-questions)
13. [Common misreadings](#13-common-misreadings)

## 1. Overview

Integral is a framework for running the software product lifecycle from first signal to verified capability in production, while keeping a traceable, machine-navigable connection between the reason a change exists and the code that implements it.

It is not a specification generator, a backlog methodology, or a coding workflow. It is the layer that keeps those honest with each other.

### Characteristics

| Property                 | What it means in practice                                                                                                                              |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Methodology-agnostic** | Assumes no Agile, Scrum, SAFe, sprints or story points. It models kinds of knowledge, not ceremonies                                                   |
| **Agent-first**          | The principal reader is a coding agent working within a context window, not a person with institutional memory                                         |
| **Graph-native**         | Artifacts are nodes with typed relations. Traceability is a query, never a maintained matrix                                                           |
| **Deterministic gates**  | Every automated check is computable without a language model. Given the same validator version and declared inputs, it always produces the same result |
| **Forge-independent**    | The traceability core needs plain git. Forges add execution-state resolution; runtime completion requires configured external authorities              |
| **Multi-repository**     | Planning and traceability across repositories are first-class. Portable integration and activation remain an explicit open contract                    |
| **Format-minimal**       | Markdown with YAML frontmatter. If you can `cat` a file you can read it; if you can `git clone` you can ship it                                        |

### The one-sentence claim

> Every implementation change governed by Integral is traceable back to the product intent that justified it, and every affected requirement in a completed Work Package is traceable forward to verified implementation and runtime evidence.

## 2. The problem

### 2.1 Knowledge and code diverge

Product knowledge and the software that implements it diverge the moment they are written down separately. A decision is made in a meeting, recorded in a document, and implemented in a repository. Six months later the code has moved and the document has not.

Nothing in ordinary tooling detects this. A test suite verifies that code does what code does. No check asks whether the code still does what someone decided it should do.

The answer to _why does this exist_ survives in tribal knowledge, which leaves when people leave.

This is not new, and it is not for lack of trying. Traceability has been a recognized good practice in systems engineering for forty years. It is rarely sustained, because the cost of maintaining it was paid by people who already knew the answer and therefore did not need the record.

### 2.2 Agents make it load-bearing

An agent does not hold the repository in its head. It holds a window.

Every decision an agent makes is built from whatever fitted inside that window. When product knowledge is scattered across documents, tickets, threads and heads, the agent does not load it. It works without it, and produces code that is locally correct and globally incoherent, faster than anyone curates the knowledge that would have justified it.

The consequence is precise, and it is the reason this framework exists:

> **Knowledge that cannot be reached within a context budget does not exist for whoever writes most of the code today.**

### 2.3 What breaks in practice

| Symptom                                                         | Underlying cause                                      |
| --------------------------------------------------------------- | ----------------------------------------------------- |
| A change is made that a past decision already ruled out         | Rejected alternatives are not recorded as artifacts   |
| Documentation is known to be stale and nobody knows which parts | Staleness is not derived from anything; it is noticed |
| A requirement changes and the blast radius is guessed           | No typed graph, so impact cannot be computed          |
| Work spans four repositories and nothing tracks the whole       | Git has no cross-repository transaction               |
| "Done" means merged, but the capability does not work           | Merge is confused with verified operation             |
| An agent asks why some code exists and gets no answer           | The thread from intent to code was never recorded     |

## 3. How Integral solves it

Four mechanisms. Each is necessary; none is sufficient alone.

### 3.1 A digital thread, recorded rather than remembered

Every artifact declares where it came from. The chain from intent to running code is a graph the system holds, not a story people retell.

```text
Intent → Outcome → Capability → Requirement ───────────────► Work Item → Code → Evidence
                                      └──► Decision ───────►┘
```

Decision is an optional branch of the thread, not a mandatory ceremony between Requirement and Work Item. A Work Item implements a Requirement directly. When an explicit solution commitment exists, the Work Item also follows the corresponding Decision.

Traversal works in both directions. Forward answers _what became of this requirement_. Backward answers _why does this code exist_.

### 3.2 A trust boundary, crossed by promotion

Exploration is allowed to be messy. Shared truth is not. The two live in separate spaces, and moving between them is a guarded event called **promotion**, never a file move.

```text
Discovery Space              Canon
(personal, messy,     ──►    (shared, curated,
 non-authoritative)   gate    authoritative)
```

### 3.3 Deterministic gates, not review discipline

Promotion is blocked when computable gate conditions fail. Not "someone should check that every requirement has a work item" but a gate that counts them and refuses.

Deterministic is the operative word. A gate that consults a language model may produce different results for identical declared inputs, which destroys the only property a gate has.

### 3.4 Derived knowledge, generated rather than maintained

Traceability matrices, impact reports, coverage summaries, dependency graphs: all computed from the artifacts and the graph. None of them is a document someone updates.

A manually maintained summary is a document that will eventually lie. The framework's answer is to not have any.

## 4. Theoretical framework

### 4.1 The ontology: nine kinds of knowledge

The core insight is that the chain below is **not a hierarchy of size**. Each step answers a fundamentally different question, and the difference is in kind, not in magnitude.

One question stands before that chain: **under whose authority may this body of Canon exist and decide?** `charter.md` answers that constitutional question. It does not enter the count below because it is structural authority, not a Canon artifact. Intent onward classifies knowledge inside an authority boundary; the Charter constitutes that boundary.

| Concept            | Question it answers                                           |
| ------------------ | ------------------------------------------------------------- |
| **Intent**         | Why should this exist?                                        |
| **Outcome**        | What result means success?                                    |
| **Capability**     | What must the product be able to do?                          |
| **Constraint**     | What must this work not violate?                              |
| **Source**         | What separately governed authority or evidence argues for it? |
| **Requirement**    | What must be true?                                            |
| **Decision**       | What durable solution commitment governs the work?            |
| **Work Item**      | What change must be executed?                                 |
| **Implementation** | What actually implements it?                                  |

An Intent may be one sentence. A Decision may run fifty pages. A Requirement may touch ten repositories. A Work Item may change one file. **Size does not determine the category. Meaning does.**

These are also not lifecycle statuses. An artifact does not become a Requirement by moving through a workflow. It is a Requirement because it states something that must be true.

Seven of the nine advance the chain. Constraint and Source do not. A Constraint is already true when the work starts, and the work has to hold within it. A Source is governed outside the decision boundary of the work that consumes it. It may be internal or external to the organization. **A Requirement is something this work must make true. A Constraint is something already true that this work cannot violate. A Source is the separately governed authority or evidence one of them rests on.**

#### Classification test

When the category is unclear, ask in order:

1. Does it explain **why the change matters**? → Intent
2. Does it describe **the state that means success**? → Outcome
3. Does it describe **what the system must be able to do**? → Capability
4. Is it **already true, and must this work avoid breaking it**? → Constraint
5. Is its truth **governed outside this work's decision boundary, and cited rather than decided here**? → Source
6. Does it state **an obligation this work must make true**? → Requirement
7. Does it establish a **durable solution commitment that subsequent work must follow**? → Decision
8. Does it describe **an executable unit of work**? → Work Item
9. Is it **source, configuration or infrastructure**? → Implementation

Constraint is asked before Requirement on purpose. A Constraint is also a verifiable obligation, so a test that asks for Requirement first swallows it.

A regulation is usually both, and the split is clean: the document is a Source, the obligation read out of it is a Constraint, and the Constraint declares `informed-by` the Source.

#### Worked example

```text
INTENT       Comply with applicable KYC regulation.
                 ↓ motivates
OUTCOME      Customer identity is verified to the required assurance
             level before regulated operations are enabled.
                 ↓ requires
CAPABILITY   SPEC-0017-CAP-0001: Verify customer identity.
                 ↓ specified by
REQUIREMENT  SPEC-0017-REQ-0003: The system must perform liveness
             verification.
                 ↓ satisfied by
DECISION     SPEC-0017-DEC-0001: Liveness verification uses provider X.
             Rejected: provider Y, on latency.
             ◄── respects ── SPEC-0017-CON-0001: biometric data never
                             leaves the region it was captured in.
                 ↓ executed through
WORK ITEM    SPEC-0017-WI-0004: Implement the provider X adapter in
             identity-service.
                 ↓ implemented by
CODE         commit abc123, ProviderXIdentityAdapter
                 ↓ evidenced by
EVIDENCE     Integration suite green; deploy 2026-03-12 carries abc123;
             production verification succeeds.
```

The Requirement survives if provider X is replaced. The Decision does not. That asymmetry is the whole point of separating them.

The chain runs downward. The Constraint enters sideways, because nothing in this work produced it and nothing in this work may break it.

### 4.2 The two spaces

The Canon is rooted at the **HQ**: the repository an agent enters the system through. Its root `charter.md` constitutes its authority. Once Canon materializes, its generated `index.md` resolves the tree and its `specs/` and `sources/` collections hold root Canon. Everything canonical hangs off it.

|                 | Discovery Space   | Canon                                |
| --------------- | ----------------- | ------------------------------------ |
| Optimizes for   | Exploration       | Shared truth                         |
| Structure       | None imposed      | Enforced                             |
| Authority       | None              | Authoritative in its declared domain |
| Version control | Typically ignored | Always tracked                       |
| Consistency     | Not required      | Required                             |

> **Mess is allowed before promotion. Inconsistency is not allowed after promotion.**

The framework deliberately does not prescribe how anyone organizes their Discovery Space. Turning divergent thinking into bureaucracy is a known failure mode, and the framework treats avoiding it as a requirement.

### 4.3 The three stages

```text
              DISCOVERY                    DESIGN                        BUILD

                 ╱╲                          ╱╲
                ╱  ╲                        ╱  ╲                    Implement
   Inputs ────►╱    ╲─── Specification ────╱    ╲─── Decisions ───►  ●──►●──►●
               ╲    ╱                      ╲    ╱    Work Package         │
                ╲  ╱                        ╲  ╱     Work Items           │
                 ╲╱                          ╲╱                           ▼
                  ▲                           ▲              Verified affected capabilities
                  │                           │              operating in production
                  │                           │                          │
                  └─────────────┬─────────────┘                          │
                                │                                        │
                       Observe | Measure | Learn ◄───────────────────────┘
```

**Discovery and Design are diamonds.** Each diverges and then converges, which is how work in the domain of ideas, knowledge and documents proceeds.

**Build is a chain.** A diamond opens a space and then closes it. Build never opens one: divergence inside Build is Design that was not declared. The chain also states that the steps are ordered.

**The loop returns to both diamonds.** Runtime evidence does not only reframe the problem. It also invalidates solution decisions already taken. After observing, measuring and learning, you either reframe at HQ or you found a defect in a Decision.

| Stage         | Consumes                                                                                                 | Produces                                                                                                      |
| ------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Discovery** | Any signal: interviews, analytics, regulation, tickets, market data, runtime observation, prior failures | One baselined **Specification**                                                                               |
| **Design**    | A baselined Specification                                                                                | Zero or more **Decisions** and, when implementation must change, one **Work Package** with its **Work Items** |
| **Build**     | A Work Package                                                                                           | **Affected capabilities implemented and externally verified in production**                                   |

Build's output is deliberately not "merged code" or "successful deployment". Those are outputs. The required result is evidence that the intended behavior is available in the runtime environment.

### 4.4 Scope, and where an artifact lives

A **scope** models conceptual ownership. It is a node of the tree hanging off the HQ, and it nests as deep as ownership requires.

```text
acme-hq
├── charter.md                   constitutes the HQ
├── index.md                     generated when Canon materializes
├── discovery/                  ignored, non-canonical
├── specs/                       Specifications owned by the HQ
│   └── SPEC-0001/
│       └── SPEC-0001.md
├── sources/                     Sources curated by the HQ
│   └── SOURCE-0001/
│       └── SOURCE-0001.md
├── identity/                    child Scope because charter.md exists
│   ├── charter.md
│   ├── index.md
│   ├── discovery/
│   ├── specs/
│   │   └── SPEC-0017/
│   │       └── SPEC-0017.md
│   └── sources/
└── payments/                    child Scope
    ├── charter.md
    ├── index.md
    ├── discovery/
    ├── specs/
    ├── sources/
    └── settlement/              nested Scope
        ├── charter.md
        ├── index.md
        ├── discovery/
        ├── specs/
        └── sources/
```

_Product_ is not a term of this framework. A product is a scope like any other, named by whoever owns it. The framework already has one word for a node that owns conceptual truth, and a second word would name a level rather than a role.

#### Constitutional authority

Placement answers **who owns this subject**. The mandatory `charter.md` at that location answers **why that owner has authority to decide it and what falls inside its jurisdiction**.

The **HQ Charter** is the founding record that constitutes the HQ. Every other Scope also carries exactly one `charter.md`. A directory without it is not a Scope, and one jurisdiction never has two concurrent Charters. The Charter states why its containing Scope exists, what it includes and excludes, the authority under which promotion occurs, and how its foundations may be amended.

Charter is not an ordinary Source: a Source is cited evidence or authority outside a consuming decision boundary, while `charter.md` creates the boundary in which that Scope's Canon can exist. It is not a Specification either: a Specification states a result the product must produce, while the Charter legislates who may decide and within what jurisdiction. For that reason Charter is structural metadata outside the eight Canon artifact classes. It has no `CHARTER-NNNN` identity: the containing Scope is its subject, and the HQ evaluation manifest pins its path and digest.

The HQ originates through Genesis: the accepted git revision that first introduces its root Charter into the HQ's authoritative history. Git records the exact content, attribution and time; when repository policy requires a cryptographic commit signature, that signature is part of the same evidence rather than a second constitutional document.

A child Scope does not constitute itself independently: nesting derives its parent and its own Charter defines its jurisdiction. Within the same repository, the accepted git revision that introduces the child Charter under the parent records the delegation. A child Charter may narrow the parent grant but may neither broaden nor contradict it. A portable authorization mechanism is needed only when the child crosses repository boundaries. Scope ancestry still creates no Constraint inheritance; enforceable product obligations remain in Specifications and flow through `based-on`.

The complete structural vocabulary of a Scope is deliberately small:

```text
charter.md    curated constitutional authority
index.md      generated navigation once Canon materializes
discovery/    ignored, non-canonical exploration
specs/        Specification aggregates
sources/      Source aggregates
<child>/      another Scope exactly when <child>/charter.md exists
```

`specs/`, `sources/` and `discovery/` are reserved collections, never Scopes. A directory below `specs/` or `sources/` organizes one Canon aggregate; it does not create jurisdiction. A non-reserved child directory becomes a Scope only through its own accepted `charter.md`.

The founding Charter and every accepted revision remain recoverable through git history. Charter carries no independent revision field: the accepted git revision identifies its exact text.

An amendment is a signed commit accepted on `main` under the repository protections in force for the HQ. It requires no parallel receipt, second Charter or Charter-specific approval path. An amendment may change the means by which the HQ acts, but it must preserve the founding purpose **Change without losing intent**. A revision that changes that purpose is not an amendment: it founds a different HQ through a new Genesis.

Portable authorization for a child in another repository remains an open interoperability contract. The model no longer leaves open whether Charter is an artifact, whether a Scope may omit one or how this Charter may be amended.

The placement rule:

> **A canonical artifact lives at the lowest scope that completely owns its subject.**

This prevents both unnecessary centralization and duplicated canonical truth. A decision governing two services in Identity belongs under `identity/specs/`, not to the root and not to either service. `identity/charter.md` establishes that Identity has authority over that subject.

The same rule decides what lives at the HQ, because the HQ is the root scope. Nothing has to be enumerated: whatever no scope below completely owns belongs there. In this repository, that is the definition of the framework itself.

What sits there has the ordinary shape. An organization-wide product obligation is not a loose statement pinned to the root or hidden in the Charter; it is a Specification under the HQ's `specs/`, whose Intent is organization-wide and which holds the Constraints that Intent justifies. _Operate lawfully in the jurisdictions we sell in_ is an Intent, and data residency is one of its Constraints. The Charter establishes who may own that rule, not the rule's product semantics.

**The HQ is always a repository, and a scope may be one.** Canon lives in repositories because repositories provide the immutable candidate revisions that gates inspect. A split scope may run repository-local validators, but canonical promotion always happens through the HQ promotion gate. That gate evaluates the complete candidate manifest, serializes acceptance, assigns identifiers and records the resulting global index revision. By default a scope is a directory inside the HQ, which is one clone and no coordination. Splitting a scope into its own repository is allowed when something forces it, an access boundary the organization must enforce being the usual reason. It costs a hop against PRINCIPLE-00, so it is a decision, not a default.

**A code repository holds implementation and repository-local supporting material, but no canonical Integral artifacts.** Nothing enters it that does not declare the Work Item it realizes, which is what gate X1 checks.

**A code repository registers into exactly one scope through authoritative structural metadata declared only by that scope.** Placement determines ownership; that Scope's `charter.md` constitutes its authority. The HQ derives repository resolution and global uniqueness from those declarations. Generated indexes, locks and external resolvers may materialize or verify a registration, but never author it. Registration links code to ownership; it does not move ownership into the code repository.

**A Constraint applies through the non-exclusive Specification hierarchy, not through Scope.** A Specification may declare any number of upstream Specification baselines through `based-on`; it inherits the union of their effective Constraints transitively. Capability and Constraint are evaluated together inside the Specification. Every separate Requirement, Decision and Work Item belonging to it is derived as `constrained-by` its own and inherited Constraints; none repeats that fact. When a Constraint changes, those derived edges select every affected branch for reevaluation. Placement in a descendant scope creates no inheritance.

Specifications that share an upstream base inherit its Constraints but do not inherit local Constraints laterally from one another. When a local Constraint comes to govern several such Specifications, it graduates to a common upstream Specification: a new authoritative Constraint there supersedes the local formulation, and each affected Specification reaches it through its own `based-on` graph. The generated index materializes each Specification's effective Constraint set. Gate G8 checks hierarchy, coverage and the structural validity of `narrows`; review decides whether one Constraint is semantically stricter than another.

The union of inherited Constraints must be coherent. A derived Specification may neither ignore nor override an inherited Constraint when two upstream bases disagree. A known contradiction blocks the transition from Design to Build until the Specifications that own those Constraints resolve or supersede them. Detecting semantic conflict is judgment, not a deterministic gate; the unresolved judgment mechanism is recorded in [section 12](#12-open-questions).

#### Canonical collections and aggregates

The Canon owned by one Scope is exactly the union of its `specs/` and `sources/` trees. There is no generic `docs/` collection: a canonical document is either derived from an Intent and belongs to a Specification aggregate, or it records a separately governed authority as a Source aggregate.

A root artifact owns a predictable directory whose name and principal file match its identifier:

```text
specs/SPEC-0017/SPEC-0017.md
sources/SOURCE-0001/SOURCE-0001.md
```

The default Specification aggregate is:

```text
specs/
└── SPEC-0017/
    ├── SPEC-0017.md
    ├── requirements/
    │   └── SPEC-0017-REQ-0003/
    │       └── SPEC-0017-REQ-0003.md
    ├── decisions/
    │   └── SPEC-0017-DEC-0001/
    │       └── SPEC-0017-DEC-0001.md
    └── work-packages/
        └── SPEC-0017-WP-0001/
            ├── SPEC-0017-WP-0001.md
            └── work-items/
                └── SPEC-0017-WI-0004/
                    └── SPEC-0017-WI-0004.md
```

Capabilities and Constraints remain inline in `SPEC-0017.md` until PRINCIPLE-00 requires one to split. A split element receives the same aggregate shape under `capabilities/` or `constraints/` without changing its identifier. Work Item placement under a Work Package is the default physical layout; `part-of` remains the graph authority in the current thirteen-relation contract, and a gate checks that placement agrees with it. Whether placement should eventually make `part-of` derived remains open.

A Source aggregate is independent of every Specification:

```text
sources/
├── SOURCE-0001/
│   └── SOURCE-0001.md
└── SOURCE-0017/
    └── SOURCE-0017.md
```

The Source lives in `sources/` of the lowest Scope that completely owns the curated extract. Its underlying resource remains governed outside the consuming decision boundary. If broader use moves curation to an ancestor Scope, the complete `SOURCE-NNNN/` directory moves while its identifier and principal filename remain unchanged.

When a Scope first accepts Canon, the same promotion materializes its generated `index.md`. From then on the index records its Charter digest, local Specifications, local Sources and immediate child Scopes. It does not flatten every descendant into one file; agents descend through the index tree within PRINCIPLE-00. An empty constituted Scope has no persisted index because git does not represent its empty Canon collections.

Scope is a property of placement. It appears in neither the identifier nor the frontmatter: reorganizations move artifacts between scopes, an identifier that changes is not an identifier, and a declared scope is a second copy of something the path already says.

### 4.5 The Canon and the repositories

Two bodies of work, and one seam between them.

```text
  CANON                      THE SEAM                     CODE
  specs/ and sources/        three links, nothing else    code repositories
  inside each Scope
  ─────────────────────────  ─────────────────────────    ───────────────────────
  Work Item   ───────────►   targets                 ──►  code repository
  Work Item   ◄───────────   Realizes:               ◄──  commit
  Work Item   ◄───────────   validation receipt     ◄──  integrated commit
```

`targets` is declared once, in the Canon. `Realizes:` is written by the commit. After that immutable commit is judged, a validation authority issues a receipt that names its exact SHA and Work Item. The HQ evaluation manifest consumes the receipt without changing the subject it attests. [Section 9](#9-the-execution-model) defines the last two.

The Canon holds no code and a code repository holds no Canon. The Work Item is the only artifact either side names, and the Work Package coordinates Work Items without touching code itself.

Discovery and Design produce nothing in the code world. They may read it, and often must: choosing between extending a service and writing a new one requires knowing what already exists. Reading code is not an operation on artifacts.

That reading is also why the Decision class exists. If every Design had to re-derive the standing commitments from source, PRINCIPLE-00 would fail on the first attempt. A Decision records what was committed to and what was rejected, so the next Design reads the Canon instead of the repository.

**The framework governs the Canon completely, and the code world at one point.** That point is the commit, which declares the Work Item it realizes. Everything else about how code is written belongs to the code repository: language, architecture, test strategy, packaging, deployment and branching model.

## 5. Definitions

Terms coined or given a specific meaning by Integral. Where a term is borrowed, its origin is named. Anything not defined here carries its ordinary industry meaning.

### 5.1 Process terms

**Integral**
An operating system for agentic product development: the framework defined by this document.

**HQ**
The single repository an agent enters the system through. Its root `charter.md` constitutes the authority under which its Canon may exist. Once Canon materializes, its root `index.md` resolves every artifact identifier. It is also the root Scope, so its `specs/` and `sources/` hold whatever Canon no child Scope completely owns. An agent never enters by opening an isolated repository with no product context.

**Charter**
The mandatory `charter.md` at the root of an HQ or Scope. It states why its containing jurisdiction exists, what it includes and excludes, the authority under which it may promote Canon and how its foundations may change. It is structural authority, not a Canon artifact, carries no `CHARTER-NNNN` identity and is never inherited in place of a local Charter. Exactly one exists per HQ or Scope; a directory without one is not a Scope.

**Discovery Space**
The non-canonical, exploratory, personal half of the system. Heterogeneous by design and typically not version-controlled. A Scope may expose it through a gitignored `discovery/` directory, but Integral prescribes nothing below that boundary. It holds raw signal and the convergence passes over it.

**Canon**
The curated, shared, version-controlled body of artifacts that are authoritative within their declared domain under the containing Scope's Charter. Inside a Scope it is exactly the union of `specs/` and `sources/`. Only promoted knowledge enters it; `charter.md`, `index.md` and `discovery/` are not Canon artifacts.

**Promotion**
The HQ-serialized guarded event by which an artifact crosses from Discovery Space into the Canon, or by which a Specification or Source advances to a new baseline. Candidate content may live in the HQ or a split scope repository, but only the HQ promotion gate accepts it into the global Canon. Promotion is a consistency boundary, not a workflow status and not a file move. It assigns the canonical identifier and records the accepted evaluation manifest.

**Gate**
A deterministic, computable check over declared inputs that blocks a promotion when a declared condition fails. Given the same validator version and the same inputs, it always produces the same result. A check requiring judgment is a review, not a gate.

**Review**
A judgment about whether something is right, recorded as an immutable attestation so that a gate can read that it happened. A review is not deterministic and never becomes a gate. At the execution seam, its receipt names the exact integrated commit SHA, Work Item, accepted or rejected verdict, authority, actor and time. The receipt lives outside the subject it attests and is anchored by the HQ evaluation manifest, avoiding a self-referential commit while remaining independent of a forge.

**Baseline**
The current agreed revision of a Specification or Source, expressed as an explicit semantic integer. The integer is not a git commit: raising it is a deliberate act, so a typo does not create a revision. The generated baseline ledger binds each `id@baseline` to its HQ promotion revision, content digest and resolved upstream baseline set, so the same baseline can never name different content. Downstream artifacts declare which baseline they were derived from.

**Digital Thread**
The traversable chain of provenance from intent to verified runtime capability. Borrowed from product lifecycle management in manufacturing, where it names the same idea applied to physical goods.

### 5.2 Knowledge terms

**Intent**
The reason a change should exist. It originates outside the implementation and survives it. Test: _if every current implementation disappeared tomorrow, would this reason still hold?_

**Outcome**
The observable state that exists if the Intent has been addressed. A state, not an activity, and not an output. Stated in the positive, and measurable, because a state you cannot check is a state nobody can disagree with.

|             | Example                                                                                             | Why the first two are not the Outcome                                   |
| ----------- | --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Activity    | Integrate the identity provider                                                                     | It names work. The work can finish with nothing about the world changed |
| Output      | The KYC service runs in production                                                                  | It names a thing produced. A running service has verified nobody        |
| **Outcome** | **Every customer reaching a regulated operation has been verified to the required assurance level** | A state, observable, and either true or false today                     |

**Capability**
Something the product must be able to do in order to produce the Outcome. Formulation test: \_the system is capable of \_\_\_\_.

Integral prefers Capability over **Feature**, which is ambiguous across two orders of magnitude: the same word covers _dark mode_ and _authentication platform_, and no rule can be written that applies sensibly to both.
**Constraint**
Something already true that this work cannot violate: a regulation, a standing commitment, a limit the organization accepted. The work does not produce it and cannot negotiate it away. It belongs to one Specification, is evaluated there with its Capabilities, and constrains every separate Requirement, Decision and Work Item reached through the non-exclusive Specification hierarchy by derived `constrained-by` edges. Another Constraint may explicitly tighten it by declaring `narrows`; transitive `based-on`, never Scope placement, determines inheritance. Example: _biometric data never leaves the region it was captured in_.

A Constraint always serves an Intent, and the test is worth stating: **if you cannot name the Intent a Constraint serves, you do not have a Constraint.** You have a preference, which belongs in a Decision, or an observation, which belongs in a Source. _The payment provider caps 100 requests per second_ is an observation about the world. _Our checkout stays under that cap_ is the Constraint, and it serves the Intent that checkout works.

**Source**
A separately governed authority or body of evidence plus what this framework extracted from it: a regulation, an internal policy owned in GRC, a paper, a vendor benchmark or an incident report. The relevant boundary is the consuming work's decision authority, not the organization's perimeter. The artifact is not the underlying source. It is the citation and the extract, so it still answers _what did we read, who governs it, and what did we take from it_ on the day the URL dies. Artifacts cite it with `informed-by`.

**Requirement**
A condition, behavior or property that must hold for a Capability to be correctly fulfilled. Precise, verifiable, and free of solution choices. Where a Constraint is already true, a Requirement is what this work must make true.

**Decision**
A durable solution commitment that constrains subsequent work, carrying the alternatives it rejected and the reason each lost. Local or readily reversible implementation choices are not Decisions. Example: _session state lives in the signed token; a server-side session store was rejected because the deployment target has no shared cache_.

A Decision is authoritative only for the commitments it states. A difference between Canon and implementation is therefore not automatically a contradiction: deciding whether the implementation violates a stated commitment requires judgment. Deterministic gates cannot establish semantic agreement. PRINCIPLE-12 governs what happens after that judgment identifies a disagreement: the implementation or the Canon must be reconciled before promotion, because known inconsistency is not an acceptable steady state.

**Work Item**
The smallest planned unit of change that is independently implementable and independently verifiable. It belongs to exactly one Work Package under one Specification, implements Requirements of that Specification only, and must target exactly one code repository.

**Work Package**
The orchestrator for the Work Items required by one Specification baseline. Through that Work Item set it implements one or more affected Capabilities; it does not itself perform verification. A baseline that requires no implementation change produces no Work Package. A Work Package may span repositories; its Work Items must not.

> **Work Item is the unit of implementation. Work Package is the unit of coordination.**

**Implementation**
The concrete technical form of the work: source, configuration, migrations, infrastructure, tests. Implementation is code. It is referenced by the Canon, never held in it.

### 5.3 Structural terms

**Artifact**
A unit of curated knowledge with a stable identity, a declared type, and typed relations to other artifacts.

**Scope**
A jurisdictional node of conceptual ownership in the tree hanging off the HQ, constituted by exactly one `charter.md` at its root. Scopes nest. A Scope is a directory inside the HQ by default, and may be a repository of its own when an operational boundary requires it. A child belongs to its parent by directory nesting. Canon ownership is derived from the nearest containing Scope and its reserved `specs/` or `sources/` collection, never declared in artifact frontmatter.

**Code repository**
A version-control boundary holding implementation and repository-local supporting material. It registers into exactly one scope, it never holds a canonical Integral artifact, and a Work Item names it in `targets`. Nothing enters it that does not declare the Work Item it realizes. The HQ is a repository too, and so is a scope that has been split out; _code repository_ names the kind that carries no Canon.

**Composed identifier**
An identifier built from its origin: `SPEC-0017-REQ-0003`. It states **origin, not ownership**. Origin is immutable, because the past does not change; ownership is not, because a Decision written for one Specification may end up governing three.

**Index**
The generated `index.md` at the root of every HQ and Scope that holds materialized Canon. It maps identifier to location, class, Scope and declared `status`, records the containing Charter digest, and lists local Specifications, local Sources and immediate child Scopes. It is derived by scanning the tree and never maintained by hand. The first ordinary promotion materializes it; later gates regenerate it deterministically and reject a persisted index that differs from the generated result. The index also materializes each Specification's derived constraint coverage and the repositories registered into each Scope.

**Authority**
The single authority that owns a given fact or grants a decision boundary. Canonical documents reference authoritative facts rather than copying them, and never replace the system that holds them. The API contract's authority is the OpenAPI document; the deployment state's authority is the deployment system; the Requirement's authority is the Specification; the Scope's right to govern that Requirement comes from its own `charter.md` and the parent acceptance chain.

**Derivation, Reference, Coordination, Lifecycle**
The four genera of relation. Only Derivation propagates staleness; the rest order execution, cite context, or change state.

## 6. The artifact model

### 6.1 Eight classes

The Canon holds exactly eight classes. The filter that produces this list: _is this curated knowledge, or is it divergence, or is it an external authority?_

| Class             | Holds                                                                             | Identifier           |
| ----------------- | --------------------------------------------------------------------------------- | -------------------- |
| **Specification** | Intent, Outcome, and the Capabilities and Constraints it owns                     | `SPEC-0017`          |
| **Capability**    | One thing the product must be able to do                                          | `SPEC-0017-CAP-0001` |
| **Constraint**    | One thing already true that the work cannot violate                               | `SPEC-0017-CON-0001` |
| **Requirement**   | One condition that must hold                                                      | `SPEC-0017-REQ-0003` |
| **Decision**      | One solution commitment and its rejected alternatives                             | `SPEC-0017-DEC-0001` |
| **Work Package**  | Coordination of the work for one Specification baseline                           | `SPEC-0017-WP-0001`  |
| **Work Item**     | One executable, independently verifiable change                                   | `SPEC-0017-WI-0004`  |
| **Source**        | One separately governed authority or evidence body and what was extracted from it | `SOURCE-0001`        |

Intent and Outcome appear once per Specification and carry no identifier. Nothing points at them one by one, and the Specification's own identifier already reaches them. Capability and Constraint are numbered because other artifacts point at them, and a thing that is pointed at needs a name.

**Specification and Source are the two root identifier classes.** Every other class is composed against the Specification that originated it. Source is the only root class whose semantic authority is not held inside the decision boundary that consumes it. It may still be governed elsewhere inside the same organization. Charter is not a third root class: it is structural authority for the directory that contains both root-class collections.

|                                                       | Justified by           |
| ----------------------------------------------------- | ---------------------- |
| Everything decided inside a Specification's authority | An Intent above it     |
| A Source governed outside that decision boundary      | The edges that cite it |

A Source is not decided inside the consuming boundary, so no Intent in that boundary stands over it. The underlying authority may be an external regulation or an internal policy decided and maintained by another body. The Source artifact exists while something cites it and is dead weight the day nothing does. One policy or paper may inform work across several Specifications, so composing it against one would state an origin that is not true.

Every class other than Specification and Source composes, Constraint included. A Constraint with no Intent above it has no reason to exist, and §5.2 makes that a test rather than a style note.

Six things that look like current Canon artifact classes and are not:

| Not a class      | Where it actually lives                                                      |
| ---------------- | ---------------------------------------------------------------------------- |
| Test             | Code. The criterion is the Requirement's `verification` field                |
| Runtime Evidence | External authority. Receipts feed the Work Package's derived `verified` view |
| Implementation   | Code. Linked by the Work Item's derived `realized-by`                        |
| Scope            | Placement, and placement is derived                                          |
| Index            | A generated file, rebuilt from the tree rather than curated                  |
| Charter          | Mandatory structural authority at the Scope root; not part of Canon          |

Nothing is lost. Each becomes a field or a pointer to its authority, which is what PRINCIPLE-07 requires. Promoting them to classes would fill the index with thousands of uncurated nodes that age on their own, which PRINCIPLE-00 forbids.

The index is worth stating outright, because it is derivable, generated and persisted all at once, and PRINCIPLE-08 forbids exactly that combination inside an artifact. It escapes because **a generated file is not an artifact.** It carries `generated`, nothing declares a relation to it, it holds no identifier of its own, and it is rebuilt rather than edited. PRINCIPLE-08 governs what is curated; a generated file is the output the principle asks for, not a case against it.

### 6.2 Cardinality

```text
Specification 1 ─── 1..N  Capability
Specification 1 ─── 0..N  Constraint
Specification 1 ─── 0..N upstream Specification baselines  (through based-on)
Capability    1 ─── 1..N  Requirement
Specification 1 ─── 0..N  Decision
Specification baseline 1 ─── 0..1  Work Package
Work Package  1 ─── 1..N  Work Item        (each WI belongs to exactly one WP)
Work Package  1 ─── 1..N  affected Capability  (derived through WI and Requirement)
Decision      1 ─── 0..N  Work Item        (through prospective follows)
Work Item     1 ─── 1     target code repository
```

At most one Work Package exists for a Specification baseline, and only when reevaluation finds implementation work to perform. A semantic change that the current implementation already satisfies creates no Work Package and does not reopen completed work.

These are coverage cardinalities, not a requirement that the numbers of Requirements, Decisions and Work Items be equal. A Decision is optional; a Work Item does not need a ceremonial Decision in order to implement a Requirement. Every new or adapted Work Item caused by a Decision declares `follows`, and one Decision may require several such Work Items when implementation crosses repository boundaries. A future retrospective-conformance mechanism may allow a Decision that adopts an already conforming implementation to have no Work Item, but that exception is not active until its portable receipt is defined. A Work Package and all of its Work Items remain within one Specification: `implements`, `follows` and `part-of` never cross that origin. Cross-Specification execution order uses `depends-on` and does not move either Work Item out of its own Work Package. Reevaluation places a Capability inside the new Work Package when one or more of its Requirements require new or adapted Work Items; a Capability whose current realized Work Items remain valid stays outside that Work Package. At completion, the set of Work Item identities planned through `part-of` must be exactly equal to the set of realized Work Item identities. The equality is over Work Items, not over commits or implementation fragments.

A Source has no composition cardinality here at all: it is cited by any number of artifacts and belongs to no Specification. Its curated artifact aggregate is owned by the Scope containing its `sources/` directory; the underlying resource remains under its separately governed authority.

### 6.3 The frontmatter contract

Every artifact has `id`, `type` and `status`. A file-backed artifact declares all three explicitly. An inline Capability or Constraint declares its own stable `id`, derives `type` from the collection that contains it (`capabilities` or `constraints`), and inherits the lifecycle `status` of its containing Specification. Each class adds its own fields.

The principal file of each root aggregate repeats its identifier in the filename: `specs/SPEC-0017/SPEC-0017.md` and `sources/SOURCE-0001/SOURCE-0001.md`. Composed file-backed artifacts follow the same directory-and-principal-file convention inside their Specification aggregate. Paths make the corpus predictable; graph relations still use identifiers.

```yaml
# Specification
id: SPEC-0017
type: specification
baseline: 3
status: stable
capabilities:
  - id: SPEC-0017-CAP-0001
    title: Verify customer identity
constraints:
  - id: SPEC-0017-CON-0001
    title: Biometric data never leaves the region it was captured in
```

Required: Intent, Outcome, and at least one Capability. A Specification declares no downward relation. Descendants declare provenance upward, so adding a Decision, Work Package or Work Item never edits or advances the Specification. Capability, Constraint and Requirement are different: together with Intent and Outcome they are the content the Specification baseline names, so changing any of them advances that baseline.

**Granularity is placement, not class.** A Capability or a Constraint is indexed by its identifier whether it sits inline in its Specification, as above, or in a file of its own. The index resolves the identifier to a location, so splitting an inline element into a file changes the location and never the identifier. That is PRINCIPLE-04 doing its work. Split when PRINCIPLE-00 says the file stopped being reachable, not before.

```yaml
# Source
id: SOURCE-0001
type: source
baseline: 1
status: stable
resource: https://eur-lex.europa.eu/eli/reg/2016/679/oj
citation: Regulation (EU) 2016/679, Article 44
extract: Personal data may leave the region only under an adequacy
  decision or an approved safeguard.
retrieved: 2026-02-04
```

```yaml
# Requirement
id: SPEC-0017-REQ-0003
type: requirement
status: stable
specifies: [SPEC-0017-CAP-0001]
verification: Liveness check rejects a static photograph and accepts a live capture.
```

```yaml
# Decision
id: SPEC-0017-DEC-0001
type: decision
status: stable
based-on: [SPEC-0017@3]
satisfies: [SPEC-0017-REQ-0003]
respects: [SPEC-0017-CON-0001]
rejected:
  - provider Y: p99 latency 4x the budget
  - in-house model: no compliance certification path
```

`SPEC-0017@3` reads _Specification 017 at baseline 3_. The part before the `@` never changes; the part after it records which revision this Decision was written against. The generated baseline ledger binds that pair to the HQ promotion revision, a digest of the complete Specification content and its exact resolved upstream baseline set.

That second half makes selection for reevaluation computable. A relation that said only _this points at SPEC-0017_ would be true forever and would therefore report nothing. Because the Decision names revision 3, gate G7 compares 3 against the current baseline and selects the Decision for reevaluation when the Specification reaches 4. The `@` is the join between an artifact and the version of the thing it was derived from. A separate reevaluation judgment decides whether the descendant remains valid; G7 checks and consumes the resulting attestation but never makes that semantic judgment itself.

It appears only inside relations, never in an identifier and never in a filename.

`rejected` is what stops an agent reproposing a discarded option six months later. Agents repropose the obvious choice, and the obvious choice is usually the one already ruled out.

```yaml
# Work Package
id: SPEC-0017-WP-0001
type: work-package
status: stable
based-on: [SPEC-0017@3]
verification:
  - requirement: SPEC-0017-REQ-0003
    check: The liveness endpoint rejects a static photograph
    method: repo:identity-service@commit-BBB#scripts/verify/liveness.sh
    authority: runtime:production-verification
    environment: production
```

The Work Package stores **verification conditions**, not their eventual results. `check` says what must be true, the versioned `method` says how to find out again, and `authority` and `environment` say who must attest it and where. Build does not rewrite the stable Work Package. Instead, the authority later issues an immutable receipt containing the Requirement, exact deployed subject, environment, verdict, observation time, actor and method version. The HQ evaluation manifest consumes those receipts and the generated index derives the Work Package's `verified` view. A convenience run URL may accompany a receipt and is understood to rot.

Who runs the check is configuration. Naming a continuous integration system here would prescribe a stack, the same way naming a git flow would.

```yaml
# Work Item
id: SPEC-0017-WI-0004
type: work-item
status: stable
based-on: [SPEC-0017@3]
part-of: [SPEC-0017-WP-0001]
implements: [SPEC-0017-REQ-0003]
follows: [SPEC-0017-DEC-0001]
targets: repo:identity-service
depends-on: [SPEC-0017-WI-0002]
```

`realized-by` is absent on purpose. It is derived from commit trailers, never written. See [section 9](#9-the-execution-model).

#### The fields

Half the vocabulary comes from OKF and keeps OKF's meaning. The other half is this framework's. Naming the source of each field costs one column and settles every later argument about whether a field may be changed here.

| Field                         | From     | Means here                                                                                                                                                                                        | Required on                         |
| ----------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| `id`                          | Integral | The canonical identifier. Assigned at promotion, never reused                                                                                                                                     | every class                         |
| `type`                        | OKF      | The class, lowercase and hyphenated: `work-item`                                                                                                                                                  | every class                         |
| `status`                      | OKF      | The lifecycle state. See [section 8.4](#84-baselines-and-staleness)                                                                                                                               | every class                         |
| `baseline`                    | Integral | For a Specification, the agreed revision of Intent, Outcome, Capability, Constraint and Requirement content plus its resolved `based-on` baseline set; for a Source, its agreed semantic revision | Specification, Source               |
| `sources`                     | OKF      | What in Discovery Space this was distilled from                                                                                                                                                   | Specification, Decision             |
| `capabilities`, `constraints` | Integral | The inline elements this Specification owns, each with its identifier                                                                                                                             | Specification, when they are inline |
| `specifies`                   | Integral | The Capability this Requirement bounds                                                                                                                                                            | Requirement                         |
| `citation`                    | Integral | What was read, named well enough to find again without the URL                                                                                                                                    | Source                              |
| `extract`                     | Integral | What this framework took from it, in this framework's words                                                                                                                                       | Source                              |
| `retrieved`                   | Integral | The date the extract was read out of the reference                                                                                                                                                | Source                              |
| `verification`                | Integral | The check that decides whether the Requirement holds                                                                                                                                              | Requirement                         |
| `rejected`                    | Integral | The alternatives that lost, and why each lost                                                                                                                                                     | Decision                            |
| `targets`                     | Integral | The one code repository the Work Item changes                                                                                                                                                     | Work Item                           |
| `verification`                | Integral | Conditions binding an affected Requirement and reproducible method to the authority and environment that must verify it                                                                           | Work Package                        |
| `verified`                    | OKF      | Generated view derived from immutable verification receipts; never written into the Work Package artifact                                                                                         | generated Work Package view         |
| `generated`                   | OKF      | Marks a file a generator wrote, so nothing edits it by hand                                                                                                                                       | any generated file                  |
| `stale_after`                 | OKF      | An expiry the index reads without traversing the graph                                                                                                                                            | optional, any class                 |
| `tags`                        | OKF      | Free labels. Carried and never read by a gate                                                                                                                                                     | optional, any class                 |
| `resource`                    | OKF      | A pointer to the thing the artifact describes                                                                                                                                                     | optional, any class                 |

`informed-by` is optional on every class, and it is meant to stay that way. Most artifacts need no authority outside their own decision boundary, and a required citation field teaches people to invent one to pass the gate. Write a Source when you would otherwise cite a separately governed internal or external authority and expect somebody to act if it changes. Do not write one for something you merely read.

`sources` and `informed-by` are not the same mechanism and do not compete. `sources` points back into Discovery Space, which is untracked, and records what an artifact was distilled from inside its own formation process. `informed-by` points at a Source, which is canonical, and records a separately governed authority the artifact rests on.

The `sources` frontmatter field is also unrelated to the reserved `sources/` directory. The field records Discovery provenance; the directory contains canonical `SOURCE-NNNN` aggregates. The shared spelling comes from OKF for the field and ordinary collection naming for the directory, so validators distinguish them by structural position rather than inventing a synonym.

Relations are frontmatter too, and [section 7.4](#74-the-relation-vocabulary) is their contract. An inline Capability or Constraint carries no frontmatter block of its own: its entry in the Specification's list supplies its own `id`, while collection placement derives `type` and the containing Specification supplies `status`. It gains an explicit frontmatter block without changing identity on the day it becomes a file.

OKF's `index.md` convention is adopted whole. The index is generated, so `generated` is set on every one of them.

## 7. Identity and the graph

### 7.1 Three questions, three answers

A file path answers three questions at once, which is why paths make poor identifiers. Integral separates them.

| Question                     | Answered by              | Lives in    | Stability          |
| ---------------------------- | ------------------------ | ----------- | ------------------ |
| What is this?                | `id`                     | Frontmatter | Permanent          |
| What relates to it, and how? | Typed relations, by `id` | Frontmatter | Follows the graph  |
| Where is it now?             | Generated index          | Derived     | Volatile by design |

**The graph never uses paths.** Prose links do, because a markdown link is what a human clicks. Move a file and the graph does not notice; the prose link breaks, a gate reports it, a tool rewrites it. The layer that degrades is the one that can afford to.

**Identity is cheaper than the path.** With paths as identifiers, asking _who implements REQ-0003_ means scanning the tree, and the cost grows with the corpus. With a stable identifier and an index it costs one small file read. The index is also the map an agent loads once to see everything available before opening anything.

### 7.2 Identifier rules

| Rule                          | Reason                                                                                                                                                                                                           |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Composed against the origin   | The origin is immutable, so the identifier cannot become a lie                                                                                                                                                   |
| Sequential with a type prefix | An agent writes these into frontmatter and verifies them by reading                                                                                                                                              |
| Assigned at promotion         | Holding a canonical identifier is what being canonical means. The HQ promotion gate serializes assignment across every Canon repository, so parallel candidate branches cannot allocate independently or collide |
| Never reused                  | A commit recording `Realizes: SPEC-0017-WI-0004` must resolve to the same Work Item forever                                                                                                                      |
| Never contains the scope      | Reorganization moves artifacts between scopes                                                                                                                                                                    |
| Never contains the baseline   | The baseline is state, the identifier is origin                                                                                                                                                                  |

**The frontmatter does not carry the Scope either.** For an artifact under `specs/` or `sources/`, the owner is the nearest ancestor directory carrying `charter.md`. The path already states it and the index already derives it. A field that repeats what is derivable is a field that can disagree with it, and on the day the two disagree there is no rule saying which one wins.

The one case a `scope:` field would win is an artifact filed in one place and belonging to another. That is exactly the state the placement rule exists to forbid, so winning that case is not a feature.

Moving a canonical artifact between Scopes is therefore a move of its complete aggregate directory between the corresponding `specs/` or `sources/` collections, and it needs a Decision recording why. A gate reads the index before and after, and rejects a move that no Decision accounts for.

Two consequences worth stating outright:

**Semantic deletion does not exist for an artifact in the ordinary lifecycle.** A promoted artifact is deprecated rather than removed, and its identifier remains resolvable for downstream references. A gate rejects ordinary removal, so the rule does not depend on anyone remembering it. Exceptional physical removal required by security or law preserves a resolvable tombstone; the purge mechanism is implementation-defined.

**A retired Specification's identifier stays a valid prefix** for artifacts that are still live. That follows from never reusing identifiers, and it is what makes composed identifiers safe.

`SPEC-0017` in full is `<hq>:SPEC-0017`; the prefix is omitted when it resolves against the current HQ. Nothing writes it and nothing parses it today. Reserving the grammar costs one line and is what keeps every existing identifier valid on the day two HQs have to coexist.

### 7.3 Which way edges are declared

> **Provenance is declared upward. Navigation is derived downward. Composition is never declared at all.**

Every dependency edge is declared by the artifact whose meaning or execution depends on the target. It owns the dependency claim. The creation order of artifact identities is irrelevant, but the revision that introduces the edge may be promoted only against a target revision that already exists. An existing artifact may therefore acquire a dependency on a newer upstream artifact during reevaluation, while no relation may manufacture retroactive provenance.

This is not a stylistic choice. If a target had to list the artifacts that depend on it, writing a Decision would edit the Specification, which raises its baseline and needlessly sends every downstream artifact through reevaluation. **A baselined artifact would be reopened by the act of something being built from it.**

Downward edges are computed by inverting the declared ones. That inverted map is what an agent navigates, so declaring upward costs downward navigation nothing.

Composition is not declared because the composed identifier already states it. `SPEC-0017-REQ-0003` says the Specification contains it, with no field that can disagree with the identifier.

### 7.4 The relation vocabulary

| Relation         | Genus        | Declared by                     | Points at                                                         | If the target changes, the source...                                                                        |
| ---------------- | ------------ | ------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `based-on`       | Derivation   | Specification, Decision, WP, WI | `SPEC-NNNN@B`; from a Specification, any number of upstream bases | is reevaluated; goes stale only if it no longer holds                                                       |
| `specifies`      | Derivation   | Requirement                     | Capability                                                        | is reevaluated; goes stale only if it no longer holds                                                       |
| `respects`       | Derivation   | Decision                        | Constraint                                                        | is reevaluated; goes stale only if it no longer holds                                                       |
| `narrows`        | Derivation   | Constraint                      | Constraint                                                        | is reevaluated; goes stale only if it no longer holds                                                       |
| `informed-by`    | Derivation   | any                             | Source                                                            | is reevaluated; goes stale only if it no longer holds                                                       |
| `satisfies`      | Derivation   | Decision                        | Requirement                                                       | is reevaluated; goes stale only if it no longer holds                                                       |
| `implements`     | Derivation   | Work Item                       | Requirement of the same Specification                             | is reevaluated; goes stale only if it no longer holds                                                       |
| `follows`        | Derivation   | Work Item                       | an existing Decision of the same Specification                    | is prospective provenance; the Work Item is reevaluated and goes stale only if the Decision no longer holds |
| `references`     | Reference    | any                             | any                                                               | nothing                                                                                                     |
| `depends-on`     | Coordination | Specification, Work Item        | Specification@B from Specification; Work Item from Work Item      | nothing; it orders promotion or execution                                                                   |
| `conflicts-with` | Coordination | Work Item                       | Work Item                                                         | nothing; it feeds the owning agent's schedule                                                               |
| `part-of`        | Coordination | Work Item                       | exactly one Work Package of the same Specification                | nothing                                                                                                     |
| `supersedes`     | Lifecycle    | the new artifact                | the retired one                                                   | nothing; the target is frozen                                                                               |

A relation that points at an artifact carrying its own baseline names the revision directly: `SPEC-0017@3`, `SOURCE-0001@1`. A relation to a composed artifact names its stable identifier. From a Specification, `based-on` names zero or more upstream bases and establishes a non-exclusive Constraint-inheritance hierarchy. A Work Package and Work Item pin only the baseline of the Specification they belong to; a Decision pins every Specification baseline required by its Derivation relations. The gate rejects a downstream artifact whose Derivation targets are not covered by the permitted baseline pins.

Thirteen declarable relations. The governing rule:

> **A relation type exists to answer one question: if the other end changes, what happens to me? Two types with the same answer are one type with two names.**

`contains` and `blocks` are absent by application of that rule. `contains` is stated by the identifier; `blocks` is the inverse of `depends-on`, and declaring both puts one fact in two places.

Everything derived, and the three different places it is derived from:

| Derived by                    | Examples                                                                                                                                                             |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inverting the declared graph  | `contains`, `blocks`, `specified-by`, `respected-by`, `narrowed-by`, `informs`, `satisfied-by`, `implemented-by`, `superseded-by`                                    |
| Shared Specification identity | `constrained-by` from every separate Requirement, Decision and Work Item to each Constraint of that Specification                                                    |
| Reading an external authority | `realized-by` from commit trailers, `validated` from validation receipts, `verified` from runtime verification receipts, deployment state from the deployment system |

**Only the Derivation genus feeds impact analysis.** This is what makes impact analysis useful rather than merely available. Untyped edges return the neighborhood, which grows with the corpus while the real impact does not.

### 7.5 Impact analysis in practice

`SPEC-0017-REQ-0003` changes. Five artifacts touch it:

| Neighbor             | Relation                                            | Reevaluate?              |
| -------------------- | --------------------------------------------------- | ------------------------ |
| `SPEC-0017-DEC-0001` | `satisfies`                                         | **Yes**                  |
| `SPEC-0017-WI-0004`  | `implements`                                        | **Yes**                  |
| `SPEC-0021`          | `references`                                        | No                       |
| `SPEC-0012`          | `depends-on` the Specification, not the Requirement | No                       |
| `SPEC-0017-WI-0009`  | `depends-on` WI-0004                                | No; execution order only |

Two reevaluation candidates out of five neighbors. Deterministic traversal selects those two; their reevaluation attestations then preserve a candidate that remains valid or derive `stale` for one that no longer does. Without typing, all five come back and the agent opens all five to find out which two matter.

## 8. Promotion and gates

### 8.1 What promotion is

Promotion is the only way knowledge enters or advances in the Canon. It is a consistency boundary: crossing it asserts that the Canon is not knowingly inconsistent with what it describes.

Constituting a Scope is the structural event immediately before that rule can apply there. Genesis is the accepted git revision that introduces the HQ's root `charter.md`; an accepted revision introducing a child `charter.md` creates a child Scope under the authority of its parent. A directory cannot receive a Specification or Source promotion before that event. Git does not represent empty collections, so `specs/`, `sources/` and the first generated `index.md` materialize with the Scope's first ordinary promotion rather than pretending to exist at Genesis. A separate portable authorization record is required only when authority crosses repository boundaries; it must never masquerade as ordinary artifact promotion.

```text
Discovery Space              ──distill──►  gates  ──►  Baselined Specification
Specification + exploration  ──distill──►  gates  ──►  Baselined Decisions + build-ready Work Package when implementation must change
Work Package + code          ──verify───►  gates  ──►  Affected capabilities implemented and externally verified in production
```

### 8.2 Promotion gates

Eight groups, all deterministic over declared inputs anchored by one immutable **HQ evaluation manifest**. The manifest names the validator version, a fixed `evaluated-at` instant, the candidate or inherited accepted SHA of every Canon repository, the digest of the previous accepted manifest, the code-repository revisions read for execution state, and the immutable receipts supplied by external authorities. Unchanged Canon repositories inherit through the previous manifest digest but resolve to explicit SHAs in the complete manifest view. The generated index is one input and one output of evaluation; it is not the complete input set. Given the same manifest, neither a moving repository, authority nor clock can change the result.

| Group                        | Checks                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **G1 Referential integrity** | Every referenced identifier and pinned baseline resolves through the baseline ledger. Every composed prefix resolves to an existing origin. Each aggregate directory and principal filename equal the artifact identifier. A revision introducing a dependency names a target present in the accepted manifest it builds on. No duplicates. No reuse after retirement. The HQ serializes identifier assignment and acceptance of the resulting manifest                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **G2 Structure**             | The HQ and every Scope have exactly one root `charter.md`; a directory without the Charter is not a Scope. Every Scope with materialized Canon has exactly one generated `index.md`. Canon artifacts occur only under `specs/` or `sources/`; `discovery/` is excluded. A Specification has Intent, Outcome, at least one Capability and zero or more upstream Specification baselines through `based-on`. A Requirement declares `verification` and exactly one `specifies`. A Work Item declares exactly one `part-of`, exactly one `targets` and at least one `implements`; its physical Work Package aggregate agrees with `part-of`, and its Work Package, Requirements and followed Decisions belong to the same Specification. A Work Package and Work Item pin only that Specification baseline through `based-on`. A Decision pins every Specification baseline required by its Derivation relations                                |
| **G3 Typing**                | Every relation is one of the thirteen. Each target is of a class that relation admits. No derived relation is declared by hand                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **G4 Coverage**              | For every baseline, each Requirement is covered by a current valid realized Work Item of the same Specification or by at least one planned Work Item that `implements` it. Every Decision that causes new or adapted implementation has at least one such Work Item declaring `follows`. The retrospective-conformance exception is not active until its portable receipt is defined; G4 cannot infer conformance from existing code. A Work Package exists only for uncovered work and orchestrates that Work Item set. At completion, every affected Requirement has a passing verification receipt whose authority, environment, exact deployed subject and immutable record resolve through the evaluation manifest. The set of Work Items planned through `part-of` is exactly the set of realized Work Items; each resolves to an accepted integrated implementation carrying its `Realizes:` trailer and a passing validation receipt |
| **G5 Acyclicity**            | Specification `based-on`, `depends-on` and `supersedes` are acyclic. No artifact composes against its own descendant. It reads no other relation, so several Work Items pointing at one Requirement are a fan and never a cycle                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **G6 Lifecycle**             | A promoted artifact is never removed, only deprecated. `supersedes: X` requires X to exist and become deprecated in the same promotion. A deprecated artifact accepts no new inbound Derivation relations. An artifact whose scope changed resolves to a Decision recording the move                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **G7 Freshness**             | Raising a baseline deterministically selects every Derivation-linked descendant whose pinned input changed. When an upstream `based-on` baseline changes, accepting the newly resolved hierarchy advances the affected Specification's baseline even if its local content did not change. G7 never decides whether a descendant still holds: it requires a reevaluation attestation naming the descendant, old and new baseline sets, verdict, authority and time. From those attestations the index derives `current`, `pending-reevaluation` or `stale`; no artifact remains current against an older resolved baseline set without an accepted attestation                                                                                                                                                                                                                                                                                |
| **G8 Constraint coverage**   | Each Specification inherits transitively the union of effective Constraints from every Specification in its `based-on` graph. Capability and Constraint are evaluated together inside their Specification. Every separate Requirement, Decision and Work Item is derived as `constrained-by` every effective Constraint of its Specification, and that coverage appears in the index. Scope ancestry contributes nothing. A declared `narrows` points to an effective Constraint. G8 checks this structure; semantic strictness and compatibility between inherited Constraints are decided by review                                                                                                                                                                                                                                                                                                                                        |

G7 is the only group that also runs on read. A changed declared input can make `pending-reevaluation` appear without a new artifact commit, but the semantic verdict can enter only through a reevaluation attestation.

Three Work Items implementing one Requirement raise a different question, and it is not acyclicity. It is whether they may reach the mainline or become externally available one at a time. [Section 9.1](#91-two-boundaries-not-one) keeps that integration strategy outside the current model.

### 8.3 The boundary of what a gate can do

> **Gates check that the graph is well formed. They never check that it is right.**

Whether an Intent is the right Intent, whether a Decision chose well, whether a Requirement is worth having: no deterministic rule reaches these.

This boundary is deliberate, and it is also the framework's largest open question. With gates alone, an agent can carry an artifact from nothing to promoted with no person involved. Where human judgment enters the model is not yet specified. See [section 12](#12-open-questions).

### 8.4 Baselines and staleness

**A Specification or Source baseline starts at 1 on its first promotion.** Other artifact classes do not carry a baseline of their own. Before promotion, a Specification or Source has no baseline at all, and OKF's `status` carries the lifecycle on its own. One field per concept: `status` says where in an artifact's life it is, while `baseline` identifies an agreed revision. The boundary is exact: a Specification baseline names its Intent, Outcome, Capabilities, Constraints, Requirements and resolved upstream baseline set. A semantic change to any of those requires promotion as baseline `n+1` through the same HQ gate as baseline `n`. Decisions, Work Packages and Work Items are immutable derivatives promoted against that baseline; creating one does not redefine the Specification, and changing a stable one requires a new or superseding artifact. For a Source, the baseline includes only its own semantic content.

The baseline ledger is generated from HQ promotion history. For each `id@baseline` it records the accepted HQ manifest revision, a digest of the complete content named by that baseline, and the resolved upstream set. A gate rejects content whose digest changed without a baseline increment and rejects reuse of an existing integer for another digest. The semantic integer remains the human-facing revision; the ledger makes its referent immutable.

```text
SPEC-0017
  status: draft        no baseline yet
  promotion            baseline: 1
  status: stable       baseline: 2, 3, 4 as it iterates
  status: deprecated   the baseline stops moving

SPEC-0017-DEC-0001
  based-on: [SPEC-0017@3]
```

`status` takes three values and no more. **`proposed` is not among them.** It presumes two actors and a turn to approve, which is a ceremony between people rather than a state of the artifact. Here whoever thinks it builds it, so nothing sits waiting for a second party to look.

That removal sharpens a question rather than answering it. With no proposing and no approving in the lifecycle, an agent carries an artifact from nothing to promoted alone. Where judgment enters is at the seam instead, in the validation receipt of [section 9.6](#96-merge-gates), and whether that verdict may be an agent's is the open question in [section 12](#12-open-questions).

When `SPEC-0017` reaches v4, the Decision is selected for reevaluation automatically. Nobody writes that derived condition; G7 computes it from the declared baseline and the current one. Until a reevaluation attestation exists the index reports `pending-reevaluation`. An accepted attestation derives `current` against v4; a rejected one derives `stale`. These are freshness states in the index, not additional values of artifact `status`.

An accepted upstream baseline change also advances every affected Specification baseline because its resolved Constraint set changed, even when its local text did not. Reevaluation attestations then record whether the existing Work Items remain valid. If they all do, no Work Package is created; uncovered or stale work produces the Work Package for the new effective baseline.

**The identifier says who carries a baseline.**

```text
carries its own                    takes the revision of what it
                                   is composed against
───────────────                    ─────────────────────────────
SPEC-0017        Specification      SPEC-0017-CAP-0001   Capability
SOURCE-0001      Source             SPEC-0017-CON-0001   Constraint
                                   SPEC-0017-REQ-0003   Requirement
                                   SPEC-0017-DEC-0001   Decision
                                   SPEC-0017-WP-0001    Work Package
                                   SPEC-0017-WI-0004    Work Item
```

Read the left column: no prefix, because nothing stands above it. Read the right: every identifier names the artifact it hangs from, and that artifact already has a number. Only two classes need one of their own in the current artifact contract; the Charter contract must decide whether it adds a third.

The same rule runs the other Derivation relations. When `SOURCE-0001` reaches 2, `informed-by: [SOURCE-0001@1]` triggers reevaluation exactly as `based-on: [SPEC-0017@3]` does when the Specification reaches 4. Neither comparison predetermines the result: each selects a candidate and requires a semantic reevaluation attestation.

Iteration and supersession are different operations, and Intent and Outcome are what tell them apart:

| Operation     | When                                                                        | Effect                                                                                     |
| ------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Iterate**   | Intent holds and the Outcome remains a refinement of the same success state | Same identifier, baseline rises                                                            |
| **Supersede** | Intent changes, or the Outcome defines a materially different success state | New identifier; the new artifact declares `supersedes` to the old one, which is deprecated |

An Outcome change therefore does not predetermine the lifecycle operation. Raising a target or refining how the same result is measured normally iterates the Specification. Replacing the state that defines success normally supersedes it. This is a semantic judgment: the fields make the choice explicit and reviewable, while gates verify only that the selected operation is structurally consistent.

Everything else in a Specification may be rewritten from end to end while retaining the same identity, provided the Intent holds and the Outcome still describes the same success state. The baseline rises and the affected graph is reevaluated.

## 9. The execution model

### 9.1 Two boundaries, not one

Merging one Work Item can leave the mainline holding a half-built capability. That is not a conflict between workflows. It is what happens when two boundaries are treated as one, and this model keeps them apart.

| Boundary  | What it is                                                                | Where it lives                                                    |
| --------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **Merge** | An integrable, independently verifiable change                            | Work Item                                                         |
| **Value** | One or more affected Capabilities implemented and evidenced in production | Coordinated by the Work Package; verified by external authorities |

**It cannot be otherwise, because git has no cross-repository branch.** A Work Package coordinates several repositories. No branch contains that. If the value boundary were a branch, the multi-repository model would be impossible, and that model is the reason the Work Package exists.

**The framework prescribes no branching model.** One rule stands in place of the several a prescribed flow would need:

> **Every commit that touches code carries `Realizes:` to a Work Item that exists.**

GitFlow, GitHub flow, trunk-based development and feature branching all satisfy it, because none of them forbids a commit message. Whichever a team already runs keeps running.

Nothing is configured either, and that is the part worth noticing. A rule that holds under every flow needs no field naming which flow is in use, no list of supported ones, and no migration on the day a team switches. There is nothing to declare because there is nothing that varies.

**The framework does not currently define an integration or activation strategy across repositories.** Git provides no atomic transaction across them, and feature flags, release manifests, environment switching and compatibility techniques establish different operational boundaries. Work Items reach their mainlines subject to their declared dependencies and repository gates; the Work Package coordinates the value boundary and is incomplete until all affected Capabilities are implemented and their verification conditions are satisfied by the declared external authorities. Whether partial implementation may be present in mainline or externally available is left open in [section 12](#12-open-questions).

That is the framework's own Outcome applied to itself. A merge is an output. _Verified capability operating in production_ is the result required.

### 9.2 Linking code to a Work Item

The authority is the commit trailer:

```text
Realizes: SPEC-0017-WI-0004
```

`Realizes:` keeps the word because systems modelling already uses it for the link between a specification element and the thing that fulfils it. Prose in this document says _implement_, where the everyday English sense of the word gets in the way.

| Property                | Why it matters                                                                                                                                    |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Not circular            | The trailer is written _as_ the commit is made. A field inside the Work Item cannot work, because writing the hash into the file changes the hash |
| Survives squash         | The squashed message carries it, which matters in a repository with linear history                                                                |
| Plain git               | `git log --format='%(trailers)'` reads it on any forge and on none                                                                                |
| Incrementally indexable | The index records the last commit processed and moves forward                                                                                     |

In a branch-based flow, a branch named `SPEC-0017-WI-0004` may let a `prepare-commit-msg` hook generate the trailer. That is convenience, not authority: not every flow creates such a branch, and under squash merges the branch name survives only if the forge chooses to keep it. The model does not require this convention.

`realized-by` is derived. Nobody writes it.

`Realizes:` establishes the provenance claim between implementation and Work Item; the trailer alone does not establish completion. A Work Item is realized only when the integrated implementation carrying that claim has been accepted against the Work Item and reached the mainline. How an integration pipeline identifies and attests that final subject belongs to implementation. It never requires writing a commit hash or execution state into canonical artifact frontmatter.

### 9.3 Forge independence

| Derived from                    | States available                                                                            |
| ------------------------------- | ------------------------------------------------------------------------------------------- |
| **Core plain git**              | realized (accepted integrated implementation carrying the trailer on the mainline)          |
| **Configured claim convention** | available, claimed, and abandoned when the convention preserves an explicit terminal record |
| **The forge**                   | in progress (draft), in review, approved, rejected                                          |

The core requires only the first row. Claim and forge states are optional enrichment: with a declared repository convention or forge the index knows more, and without one the model still works at lower resolution.

Not an adapter that abstracts everything. A core that needs none, and an adapter that adds detail where one exists.

### 9.4 Work Item state is derived

The required `status` field records the Work Item artifact lifecycle as defined by OKF: `draft`, `stable` or `deprecated`. The execution state below is a separate property derived from git and forge state; it is never written to frontmatter.

| Situation                                                                                             | Derived state | Source               |
| ----------------------------------------------------------------------------------------------------- | ------------- | -------------------- |
| No active claim under the configured convention                                                       | available     | configured flow      |
| Active claim, no accepted integrated implementation yet                                               | claimed       | configured flow      |
| Draft pull request open                                                                               | in progress   | forge                |
| Pull request ready                                                                                    | in review     | forge                |
| Accepted integrated implementation carrying the trailer is present on the mainline                    | realized      | git                  |
| Accepted validation receipt for that exact integrated commit is present in the HQ evaluation manifest | validated     | validation authority |
| Explicit terminal claim record without a realized implementation                                      | abandoned     | configured flow      |

A written execution-state field would be a second source of truth for something git already knows, and it would drift the first time an agent crashed mid-task.

### 9.5 Concurrency between agents

**One agent owns a Work Package.** It holds the whole graph the package depends on, so it is the only party that can decide what runs in parallel, and the dependencies it needs for that decision are already declared. Nothing inside a package is a race, because nothing inside a package is contended.

That collapses most of what a concurrency model would otherwise carry.

**A claim is a record, not a lock.** Under a branch-based convention the branch marks what is in flight so an interrupted run can be found again. Other flows may use a different record. There is no stranger to lock out inside the package, because the only agent working the package is the one that created it.

**`conflicts-with` feeds a planner, not a gate between rivals.** It tells the owning agent which of its own Work Items must not run at the same time, which is exactly the input a scheduler needs.

**Abandonment is recoverable when the configured flow preserves a terminal claim record.** An agent that dies may leave a stale claim without a realized implementation. Detecting that condition is flow-specific; what to do about it is policy, not model.

Real concurrency moves up one level, to two agents holding two Work Packages that touch the same code repository. Neither one can see the other's plan. That case is open, and [section 12](#12-open-questions) records it.

### 9.6 Merge gates

_Mainline_ here means whatever branch the flow integrates into. Which branch that is belongs to the flow, not to this model.

| Gate | Rule                                                                                                                                                                                                        |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| X1   | Every commit reaching the mainline carries a `Realizes:` trailer resolving to a Work Item in the index                                                                                                      |
| X2   | The Work Item it names is not deprecated                                                                                                                                                                    |
| X3   | The change touches only the code repository the Work Item `targets`                                                                                                                                         |
| X4   | No Work Item in flight `conflicts-with` another currently claimed. Inside one package the owning agent avoids this by scheduling, and the gate is the backstop                                              |
| X5   | Every `depends-on` of the Work Item is already realized                                                                                                                                                     |
| X6   | Every realized Work Item on the exact integrated commit SHA has one immutable validation receipt in the HQ evaluation manifest naming that SHA, Work Item, `accepted` verdict, authority, reviewer and time |
| X7   | Reserved. Its rule must define a portable cross-repository integration or activation invariant that is consistent with the complete model; no behavior is currently enforced                                |

X1 is the one that keeps the thread unbroken. Code with no trailer is code with no recorded reason, and the thread is cut at the point where it matters most.

X6 is where judgment enters the model, and it is deliberately not the gate's judgment. A reviewer decides whether the implementation satisfies the Work Item, which requires reading both and is not computable. After the integrated SHA exists, the declared validation authority issues an immutable receipt. The gate checks only that every `Realizes:` value has exactly one corresponding receipt, that its subject equals the integrated SHA, that the verdict is `accepted`, and that its declared fields are well formed. Multiple Work Items on one integrated commit therefore remain unambiguous, and validation never changes the commit it attests.

```yaml
authority: validation:identity-service
subject: commit:BBB
work-item: SPEC-0017-WI-0004
verdict: accepted
by: agent:reviewer-3
at: 2026-03-12T09:45:00Z
receipt: validation:01HRZ...
```

The receipt is external to the commit but can be stored as an immutable git object or by another configured authority; its identifier and digest are anchored by the HQ evaluation manifest, so no forge is required. The `by` value accepts `agent:` and `human:` alike, and the gate does not distinguish. Which of the two the model should require, and what independence or authorization it must prove, is the open question in [section 12](#12-open-questions).

**The pull request is not a unit of this model. The commit is.** Fifteen commits and four Work Items in one pull request is ordinary under feature branching, and every gate above reads commits, so the case needs no rule of its own.

### 9.7 Cross-repository consistency

Git provides no atomic transaction across repositories, so the Work Package is where the state of a change spanning several of them becomes readable at all.

```text
SPEC-0017-WP-0001 realized by:
  web-app             @ commit AAA
  identity-service    @ commit BBB
  compliance-service  @ commit CCC
```

**That view is derived on read and never stored.** It is harvested from `Realizes:` trailers across the registered code repositories, exactly as a Work Item's state is. Writing it into a field would make it wrong immediately, because writing is itself a commit.

The Work Package remains incomplete until every required Work Item is realized and every external verification condition has a passing attestation bound to the exact deployed subject. It orchestrates the Work Items but verifies nothing itself. Its derived view correlates planned state from the Canon, integrated state from git, deployment state from the deployment system, and immutable verification receipts from their declared runtime authority through the HQ evaluation manifest.

## 10. Constitutional principles

Eighteen constitutional principles bound every solution. They are numbered `PRINCIPLE-NN` and referenced by number throughout the framework.

**PRINCIPLE-00 is the metaprinciple.** The other seventeen bound the solution; PRINCIPLE-00 ranks them, and every choice in this document was judged against it first: identity over paths, typed relations over untyped, derived views over maintained ones, one document per question over one document that knows everything.

| ID               | Constitutional principle                                                          | Consequence                                                                                                                                                          |
| ---------------- | --------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PRINCIPLE-00** | Every artifact is reachable within a bounded context budget                       | A correct artifact that cannot be reached does not do its job                                                                                                        |
| **PRINCIPLE-01** | Discovery optimizes for exploration                                               | Discovery Space is allowed to be messy, personal and heterogeneous                                                                                                   |
| **PRINCIPLE-02** | Canon optimizes for shared truth                                                  | Canonical artifacts are curated, structured, versioned and traceable                                                                                                 |
| **PRINCIPLE-03** | Only promoted knowledge enters the Canon                                          | Existing somewhere grants nothing                                                                                                                                    |
| **PRINCIPLE-04** | Artifact identity is independent of location                                      | Paths move when scopes reorganize; identifiers do not                                                                                                                |
| **PRINCIPLE-05** | An artifact lives at the lowest scope that completely owns its subject            | Placement follows conceptual ownership, not convenience                                                                                                              |
| **PRINCIPLE-06** | Scope hierarchy is independent of repository topology                             | Scopes model ownership; repositories model version-control boundaries                                                                                                |
| **PRINCIPLE-07** | Every fact has an authority                                                       | Duplicated truth is minimized; authoritative sources are explicit                                                                                                    |
| **PRINCIPLE-08** | Derived knowledge is generated, not maintained                                    | Traceability matrices and impact reports are computed views, and no state derivable from history is written into an artifact                                         |
| **PRINCIPLE-09** | A Work Item targets exactly one code repository                                   | Cross-repository coordination belongs to the Work Package                                                                                                            |
| **PRINCIPLE-10** | Work Item is the unit of implementation; Work Package is the unit of coordination | Replaces the Epic/Story mental model                                                                                                                                 |
| **PRINCIPLE-11** | Context flows downward; evidence flows upward                                     | Agents start from product context and descend; verification propagates back                                                                                          |
| **PRINCIPLE-12** | Canon and implementation must never knowingly disagree                            | Once judgment identifies a contradiction, Canon or implementation must be reconciled before promotion. Semantic agreement is not established by a deterministic gate |
| **PRINCIPLE-13** | Promotion is guarded by validators                                                | Crossing a trust boundary requires explicit quality gates                                                                                                            |
| **PRINCIPLE-14** | Runtime closes the loop                                                           | Verified runtime evidence is part of the thread and feeds future Discovery                                                                                           |
| **PRINCIPLE-15** | Mess is allowed before promotion; known inconsistency is rejected at promotion    | Promotion is an acceptance boundary: structural consistency is gated, while semantic inconsistency is resolved under PRINCIPLE-12                                    |
| **PRINCIPLE-16** | A code repository holds no canonical artifacts                                    | Canon and code never sit in one tree, so neither can drift into the other                                                                                            |
| **PRINCIPLE-17** | Every HQ and Scope is constituted by exactly one root `charter.md`                | A directory without the Charter is not a Scope; only its `specs/` and `sources/` may hold Canon                                                                      |

Two consequences of PRINCIPLE-00 are easy to miss. The principal actor is an agent, so context cost, determinism and concurrency replace developer experience as design arguments. And **granularity becomes normative**: the ontology holds that size does not determine the category, which is true for classification, but a fifty-page Decision fails PRINCIPLE-00 no matter how well it is classified. Size stops being a matter of style.

## 11. Intellectual lineage

Where the ideas come from, so a reader can tell what is borrowed from what is coined.

| Borrowed                                       | From                                                                                                                                                                                                                                           | Used for                                                                                                                   |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Double Diamond                                 | [British Design Council, 2003](https://www.designcouncil.org.uk/our-resources/the-double-diamond/)                                                                                                                                             | The shape of Discovery and Design                                                                                          |
| Outcomes over outputs                          | Josh Seiden, _Outcomes Over Output_, 2019                                                                                                                                                                                                      | Why Build's result is a verified capability rather than merged code                                                        |
| Digital Thread                                 | Product lifecycle management, manufacturing. Established practice, with no single originating source                                                                                                                                           | The traversable provenance chain                                                                                           |
| Traceability, baselines                        | Systems engineering and configuration management, `ISO/IEC/IEEE 15288`                                                                                                                                                                         | Requirement/implementation linkage and revision control                                                                    |
| Change impact analysis                         | Bohner and Arnold, _Software Change Impact Analysis_, IEEE Computer Society Press, 1996                                                                                                                                                        | Computing what a changed artifact puts at risk                                                                             |
| Architecture Decision Record                   | [Michael Nygard, 2011](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions)                                                                                                                                           | The Decision class's ancestor                                                                                              |
| Trunk-Based Development                        | [Paul Hammant, continuous delivery practice](https://trunkbaseddevelopment.com/)                                                                                                                                                               | The recommended default flow, not the execution model                                                                      |
| Feature branching, GitFlow, GitHub flow        | [Fowler, 2020](https://martinfowler.com/articles/branching-patterns.html), [Driessen, 2010](https://nvie.com/posts/a-successful-git-branching-model/), [GitHub documentation](https://docs.github.com/en/get-started/using-github/github-flow) | The flows the execution model tolerates without prescribing one                                                            |
| Commit trailers                                | [git `interpret-trailers`](https://git-scm.com/docs/git-interpret-trailers), and the `Signed-off-by` convention it documents                                                                                                                   | `Realizes:` as the link from code to a Work Item                                                                           |
| Stacked pull requests                          | Phabricator, and the tools that followed. The original tool is archived                                                                                                                                                                        | Dependent Work Items                                                                                                       |
| Progressive disclosure, provenance frontmatter | [OpenKnowledgeFormat, Google Cloud, 2026](https://github.com/GoogleCloudPlatform/open-knowledge-format)                                                                                                                                        | The substrate and metadata vocabulary                                                                                      |
| Ubiquitous language                            | Domain-Driven Design, Eric Evans, Addison-Wesley, 2003                                                                                                                                                                                         | Why the vocabulary is enforced rather than suggested                                                                       |
| Constitutional charter and delegated authority | Constitutional and federal governance traditions, with no single originating source                                                                                                                                                            | Why every jurisdiction carries one Charter while child membership and delegation derive from nesting and parent acceptance |

### 11.1 The relationship to OpenKnowledgeFormat

[OKF](https://github.com/GoogleCloudPlatform/open-knowledge-format) is adopted as **substrate and metadata vocabulary**, not as graph model.

Adopted directly: markdown with frontmatter and no required SDK; `index.md` as progressive disclosure; the `sources`, `generated`, `verified`, `status` and `stale_after` fields; and the attested-computation pattern, whose attester is explicitly deterministic non-LLM code.

Two places where Integral adds what OKF deliberately omits:

**Identity.** OKF makes the concept identifier the file's path. That is coherent for a corpus whose directory structure is, in OKF's own words, independent of the domain, so paths never move. It breaks at the operation this model is built around: an artifact moving between scopes when ownership changes.

**Relation typing.** OKF conveys the kind of relation in the surrounding prose and treats every link as an untyped directed edge. That suits a corpus that is read. This corpus is audited: it is asked _what broke_, not _what does this say_, and auditing requires knowing the nature of each connection without reading anything.

Neither is a flaw in OKF. They are the difference between a knowledge catalog and a traceability system.

## 12. Open questions

This document describes the agreed model and identifies the constitutional questions it deliberately leaves unresolved.

| Question                                               | Why it is unresolved                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **The judgment points**                                | Gates check form, never correctness. At the execution seam, judgment appears as an immutable validation receipt and the gate reads its form and accepted verdict, not semantic truth. G7 likewise consumes a reevaluation attestation without issuing it. No equivalent judgment is yet defined for authorizing the transition from Design to a build-ready Work Package, including whether effective Constraints inherited from several Specifications are semantically compatible. Who or what may issue these judgments, what independence they require, and by what acceptance rule, remains unresolved |
| **Retrospective conformance**                          | A future exception may let a Decision adopt an existing integrated implementation without creating a Work Item or retroactive `follows`. It is not active in G4. The model requires an auditable fact binding the Decision, exact integrated subject, verdict, authority and time; its portable representation and attestation mechanism remain undefined                                                                                                                                                                                                                                                   |
| **Distributed delegation**                             | Genesis, amendment and same-repository delegation are accepted git revisions, not parallel receipts. The portable authorization contract for a child Scope held in another repository remains unresolved                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Aggregate containment and `part-of`**                | Work Items are physically colocated under their Work Package aggregate while `part-of` remains a declared relation. Whether the relation should become derived from that accepted placement, or the physical layout should stop nesting Work Items, remains unresolved                                                                                                                                                                                                                                                                                                                                      |
| **Discovery provenance**                               | Discovery Space is untracked, and the Intent and Requirements that enter the Canon come from it. OKF's `sources` is the mechanism; the rule for when it is required is unwritten                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Trust is not binary**                                | A baseline is one number. It cannot distinguish an artifact a person reviewed yesterday from one an agent generated two years ago and nobody read                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Design-stage divergence**                            | Prototypes and vendor evaluations are not Decisions, and the model gives them no home. A vendor evaluation is also the record of what was rejected, which is expensive to lose                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Two agents, two Work Packages, one code repository** | One agent per Work Package removed every collision inside a package and moved them up a level, where neither agent can see the other's plan                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Cross-repository integration strategy**              | Git provides no atomic transaction across repositories. Feature flags, release manifests, environment switching and compatibility techniques can coordinate activation, but the framework does not yet define a portable integration or activation contract                                                                                                                                                                                                                                                                                                                                                 |
| **Multi-HQ**                                           | The identifier grammar reserves the namespace. Nothing resolves across HQs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Historical adoption**                                | A legacy estate must enter by reconstructing the historical graph from current implementation and surviving evidence, not by pretending every existing commit already followed the model. The ordering, confidence levels and minimum evidence required for that reconstruction remain to be defined                                                                                                                                                                                                                                                                                                        |

## 13. Common misreadings

Failure modes this framework invites. Each one is a reasonable reading of a rule, applied one step too far.

### Discovery Space is treated as a backlog

**Symptom.** Naming conventions, required fields and cleanup rules appear in Discovery Space. Contributors start asking where a note belongs before writing it.

**Cause.** PRINCIPLE-02 is applied to the wrong side of the boundary.

**Correction.** PRINCIPLE-01 exists to prevent exactly this. The framework does not prescribe how Discovery Space is organized, and turning divergent thinking into bureaucracy is a design failure, not a maturity milestone.

### The Specification carries implementation detail

**Symptom.** A Specification goes stale on every refactor. Nobody trusts it, so nobody reads it.

**Cause.** Solution decisions were written into the Requirement layer.

**Correction.** A Requirement states what must be true; a Decision states how. The test: _if the provider were replaced tomorrow, would this sentence survive?_ If not, it belongs in a Decision.

### A Decision describes the code

**Symptom.** The Decision needs rewriting on every commit, and PRINCIPLE-12 fires constantly.

**Cause.** The Decision was treated as an exhaustive description of the implementation rather than as a set of explicit commitments.

**Correction.** A Decision governs only the commitments it explicitly states. Determining that code contradicts one of them requires judgment; once identified, PRINCIPLE-12 requires the contradiction to be resolved rather than accepted as steady state.

### An artifact is renamed when its owner changes

**Symptom.** Old commits, old Decisions and old evidence stop resolving.

**Cause.** The composed identifier was read as ownership rather than origin.

**Correction.** Identifiers are never renamed and never reused. An artifact that moves between scopes keeps its identifier and moves its file, and a Decision records the move. Ownership changed; origin did not, and origin is what the identifier states. Supersession is a different operation, for when the subject itself changed.

### A traceability matrix is maintained by hand

**Symptom.** The matrix is accurate on the day it is written and misleading a month later.

**Cause.** A derived view was written down as a document.

**Correction.** PRINCIPLE-08. The matrix is a query over the graph. If a view cannot be generated, the missing piece is a relation, not a document.

### Merge is treated as done

**Symptom.** Work Packages close while the capability does not work in production.

**Cause.** The merge boundary was confused with the value boundary.

**Correction.** A Work Item is realized when an accepted integrated implementation carrying its trailer reaches the mainline. A Work Package is complete only when every planned Work Item is realized and external authorities provide the required verification records. The Work Package orchestrates that boundary; it does not perform the verification.

### A hotfix bypasses the lifecycle

**Symptom.** An urgent commit reaches the mainline with no Work Item because the incident was called a hotfix.

**Cause.** Urgency was treated as permission to enter at the line of code instead of at the lifecycle.

**Correction.** Integral has no bypass category called hotfix. Urgent work may compress Discovery and Design to the smallest honest Intent, Requirement and Work Item, but it still enters through the cycle and carries the same provenance. A future adoption process may reconstruct history for code that predates the framework; it does not authorize new unlinked code.

### A Constraint is written with no Intent above it

**Symptom.** A Specification collects rules nobody can trace to a purpose. Arguments about them cannot be settled, because there is nothing to settle them against.

**Cause.** A preference or an observation was filed as a Constraint.

**Correction.** Name the Intent the Constraint serves. If none exists, it is not a Constraint. A preference belongs in a Decision, where `rejected` records what lost and why. An observation belongs in a Source, where `retrieved` records when it was true.

### An internal foundational document is automatically treated as a Source

**Symptom.** A risk policy, data-treatment policy or design system is copied into Source artifacts even when the same scope owns and may change its normative content. Conversely, a document written inside the company is rejected as a Source even though another authority governs it.

**Cause.** External was read as _outside the company_ instead of _outside the consuming decision boundary_.

**Correction.** Classify authority, not provenance. A separately governed policy is a Source to the work that consumes it, whether its authority is internal or external to the organization. A policy governed inside Integral is expressed through its own Specification, Constraints and Decisions. A founding document that constitutes the right to govern is a Charter, not evidence cited by the authority it creates.

### A Scope inherits a Charter instead of carrying one

**Symptom.** A directory is called a Scope and receives Canon even though no document defines its purpose, jurisdiction or authority. Its owner is inferred from an ancestor Charter.

**Cause.** Parent membership was confused with local constitution.

**Correction.** Every HQ and Scope carries exactly one root `charter.md`. Nesting derives the parent and the local Charter defines the child jurisdiction. Within one repository, the accepted git revision introducing that Charter records the parent's authorization; cross-repository delegation requires a portable authorization contract. Without a local Charter the directory is not a Scope and cannot own `specs/` or `sources/` Canon.

### Canon is placed in a generic documentation tree

**Symptom.** Paths such as `identity/docs/models/` appear, and an agent must read their contents to learn whether `models` is a Scope, a Specification, implementation material or exploration.

**Cause.** File format and familiar folder names were allowed to substitute for the ontology.

**Correction.** Integral has no structural `docs/` or `models/` category. Canon exists only under `specs/` and `sources/`; exploration belongs in `discovery/`; a new jurisdiction is a child directory with exactly one root `charter.md`; implementation remains in code repositories.

### A Source is stored as a loose file

**Symptom.** `sources/SOURCE-0001.md` sits beside other Source files and has no aggregate boundary for future supporting material or atomic movement between Scopes.

**Cause.** Source was treated as a flat Markdown collection instead of a root artifact class.

**Correction.** The canonical shape is `sources/SOURCE-0001/SOURCE-0001.md`. Directory and principal file match the identifier, and the complete aggregate moves without changing that identity.

### The Canon and the repositories are read as a division of labour

**Symptom.** Humans are kept out of the code repositories, or agents are kept out of the Canon, and someone configures permissions to enforce it.

**Cause.** A rule about where artifacts live is read as a rule about who may act.

**Correction.** The Canon is entered by promotion and code is entered by a Work Item. Both are gated events, and a gate reads the change, never the author. The framework cannot grant or revoke access, so an access rule would be a recommendation with no gate behind it.

### A Work Item spans repositories

**Symptom.** Pull requests must merge in a specific order across repositories, and one of them cannot be reverted alone.

**Cause.** Coordination leaked into the implementation unit.

**Correction.** PRINCIPLE-09. The Work Item is decomposed per code repository, and the Work Package coordinates them. If a Work Item routinely spans code repositories, it is too large.

### A language model is added to a gate

**Symptom.** The same repository validates two different ways on two runs, and contributors retry until it passes.

**Cause.** A judgment question was mistaken for a form question.

**Correction.** Gates are deterministic by definition. What needs judgment is a review, and it must be visible as one. A non-deterministic gate is worse than no gate, because it manufactures confidence.

### The graph is treated as documentation

**Symptom.** Relations are declared for completeness, and impact analysis returns everything.

**Cause.** Relation types were chosen for how they read rather than for how they propagate.

**Correction.** A relation type exists to answer one question: if the other end changes, what happens to me? `references` is the correct choice for a citation, and it propagates nothing.

## Appendix A: Quick reference

### Scope layout

```text
<scope>/
├── charter.md
├── index.md                     generated once Canon materializes
├── discovery/                  ignored, non-canonical
├── specs/
│   └── SPEC-NNNN/
│       └── SPEC-NNNN.md
├── sources/
│   └── SOURCE-NNNN/
│       └── SOURCE-NNNN.md
└── <child-scope>/
    ├── charter.md
    └── ...
```

`charter.md` makes the containing directory a Scope. Canon exists only below
that Scope's `specs/` and `sources/`; child Scope membership derives from
nesting.

### Identifier forms

```text
SPEC-0017                Specification
SPEC-0017-CAP-0001        Capability
SPEC-0017-CON-0001        Constraint
SOURCE-0001              Source, a root class independent of any Specification
SPEC-0017-REQ-0003        Requirement
SPEC-0017-DEC-0001        Decision
SPEC-0017-WP-0001         Work Package
SPEC-0017-WI-0004         Work Item
<hq>:SPEC-0017           Fully qualified, prefix reserved and unused
SPEC-0017@3              A specific baseline, used only in relations
SOURCE-0001@1            The same form. Specification and Source are the
                        only classes carrying a baseline of their own
```

### The thirteen relations

```text
Derivation     based-on  specifies  respects  narrows  informed-by
               satisfies  implements  follows
Reference      references
Coordination   depends-on  conflicts-with  part-of
Lifecycle      supersedes
```

### The classification test

```text
Why does it matter?              → Intent
What state means success?        → Outcome
What must the system do?         → Capability
What must this work not break?   → Constraint
What separately governed authority
outside this decision argues?    → Source
What must this work make true?   → Requirement
What durable solution commitment
governs subsequent work?        → Decision
What change must be executed?    → Work Item
What actually implements it?     → Implementation
```

### The rules that decide most arguments

```text
Provenance is declared upward. Navigation is derived downward.
Composition is never declared; the identifier states it.

The nearest containing charter.md identifies the Scope. Only that
Scope's specs/ and sources/ hold Canon.

A relation type exists to answer one question: if the other end
changes, what happens to me?

Gates check that the graph is well formed. They never check that
it is right.

Mess is allowed before promotion. Inconsistency is not allowed after.

Knowledge that cannot be reached within a context budget does not
exist for whoever writes most of the code today.
```
