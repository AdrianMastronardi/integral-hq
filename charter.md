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
| **Forge-independent**    | The traceability core needs plain git. Forges may enrich coordination and review; runtime completion requires configured external authorities          |
| **Multi-repository**     | Planning and traceability across repositories are first-class. Portable integration and activation remain an explicit open contract                    |
| **Format-minimal**       | Canon uses an open, inspectable representation selected by Specification; no proprietary runtime is required to read it                                |

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

### 4.1 The ontology: nine concepts in the thread

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

This is not the list of Canon artifact classes. Intent and Outcome are knowledge contained by a Specification rather than independently identified artifacts. Work Package is a coordination artifact that organizes Work Items but adds no semantic step to the chain above. Implementation is code in a code repository, not a Canon artifact. [Section 6.1](#61-eight-classes) defines the resulting eight Canon classes.

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
9. Is it **source code, configuration or infrastructure**? → Implementation

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

The Canon is rooted at the **HQ**: the repository an agent enters the system through. Its root `charter.md` constitutes its authority. Once Canon materializes, its generated `docs/index.md` resolves the tree and its `docs/specs/` and `docs/sources/` collections hold root Canon. Everything canonical hangs off it.

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
├── discovery/                  ignored, non-canonical
├── docs/                        reserved Canon root
│   ├── index.md                 generated when Canon materializes
│   ├── specs/                   Specifications owned by the HQ
│   └── sources/                 Sources curated by the HQ
├── identity/                    child Scope because charter.md exists
│   ├── charter.md
│   ├── discovery/
│   └── docs/
│       ├── index.md
│       ├── specs/
│       └── sources/
└── payments/                    child Scope
    ├── charter.md
    ├── discovery/
    ├── docs/
    │   ├── index.md
    │   ├── specs/
    │   └── sources/
    └── settlement/              nested Scope
        ├── charter.md
        ├── discovery/
        └── docs/
            ├── index.md
            ├── specs/
            └── sources/
```

_Product_ is not a term of this framework. A product is a scope like any other, named by whoever owns it. The framework already has one word for a node that owns conceptual truth, and a second word would name a level rather than a role.

#### Constitutional authority

Placement answers **who owns this subject**. The mandatory `charter.md` at that location answers **why that owner has authority to decide it and what falls inside its jurisdiction**.

The **HQ Charter** is the founding record that constitutes the HQ. Every other Scope also carries exactly one `charter.md`. A directory without it is not a Scope, and one jurisdiction never has two concurrent Charters. The Charter states why its containing Scope exists, what it includes and excludes, the authority under which promotion occurs, and how its foundations may be amended.

Charter is not an ordinary Source: a Source is cited evidence or authority outside a consuming decision boundary, while `charter.md` creates the boundary in which that Scope's Canon can exist. It is not a Specification either: a Specification states a result the product must produce, while the Charter legislates who may decide and within what jurisdiction. For that reason Charter is structural metadata outside the eight Canon artifact classes. It has no `CHARTER-NNNN` identity: the containing Scope is its subject, and accepted repository history preserves its exact text.

The HQ originates through Genesis: the accepted git revision that first introduces its root Charter into the HQ's authoritative history. Git records the exact content, attribution and time; when repository policy requires a cryptographic commit signature, that signature is part of the same evidence rather than a second constitutional document.

A child Scope does not constitute itself independently: nesting derives its parent and its own Charter defines its jurisdiction. Within the same repository, the accepted git revision that introduces the child Charter under the parent records the delegation. A child Charter may narrow the parent grant but may neither broaden nor contradict it. A portable authorization mechanism is needed only when the child crosses repository boundaries. Scope ancestry still creates no Constraint inheritance; enforceable product obligations remain in Specifications and flow through `based-on`.

The complete structural vocabulary of a Scope is deliberately small:

```text
charter.md    curated constitutional authority
discovery/    ignored, non-canonical exploration
docs/         reserved Canon root
  index.md    generated navigation once Canon materializes
  specs/      Specifications
  sources/    Sources
<child>/      another Scope exactly when <child>/charter.md exists
```

`docs/` and `discovery/` are reserved collections, never Scopes. Within `docs/`, `specs/` and `sources/` are also reserved. A directory below those collections may organize a Canon aggregate; it does not create jurisdiction. A non-reserved child directory becomes a Scope only through its own accepted `charter.md`.

The founding Charter and every accepted revision remain recoverable through git history. Charter carries no independent revision field: the accepted git revision identifies its exact text.

An amendment is a signed commit accepted on `main` under the repository protections in force for the HQ. It requires no parallel receipt, second Charter or Charter-specific approval path. An amendment may change the means by which the HQ acts, but it must preserve the founding purpose **Change without losing intent**. A revision that changes that purpose is not an amendment: it founds a different HQ through a new Genesis.

Portable authorization for a child in another repository remains an open interoperability contract. The model no longer leaves open whether Charter is an artifact, whether a Scope may omit one or how this Charter may be amended.

The placement rule:

> **A canonical artifact lives at the lowest scope that completely owns its subject.**

This prevents both unnecessary centralization and duplicated canonical truth. A decision governing two services in Identity belongs under `identity/docs/specs/`, not to the root and not to either service. `identity/charter.md` establishes that Identity has authority over that subject.

The same rule decides what lives at the HQ, because the HQ is the root scope. Nothing has to be enumerated: whatever no scope below completely owns belongs there. In this repository, that is the definition of the framework itself.

What sits there has the ordinary shape. An organization-wide product obligation is not a loose statement pinned to the root or hidden in the Charter; it is a Specification under the HQ's `docs/specs/`, whose Intent is organization-wide and which holds the Constraints that Intent justifies. _Operate lawfully in the jurisdictions we sell in_ is an Intent, and data residency is one of its Constraints. The Charter establishes who may own that rule, not the rule's product semantics.

**The HQ is always a repository, and a Scope may be one.** Canon lives in repositories because repositories provide immutable candidate revisions for verification. A split Scope may run repository-local validators, but canonical promotion is always accepted through the HQ, which serializes acceptance and preserves global identity. The verification Specification defines the concrete protocol. By default a Scope is a directory inside the HQ, which is one clone and no coordination. Splitting a Scope into its own repository is allowed when something forces it, an access boundary the organization must enforce being the usual reason. It costs a hop against PRINCIPLE-00, so it is a decision, not a default.

**A code repository holds implementation and repository-local supporting material, but no canonical Integral artifacts.** Every governed implementation change remains traceable to the Work Item it realizes; the accepted verification contract defines how that claim is represented and checked.

**A code repository registers into exactly one scope through authoritative structural metadata declared only by that scope.** Placement determines ownership; that Scope's `charter.md` constitutes its authority. The HQ derives repository resolution and global uniqueness from those declarations. Generated indexes, locks and external resolvers may materialize or verify a registration, but never author it. Registration links code to ownership; it does not move ownership into the code repository.

**A Constraint applies through the non-exclusive Specification hierarchy, not through Scope.** A Specification may declare any number of upstream Specification baselines through `based-on`; it inherits the union of their effective Constraints transitively. Capability and Constraint are evaluated together inside the Specification. Every separate Requirement, Decision and Work Item belonging to it is derived as `constrained-by` its own and inherited Constraints; none repeats that fact. When a Constraint changes, those derived edges select every affected branch for reevaluation. Placement in a descendant scope creates no inheritance.

Specifications that share an upstream base inherit its Constraints but do not inherit local Constraints laterally from one another. When a local Constraint comes to govern several such Specifications, it graduates to a common upstream Specification: a new authoritative Constraint there supersedes the local formulation, and each affected Specification reaches it through its own derivation graph. The generated index materializes each Specification's effective Constraint set. Deterministic verification checks hierarchy, coverage and the structural validity of narrowing; review decides whether one Constraint is semantically stricter than another.

The union of inherited Constraints must be coherent. A derived Specification may neither ignore nor override an inherited Constraint when two upstream bases disagree. A known contradiction blocks the transition from Design to Build until the Specifications that own those Constraints resolve or supersede them. Detecting semantic conflict is judgment, not a deterministic gate; the unresolved judgment mechanism is recorded in [section 12](#12-open-questions).

#### Canonical collections and aggregates

The Canon owned by one Scope is exactly the union of its `docs/specs/` and `docs/sources/` trees. `docs/` is reserved for Canon and is not a generic documentation directory. A canonical document either belongs to a Specification aggregate or records a separately governed authority as a Source.

Specification semantically contains its Intent, Outcome, Capabilities, Constraints and Requirements. Work Package coordinates its Work Items. Source remains independent of every Specification and may carry supporting material. The accepted representation Specification decides how files, collections and aggregate directories realize those facts; a directory alone creates neither identity nor authority.

A Source lives in `docs/sources/` of the lowest Scope that completely owns the curated extract, whether or not another Canon artifact currently cites it. Its underlying resource may live inside or outside the HQ and remains governed outside the consuming decision boundary.

When a Scope first accepts Canon, the same promotion materializes its generated `docs/index.md`. It provides navigation to local Specifications, local Sources and immediate child Scopes without flattening every descendant into one file. Agents descend through the index tree within PRINCIPLE-00. The representation Specification defines whether any subordinate generated navigation is needed; it can never create a second authority for Canon facts.

Scope is a property of placement. It appears in neither the identifier nor the artifact representation: reorganizations move artifacts between scopes, an identifier that changes is not an identifier, and a declared scope is a second copy of something the path already says.

### 4.5 The Canon and the repositories

Two bodies of work, and one seam between them.

```text
  CANON                      THE SEAM                     CODE
  docs/specs and             typed links                  code repositories
  docs/sources
  inside each Scope
  ─────────────────────────  ─────────────────────────    ───────────────────────
  Work Item   ───────────►   implementation target   ──►  code repository
  Work Item   ◄───────────   realization claim       ◄──  implementation revision
  Work Item   ◄───────────   validation evidence     ◄──  integrated revision
```

The implementation target is declared once, in the Canon. An immutable implementation revision carries the realization claim in the form selected by the accepted representation and verification contracts. After that revision is judged, a validation authority issues evidence that identifies the exact implementation subject and Work Item. [Section 9](#9-the-execution-model) defines the semantic boundary without prescribing one implementation mechanism.

The Canon holds no code and a code repository holds no Canon. The Work Item is the only artifact either side names, and the Work Package coordinates Work Items without touching code itself.

Discovery and Design produce nothing in the code world. They may read it, and often must: choosing between extending a service and writing a new one requires knowing what already exists. Reading code is not an operation on artifacts.

That reading is also why the Decision class exists. If every Design had to re-derive the standing commitments from source, PRINCIPLE-00 would fail on the first attempt. A Decision records what was committed to and what was rejected, so the next Design reads the Canon instead of the repository.

**The framework governs the Canon completely, and the code world at one point.** That point is the immutable implementation revision, which declares the Work Item it realizes. Everything else about how code is written belongs to the code repository: language, architecture, test strategy, packaging, deployment and branching model.

## 5. Definitions

Terms coined or given a specific meaning by Integral. Where a term is borrowed, its origin is named. Anything not defined here carries its ordinary industry meaning.

### 5.1 Process terms

**Integral**
An operating system for agentic product development: the framework defined by this document.

**HQ**
The single repository an agent enters the system through. Its root `charter.md` constitutes the authority under which its Canon may exist. Once Canon materializes, its `docs/index.md` resolves every artifact identifier. It is also the root Scope, so its `docs/specs/` and `docs/sources/` hold whatever Canon no child Scope completely owns. An agent never enters by opening an isolated repository with no product context.

**Charter**
The mandatory `charter.md` at the root of an HQ or Scope. It states why its containing jurisdiction exists, what it includes and excludes, the authority under which it may promote Canon and how its foundations may change. It is structural authority, not a Canon artifact, carries no `CHARTER-NNNN` identity and is never inherited in place of a local Charter. Exactly one exists per HQ or Scope; a directory without one is not a Scope.

**Discovery Space**
The non-canonical, exploratory, personal half of the system. Heterogeneous by design and typically not version-controlled. A Scope may expose it through a gitignored `discovery/` directory, but Integral prescribes nothing below that boundary. It holds raw signal and the convergence passes over it.

**Canon**
The curated, shared, version-controlled body of artifacts that are authoritative within their declared domain under the containing Scope's Charter. Inside a Scope it is exactly the union of `docs/specs/` and `docs/sources/`. Only promoted knowledge enters it; `charter.md`, `docs/index.md` and `discovery/` are not Canon artifacts.

**Promotion**
The HQ-serialized guarded event by which an artifact crosses from Discovery Space into the Canon, or by which a Specification or Source advances to a new baseline. Candidate content may live in the HQ or a split scope repository, but only the HQ promotion boundary accepts it into the global Canon. Promotion is a consistency boundary, not a workflow status and not a file move. Its representation and verification contracts preserve global identity and the accepted revision.

**Gate**
A deterministic, computable check over declared inputs that blocks a promotion when a declared condition fails. Given the same validator version and the same inputs, it always produces the same result. A check requiring judgment is a review, not a gate.

**Review**
A judgment about whether something is right, recorded as immutable evidence so that deterministic verification can establish that it happened. A review is not deterministic and never becomes a gate. At the execution seam, its evidence identifies the exact implementation subject, Work Item, verdict, authority, actor and time. It lives outside the subject it attests and must remain independently verifiable.

**Baseline**
The current agreed semantic revision of a Specification or Source. It is not merely a repository revision: raising it is a deliberate act. A baseline must resolve immutably to the complete accepted meaning it names, including upstream Specification baselines where applicable. Downstream artifacts identify the exact baseline on which their meaning depends.

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
A separately governed authority or body of evidence plus what this framework extracted from it: a regulation, an internal policy owned in GRC, a paper, a vendor benchmark or an incident report. The relevant boundary is the consuming work's decision authority, not the organization's perimeter. The artifact is not the underlying resource. It preserves durable citation, an extract in this framework's words, its applicability and when it was consulted, so its meaning survives an unavailable resource. A locator is optional and may identify a URI or file inside or outside the HQ.

Not every Specification or Decision requires a Source. Tacit knowledge is valid input, and Integral never requires a fabricated citation merely to satisfy structure. When a separately governed authority materially informs an artifact, however, the canonical Source and the exact baseline used belong in the graph.

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
The concrete technical form of the work: source code, configuration, migrations, infrastructure and tests. Implementation is code. It is referenced by the Canon, never held in it.

### 5.3 Structural terms

**Artifact**
A canonical semantic or coordination unit with a stable identity, a declared class and typed relations to other artifacts.

**Scope**
A jurisdictional node of conceptual ownership in the tree hanging off the HQ, constituted by exactly one `charter.md` at its root. Scopes nest. A Scope is a directory inside the HQ by default, and may be a repository of its own when an operational boundary requires it. A child belongs to its parent by directory nesting. Canon ownership is derived from the nearest containing Scope and its reserved `docs/specs/` or `docs/sources/` collection, never declared in an artifact.

**Code repository**
A version-control boundary holding implementation and repository-local supporting material. It registers into exactly one Scope, it never holds a canonical Integral artifact, and each Work Item identifies exactly one such repository as its target. Every governed change declares the Work Item it realizes. The HQ is a repository too, and so is a Scope that has been split out; _code repository_ names the kind that carries no Canon.

**Composed identifier**
An identifier built from its origin: `SPEC-0017-REQ-0003`. It states **origin, not ownership**. Origin is immutable because the past does not change; Scope ownership may change when responsibility for the same subject moves.

**Index**
The generated `docs/index.md` of every HQ and Scope that holds materialized Canon. It is the bounded navigation entry point for that Scope and is derived rather than maintained by hand. The accepted representation and verification Specifications define its exact contents and how equality with the Canon is checked.

**Authority**
The single authority that owns a given fact or grants a decision boundary. Canonical documents reference authoritative facts rather than copying them, and never replace the system that holds them. The API contract's authority is the OpenAPI document; the deployment state's authority is the deployment system; the Requirement's authority is the Specification; the Scope's right to govern that Requirement comes from its own `charter.md` and the parent acceptance chain.

**Derivation, Reference, Membership, Coordination, Lifecycle**
The five genera of relation. Only Derivation propagates staleness; the rest cite context, establish immediate containment, order execution, or change lifecycle.

## 6. The artifact model

### 6.1 Eight classes

The Canon holds exactly eight classes. They are the stable semantic and coordination units the graph must identify; Implementation remains outside the Canon.

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

A Source is not decided inside the consuming boundary, so no Intent in that boundary stands over it. The underlying authority may be an external regulation or an internal policy decided and maintained by another body. A Source is created when preserving that authority or evidence has value; it is not mandatory for tacit knowledge and need not be tied to one consumer. One policy or paper may inform work across several Specifications, so composing it against one would state an origin that is not true.

Every class other than Specification and Source uses an identifier composed from its Specification of origin, Constraint included. A Constraint with no Intent above it has no reason to exist, and §5.2 makes that a test rather than a style note.

Six things that look like current Canon artifact classes and are not:

| Not a class      | Where it actually lives                                                 |
| ---------------- | ----------------------------------------------------------------------- |
| Test             | Code. The Requirement records the criterion by which it can be verified |
| Runtime Evidence | External authority. Evidence feeds a derived Work Package view          |
| Implementation   | Code. Traceable through the Work Item                                   |
| Scope            | Placement, and placement is derived                                     |
| Index            | A generated file, rebuilt from the tree rather than curated             |
| Charter          | Mandatory structural authority at the Scope root; not part of Canon     |

Nothing is lost. Each remains in its authoritative system or is referenced from Canon, which is what PRINCIPLE-07 requires. Promoting them to classes would fill the index with thousands of uncurated nodes that age on their own, which PRINCIPLE-00 forbids.

The index is worth stating outright, because it is derivable, generated and persisted all at once, and PRINCIPLE-08 forbids exactly that combination inside an artifact. It escapes because **a generated file is not an artifact.** Its representation identifies it as generated, nothing declares a relation to it, it holds no identifier of its own, and it is rebuilt rather than edited. PRINCIPLE-08 governs what is curated; a generated file is the output the principle asks for, not a case against it.

### 6.2 Cardinality

```text
Specification 1 ─── 1..N  Capability
Specification 1 ─── 0..N  Constraint
Specification 1 ─── 0..N  Requirement
Specification 1 ─── 0..N upstream Specification baselines  (through based-on)
Requirement  1 ─── 1..N  Capability       (of the same Specification)
Specification 1 ─── 0..N  Decision
Specification baseline 1 ─── 0..1  Work Package
Work Package  1 ─── 1..N  Work Item        (each WI belongs to exactly one WP)
Work Package  1 ─── 1..N  affected Capability  (derived through WI and Requirement)
Decision      1 ─── 0..N  Work Item        (through prospective follows)
Work Item     1 ─── 1     target code repository
```

At most one Work Package exists for a Specification baseline, and only when reevaluation finds implementation work to perform. A semantic change that the current implementation already satisfies creates no Work Package and does not reopen completed work.

These are coverage cardinalities, not a requirement that the numbers of Requirements, Decisions and Work Items be equal. A Decision is optional; a Work Item does not need a ceremonial Decision in order to implement a Requirement. Every new or adapted Work Item caused by a Decision declares that dependency, and one Decision may require several such Work Items when implementation crosses repository boundaries. A future retrospective-conformance mechanism may allow a Decision that adopts an already conforming implementation to have no Work Item, but that exception is not active until its portable evidence is defined.

A Requirement, Decision and Work Package declare immediate membership in exactly one Specification baseline; a Work Item declares immediate membership in exactly one Work Package. The latter resolves transitively to the same Specification baseline, so membership does not need to be duplicated on the Work Item. Cross-Specification execution order does not move either Work Item out of its own Work Package. Reevaluation places a Capability inside the new Work Package when one or more of its Requirements require new or adapted Work Items; a Capability whose current realized Work Items remain valid stays outside that Work Package. At completion, the planned and realized Work Item identity sets must be equal; the equality is over Work Items, not commits or implementation fragments.

A Source has no composition cardinality here at all: it is cited by any number of artifacts and belongs to no Specification. Its canonical artifact is owned by the Scope containing its `docs/sources/` collection; the underlying resource remains under its separately governed authority.

### 6.3 Representation authority

The Charter defines what each artifact means and the invariants the Canon must preserve. It does not freeze a serialization format, metadata field set, body template, filename convention, lifecycle vocabulary or validation algorithm. Accepted Specifications own those implementation contracts:

- the representation Specification defines artifact structure, fields, relation serialization, aggregate layout, index shape and lifecycle vocabularies;
- the verification Specification defines deterministic checks, state transitions, evidence contracts and promotion behavior.

Changing either contract within these constitutional boundaries requires a new Specification baseline, not a Charter amendment. A representation change requires an amendment only when it changes the ontology, authority, identity, ownership, membership or traceability semantics stated here.

Every canonical artifact must expose a stable identity, its class, its lifecycle and its typed relations in a machine-readable form selected by the representation Specification. Specification and Source carry semantic baselines. The representation Specification decides which semantic constituents are inline and which Canon classes are represented separately.

Work Package and Work Item additionally carry exactly one explicit execution status for coordination. That status is not the artifact lifecycle and does not establish realization, validation or runtime verification; those remain evidence-backed facts. The representation Specification defines the allowed status vocabulary, and the verification Specification defines any permitted transitions.

Work Package and Work Item are the artifacts a development agent receives as orders of work, so their accepted representations must provide the complete context needed to coordinate or execute them without depending on external navigation. The representation Specification decides how those self-contained projections are constructed. Other artifacts need not duplicate their dependencies and may use resolvable links.

A Source preserves one separately governed authority or evidence body through a durable citation, a self-contained extract, its applicability and the date it was consulted. A resource locator is optional and may point to a URI or file inside or outside the HQ. Referencing a Source identifies the exact Source baseline used. Discovery provenance is optional, non-authoritative context and is distinct from a canonical Source relationship.

## 7. Identity and the graph

### 7.1 Three questions, three answers

A file path answers three questions at once, which is why paths make poor identifiers. Integral separates them.

| Question                     | Answered by            | Lives in | Stability          |
| ---------------------------- | ---------------------- | -------- | ------------------ |
| What is this?                | Stable identifier      | Artifact | Permanent          |
| What relates to it, and how? | Typed relations, by ID | Artifact | Follows the graph  |
| Where is it now?             | Generated index        | Derived  | Volatile by design |

**The graph never uses paths.** Prose links do, because a markdown link is what a human clicks. Move a file and the graph does not notice; the prose link breaks, a gate reports it, a tool rewrites it. The layer that degrades is the one that can afford to.

**Identity is cheaper than the path.** With paths as identifiers, asking _who implements REQ-0003_ means scanning the tree, and the cost grows with the corpus. With a stable identifier and an index it costs one bounded navigation read. The index is also the map an agent loads before opening the relevant artifact.

### 7.2 Identifier rules

| Rule                          | Reason                                                                                                                                                                                                           |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Composed against the origin   | The origin is immutable, so the identifier cannot become a lie                                                                                                                                                   |
| Sequential with a type prefix | An agent can write and verify them directly                                                                                                                                                                      |
| Assigned at promotion         | Holding a canonical identifier is what being canonical means. The HQ promotion gate serializes assignment across every Canon repository, so parallel candidate branches cannot allocate independently or collide |
| Never reused                  | An implementation claim naming `SPEC-0017-WI-0004` must resolve to the same Work Item forever                                                                                                                    |
| Never contains the scope      | Reorganization moves artifacts between scopes                                                                                                                                                                    |
| Never contains the baseline   | The baseline is state, the identifier is origin                                                                                                                                                                  |

**The artifact does not declare its Scope either.** For an artifact under `docs/specs/` or `docs/sources/`, the owner is the nearest ancestor directory carrying `charter.md`. Placement already states it and the index already derives it. A field that repeats what is derivable is a field that can disagree with it, and on the day the two disagree there is no rule saying which one wins.

The one case a `scope:` field would win is an artifact filed in one place and belonging to another. That is exactly the state the placement rule exists to forbid, so winning that case is not a feature.

Moving a canonical artifact between Scopes is therefore a move of its complete representation, including any aggregate, between the corresponding `docs/specs/` or `docs/sources/` collections, and it needs a Decision recording why. Verification compares the index before and after and rejects a move that no Decision accounts for.

Two consequences worth stating outright:

**Semantic deletion does not exist for an artifact in the ordinary lifecycle.** A promoted artifact is deprecated rather than removed, and its identifier remains resolvable for downstream references. A gate rejects ordinary removal, so the rule does not depend on anyone remembering it. Exceptional physical removal required by security or law preserves a resolvable tombstone; the purge mechanism is implementation-defined.

**A retired Specification's identifier stays a valid prefix** for artifacts that are still live. That follows from never reusing identifiers, and it is what makes composed identifiers safe.

`SPEC-0017` in full is `<hq>:SPEC-0017`; the prefix is omitted when it resolves against the current HQ. Nothing writes it and nothing parses it today. Reserving the grammar costs one line and is what keeps every existing identifier valid on the day two HQs have to coexist.

### 7.3 Authority of relationship facts

> **A dependency belongs to the dependent; membership belongs to the constituent. Navigation is derived. Origin is encoded in the identifier.**

Every dependency fact is authoritative at the artifact whose meaning or execution depends on the target. Every membership fact is authoritative at the constituent whose immediate parent it identifies. The representation Specification may choose how those facts are serialized, but it may not create a second authority by requiring the target or parent to maintain the inverse. The creation order of artifact identities is irrelevant, but a new relationship may be promoted only against a target that already exists. An existing artifact may therefore acquire a dependency on a newer upstream artifact during reevaluation, while no relationship may manufacture retroactive provenance.

This is not a stylistic choice. If a target had to list the artifacts that depend on it, writing a Decision would edit the Specification, which raises its baseline and needlessly sends every downstream artifact through reevaluation. **A baselined artifact would be reopened by the act of something being built from it.**

Reverse navigation is computed from the authoritative facts. That inverted map is what an agent navigates, so preserving one authority costs downward navigation nothing.

A composed identifier records where an artifact originated; it does not declare current membership. Immediate membership is explicit so an artifact may move without changing identity. For a Work Item, following its Work Package membership and then that package's Specification membership resolves the governing Specification baseline transitively.

### 7.4 The relation vocabulary

The labels below state the semantic model in this Charter; they are not required serialized field names. The representation Specification owns their concrete names, direction and scalar or sequence shape while preserving these connections and effects.

| Conceptual label | Genus        | Semantic connection                                                            | Effect of change                                                                                   |
| ---------------- | ------------ | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- |
| `based-on`       | Derivation   | Specification to upstream Specification baseline; Decision to earlier Decision | reevaluate the dependent artifact; stale only if it no longer holds                                |
| `specifies`      | Derivation   | Requirement to one or more Capabilities of the same Specification              | reevaluate the Requirement; stale only if it no longer holds                                       |
| `respects`       | Derivation   | Decision to Constraint                                                         | reevaluate the Decision; stale only if it no longer holds                                          |
| `narrows`        | Derivation   | Constraint to Constraint                                                       | reevaluate the narrower Constraint; stale only if it no longer holds                               |
| `informed-by`    | Derivation   | Canon artifact to exact Source baseline                                        | reevaluate the dependent artifact; stale only if it no longer holds                                |
| `satisfies`      | Derivation   | Decision to Requirement                                                        | reevaluate the Decision; stale only if it no longer holds                                          |
| `implements`     | Derivation   | Work Item to Requirement of the same Specification                             | reevaluate the Work Item; stale only if it no longer holds                                         |
| `follows`        | Derivation   | Work Item to Decision of the same Specification                                | prospective provenance; reevaluate the Work Item and stale it only if the Decision no longer holds |
| `references`     | Reference    | any Canon artifact to any Canon artifact                                       | no propagation                                                                                     |
| `part-of`        | Membership   | constituent to immediate canonical parent                                      | establish membership and baseline context without propagating staleness                            |
| `depends-on`     | Coordination | Specification to upstream baseline, or Work Item to Work Item                  | order promotion or execution without propagating staleness                                         |
| `conflicts-with` | Coordination | Work Item to Work Item                                                         | inform scheduling without propagating staleness                                                    |
| `supersedes`     | Lifecycle    | new artifact to retired artifact                                               | freeze the retired artifact without propagating staleness                                          |

A relation that points at a Specification or Source names the exact baseline when that revision matters. `based-on` has two distinct typed uses: a Specification may name zero or more upstream Specification baselines, establishing a non-exclusive Constraint-inheritance hierarchy; a Decision may name the earlier Decisions whose commitments condition it. Decision membership, not a generic Specification dependency, supplies its governing Specification baseline.

`part-of` identifies the immediate canonical parent. Requirement, Decision and Work Package each point to exactly one Specification baseline. Work Item points to exactly one Work Package of the same Specification and resolves its Specification baseline transitively. Capability and Constraint membership is intrinsic to the Specification that holds them and requires no separate membership relation. On a Specification baseline advance, every continuing constituent's membership is updated mechanically to the new baseline; accepted history preserves prior membership without weakening the current graph.

Thirteen semantic relations. The governing rule:

> **A relation type exists to answer one question: if the other end changes, what happens to me? Two types with the same answer are one type with two names.**

`contains` and `blocks` are absent by application of that rule. `contains` is the inverse of immediate membership; `blocks` is the inverse of execution dependency. Declaring either would put one fact in two places.

Everything derived, and the three different places it is derived from:

| Derived by                    | Examples                                                                                                                              |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Inverting the declared graph  | `contains`, `blocks`, `specified-by`, `respected-by`, `narrowed-by`, `informs`, `satisfied-by`, `implemented-by`, `superseded-by`     |
| Shared Specification identity | `constrained-by` from every separate Requirement, Decision and Work Item to each Constraint of that Specification                     |
| Reading an external authority | realization from implementation history, validation and verification from their evidence, deployment state from the deployment system |

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

Constituting a Scope is the structural event immediately before that rule can apply there. Genesis is the accepted git revision that introduces the HQ's root `charter.md`; an accepted revision introducing a child `charter.md` creates a child Scope under the authority of its parent. A directory cannot receive a Specification or Source promotion before that event. Git does not represent empty collections, so `docs/specs/`, `docs/sources/` and the first generated `docs/index.md` materialize with the Scope's first ordinary promotion rather than pretending to exist at Genesis. A separate portable authorization record is required only when authority crosses repository boundaries; it must never masquerade as ordinary artifact promotion.

```text
Discovery Space              ──distill──►  gates  ──►  Baselined Specification
Specification + exploration  ──distill──►  gates  ──►  Decisions and build-ready Work Package associated with its baseline when implementation must change
Work Package + code          ──verify───►  gates  ──►  Affected capabilities implemented and externally verified in production
```

### 8.2 Promotion gates

Promotion is guarded by deterministic verification over immutable declared inputs. The Charter requires the following invariants; the accepted verification Specification formalizes their algorithms, manifests, evidence schemas and diagnostics:

- every identifier, baseline and relation target resolves uniquely, and identities are never reused;
- every Scope and Canon artifact satisfies the accepted representation contract and appears only within its authoritative boundary;
- every relation is typed, points to an allowed class and is declared only by its authoritative source;
- Requirements, Decisions and execution work have complete coverage without manufacturing ceremonial artifacts;
- derivation, membership, coordination and lifecycle graphs satisfy their applicable acyclicity and origin rules;
- accepted lifecycle history remains resolvable, including deprecated and moved artifacts;
- a changed derivation input selects every affected descendant for semantic reevaluation, without a deterministic gate pretending to make that judgment;
- every Specification exposes the coherent transitive set of effective Constraints that governs its constituent work; and
- completion claims resolve to the required implementation, validation and runtime evidence.

Verification may generate navigation, ledgers, manifests and derived freshness or evidence views. Those generated structures never become competing authorities for facts already owned elsewhere. Given the same declared inputs and verifier version, verification must produce the same result.

Three Work Items implementing one Requirement raise a different question, and it is not acyclicity. It is whether they may reach the mainline or become externally available one at a time. [Section 9.1](#91-two-boundaries-not-one) keeps that integration strategy outside the current model.

### 8.3 The boundary of what a gate can do

> **Gates check that the graph is well formed. They never check that it is right.**

Whether an Intent is the right Intent, whether a Decision chose well, whether a Requirement is worth having: no deterministic rule reaches these.

This boundary is deliberate, and it is also the framework's largest open question. With gates alone, an agent can carry an artifact from nothing to promoted with no person involved. Where human judgment enters the model is not yet specified. See [section 12](#12-open-questions).

### 8.4 Baselines and staleness

**Specification and Source are the only artifact classes that carry semantic baselines.** Before first promotion they have no baseline. Artifact lifecycle and semantic revision remain distinct concepts: lifecycle says where an artifact stands, while baseline identifies one agreed meaning. The representation Specification defines how both are encoded and their vocabularies; the verification Specification defines the allowed transitions and checks.

A Specification baseline names its Intent, Outcome, inline Capabilities, inline Constraints, Requirements and resolved upstream Specification baseline set. A semantic change to any of those advances the baseline through the same promotion boundary. Decisions, Work Packages and Work Items are derivatives associated with the applicable Specification baseline; creating one does not redefine the Specification. For a Source, the baseline includes only its own semantic content.

Every baseline resolves immutably to accepted content and its upstream baseline set. Verification rejects silent semantic changes and reuse of one baseline for different content. The exact ledger, digest and manifest representations belong to the verification Specification.

When a baseline changes, deterministic graph traversal selects affected Derivation descendants for reevaluation. It does not decide whether they remain valid. The resulting judgment is recorded as immutable evidence, from which freshness views are derived. An accepted upstream baseline change also advances every affected Specification baseline because its effective Constraint set changed, even when its local text did not. If existing implementation remains valid, no Work Package is required; uncovered or stale work produces one for the new effective baseline.

**The identifier says who carries a baseline.**

```text
carries its own                    resolves a governing Specification baseline
───────────────                    ───────────────────────────────────────────
SPEC-0017        Specification      SPEC-0017-CAP-0001   Capability
SOURCE-0001      Source             SPEC-0017-CON-0001   Constraint
                                   SPEC-0017-REQ-0003   Requirement
                                   SPEC-0017-DEC-0001   Decision
                                   SPEC-0017-WP-0001    Work Package
                                   SPEC-0017-WI-0004    Work Item
```

Read the left column: no prefix, because nothing stands above it. Read the right: every identifier names the Specification from which it originated, while immediate membership resolves the applicable baseline. Only two classes carry their own semantic baseline.

The same rule governs all Derivation relations. When a Source or upstream Specification advances, any dependent artifact pinned to the earlier baseline is selected for reevaluation. The comparison never predetermines the result; it selects a candidate and requires semantic judgment.

Iteration and supersession are different operations, and Intent and Outcome are what tell them apart:

| Operation     | When                                                                        | Effect                                                                                     |
| ------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Iterate**   | Intent holds and the Outcome remains a refinement of the same success state | Same identifier, baseline rises                                                            |
| **Supersede** | Intent changes, or the Outcome defines a materially different success state | New identifier; the new artifact declares `supersedes` to the old one, which is deprecated |

An Outcome change therefore does not predetermine the lifecycle operation. Raising a target or refining how the same result is measured normally iterates the Specification. Replacing the state that defines success normally supersedes it. This is a semantic judgment: the artifact makes the choice explicit and reviewable, while deterministic verification establishes only that the selected operation is structurally consistent.

Everything else in a Specification may be rewritten from end to end while retaining the same identity, provided the Intent holds and the Outcome still describes the same success state. The baseline rises and the affected graph is reevaluated.

## 9. The execution model

### 9.1 Two boundaries, not one

Merging one Work Item can leave the mainline holding a half-built capability. That is not a conflict between workflows. It is what happens when two boundaries are treated as one, and this model keeps them apart.

| Boundary  | What it is                                                                | Where it lives                                                    |
| --------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **Merge** | An integrable, independently verifiable change                            | Work Item                                                         |
| **Value** | One or more affected Capabilities implemented and evidenced in production | Coordinated by the Work Package; verified by external authorities |

**It cannot be otherwise, because git has no cross-repository branch.** A Work Package coordinates several repositories. No branch contains that. If the value boundary were a branch, the multi-repository model would be impossible, and that model is the reason the Work Package exists.

**The framework prescribes no branching model.** One invariant stands in place of the several a prescribed flow would need:

> **Every governed implementation change identifies the Work Item it realizes.**

GitFlow, GitHub flow, trunk-based development and feature branching can all satisfy it. The accepted verification contract chooses a durable mechanism without making one flow constitutional.

**The framework does not currently define an integration or activation strategy across repositories.** Git provides no atomic transaction across them, and feature flags, release manifests, environment switching and compatibility techniques establish different operational boundaries. Work Items reach their mainlines subject to their declared dependencies and repository gates; the Work Package coordinates the value boundary and is incomplete until all affected Capabilities are implemented and their verification conditions are satisfied by the declared external authorities. Whether partial implementation may be present in mainline or externally available is left open in [section 12](#12-open-questions).

That is the framework's own Outcome applied to itself. A merge is an output. _Verified capability operating in production_ is the result required.

### 9.2 Linking code to a Work Item

The authoritative realization claim is attached to immutable implementation history and identifies one existing Work Item. It must avoid circularity, survive the repository's integration strategy, remain forge-independent at the core and support deterministic indexing. The representation and verification Specifications define its concrete encoding.

The claim alone does not establish completion. A Work Item is realized only when the integrated implementation carrying that claim has been accepted against the Work Item and reached the mainline. Validation of that exact implementation subject is a separate evidence-backed fact. Neither fact is made true by writing it into the Work Item.

### 9.3 Forge independence

The core requires plain version-control history and immutable evidence, not a particular forge. A configured repository convention or forge may enrich coordination and review views, but losing that integration must not break identity, provenance or realization resolution.

### 9.4 Execution status and evidence

Work Package and Work Item carry exactly one explicit execution status for coordination, separate from artifact lifecycle. The representation Specification defines its vocabulary. Transition rules, authorities and preconditions belong to the verification Specification.

Execution status does not replace evidence. Realization comes from accepted implementation history, validation from its declared authority, and runtime verification from the authority observing the deployed subject. Generated views may correlate those facts with the declared coordination status and must expose disagreements rather than treating the status as proof.

### 9.5 Concurrency between agents

**One agent owns a Work Package.** It holds the whole graph the package depends on, so it is the only party that can decide what runs in parallel, and the dependencies it needs for that decision are already declared. Nothing inside a package is a race, because nothing inside a package is contended.

That collapses most of what a concurrency model would otherwise carry.

**A claim is a record, not a lock.** Under a branch-based convention the branch marks what is in flight so an interrupted run can be found again. Other flows may use a different record. There is no stranger to lock out inside the package, because the only agent working the package is the one that created it.

**`conflicts-with` feeds a planner, not a gate between rivals.** It tells the owning agent which of its own Work Items must not run at the same time, which is exactly the input a scheduler needs.

**Abandonment is recoverable when the configured flow preserves a terminal claim record.** An agent that dies may leave a stale claim without a realized implementation. Detecting that condition is flow-specific; what to do about it is policy, not model.

Real concurrency moves up one level, to two agents holding two Work Packages that touch the same code repository. Neither one can see the other's plan. That case is open, and [section 12](#12-open-questions) records it.

### 9.6 Merge verification boundary

_Mainline_ here means whatever branch the flow integrates into. Which branch that is belongs to the flow, not to this model.

The execution boundary must deterministically establish that every integrated implementation change resolves to an existing, live Work Item; changes stay within that Work Item's one target repository; declared conflicts and dependencies are respected; and realization of the exact integrated subject has accepted validation evidence from the declared authority.

The accepted verification Specification owns the concrete checks, evidence schema and integration mechanism. Judgment belongs to the validating authority, not to the gate: deterministic verification checks the identity, subject, verdict, authority and integrity of the evidence, but does not decide whether the implementation is correct.

The pull request is not a unit of this model. The immutable integrated implementation subject is. A forge may organize several commits and Work Items in one review without changing that boundary.

### 9.7 Cross-repository consistency

Git provides no atomic transaction across repositories, so the Work Package is where the state of a change spanning several of them becomes readable at all.

```text
SPEC-0017-WP-0001 realized by:
  web-app             @ commit AAA
  identity-service    @ commit BBB
  compliance-service  @ commit CCC
```

**That view is derived on read and never stored as evidence in an artifact.** It is harvested from realization claims across the registered code repositories. A Work Package's explicit execution status may summarize coordination, but it cannot replace or override this derived implementation view.

The Work Package reaches evidence-backed completion only when every required Work Item is realized and every external verification condition has a passing attestation bound to the exact deployed subject. It orchestrates the Work Items but verifies nothing itself. Its derived view correlates planned state from the Canon, integrated state from version-control history, deployment state from the deployment system, and immutable verification evidence from the declared runtime authorities.

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
| **PRINCIPLE-08** | Derived knowledge is generated, not maintained                                    | Evidence views are computed; explicit coordination status never substitutes for facts derived from authoritative history                                             |
| **PRINCIPLE-09** | A Work Item targets exactly one code repository                                   | Cross-repository coordination belongs to the Work Package                                                                                                            |
| **PRINCIPLE-10** | Work Item is the unit of implementation; Work Package is the unit of coordination | Replaces the Epic/Story mental model                                                                                                                                 |
| **PRINCIPLE-11** | Context flows downward; evidence flows upward                                     | Agents start from product context and descend; verification propagates back                                                                                          |
| **PRINCIPLE-12** | Canon and implementation must never knowingly disagree                            | Once judgment identifies a contradiction, Canon or implementation must be reconciled before promotion. Semantic agreement is not established by a deterministic gate |
| **PRINCIPLE-13** | Promotion is guarded by validators                                                | Specifications formalize deterministic gates within the semantic boundaries constituted here                                                                         |
| **PRINCIPLE-14** | Runtime closes the loop                                                           | Verified runtime evidence is part of the thread and feeds future Discovery                                                                                           |
| **PRINCIPLE-15** | Mess is allowed before promotion; known inconsistency is rejected at promotion    | Promotion is an acceptance boundary: structural consistency is gated, while semantic inconsistency is resolved under PRINCIPLE-12                                    |
| **PRINCIPLE-16** | A code repository holds no canonical artifacts                                    | Canon and code never sit in one tree, so neither can drift into the other                                                                                            |
| **PRINCIPLE-17** | Every HQ and Scope is constituted by exactly one root `charter.md`                | A directory without the Charter is not a Scope; only its `docs/specs/` and `docs/sources/` may hold Canon                                                            |

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
| Stacked pull requests                          | Phabricator, and the tools that followed. The original tool is archived                                                                                                                                                                        | Dependent Work Items                                                                                                       |
| Progressive disclosure                         | [OpenKnowledgeFormat, Google Cloud, 2026](https://github.com/GoogleCloudPlatform/open-knowledge-format)                                                                                                                                        | The generated navigation entry point and bounded context                                                                   |
| Ubiquitous language                            | Domain-Driven Design, Eric Evans, Addison-Wesley, 2003                                                                                                                                                                                         | Why the vocabulary is enforced rather than suggested                                                                       |
| Constitutional charter and delegated authority | Constitutional and federal governance traditions, with no single originating source                                                                                                                                                            | Why every jurisdiction carries one Charter while child membership and delegation derive from nesting and parent acceptance |

### 11.1 The relationship to OpenKnowledgeFormat

[OKF](https://github.com/GoogleCloudPlatform/open-knowledge-format) is the principal influence on Integral's inspectable knowledge representation and progressive disclosure. The Charter does not freeze an OKF version, serialization format or metadata field list; the accepted representation Specification records which substrate and conventions apply.

Integral retains two constitutional requirements that any substrate must support:

**Identity.** OKF makes the concept identifier the file's path. That is coherent for a corpus whose directory structure is, in OKF's own words, independent of the domain, so paths never move. It breaks at the operation this model is built around: an artifact moving between scopes when ownership changes.

**Relation typing.** OKF conveys the kind of relation in the surrounding prose and treats every link as an untyped directed edge. That suits a corpus that is read. This corpus is audited: it is asked _what broke_, not _what does this say_, and auditing requires knowing the nature of each connection without reading anything.

Neither is a flaw in OKF. They are the difference between a knowledge catalog and a traceability system.

## 12. Open questions

This document describes the agreed model and identifies the constitutional questions it deliberately leaves unresolved.

| Question                                               | Why it is unresolved                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **The judgment points**                                | Gates check form, never correctness. At the execution seam, judgment appears as immutable validation evidence and deterministic verification reads its form and verdict, not semantic truth. No equivalent judgment is yet defined for authorizing the transition from Design to a build-ready Work Package, including whether effective Constraints inherited from several Specifications are semantically compatible. Who or what may issue these judgments, what independence they require, and by what acceptance rule, remains unresolved |
| **Retrospective conformance**                          | A future exception may let a Decision adopt an existing integrated implementation without creating a Work Item or retroactive `follows`. The model requires an auditable fact binding the Decision, exact integrated subject, verdict, authority and time; its portable representation and attestation mechanism remain undefined                                                                                                                                                                                                              |
| **Distributed delegation**                             | Genesis, amendment and same-repository delegation are accepted git revisions, not parallel receipts. The portable authorization contract for a child Scope held in another repository remains unresolved                                                                                                                                                                                                                                                                                                                                       |
| **Trust is not binary**                                | A baseline is one number. It cannot distinguish an artifact a person reviewed yesterday from one an agent generated two years ago and nobody read                                                                                                                                                                                                                                                                                                                                                                                              |
| **Design-stage divergence**                            | Prototypes and vendor evaluations are not Decisions, and the model gives them no home. A vendor evaluation is also the record of what was rejected, which is expensive to lose                                                                                                                                                                                                                                                                                                                                                                 |
| **Two agents, two Work Packages, one code repository** | One agent per Work Package removed every collision inside a package and moved them up a level, where neither agent can see the other's plan                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Cross-repository integration strategy**              | Git provides no atomic transaction across repositories. Feature flags, release manifests, environment switching and compatibility techniques can coordinate activation, but the framework does not yet define a portable integration or activation contract                                                                                                                                                                                                                                                                                    |
| **Multi-HQ**                                           | The identifier grammar reserves the namespace. Nothing resolves across HQs                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Historical adoption**                                | A legacy estate must enter by reconstructing the historical graph from current implementation and surviving evidence, not by pretending every existing commit already followed the model. The ordering, confidence levels and minimum evidence required for that reconstruction remain to be defined                                                                                                                                                                                                                                           |

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

**Correction.** A Work Item is realized when an accepted integrated implementation carrying its realization claim reaches the mainline. A Work Package has evidence-backed completion only when every planned Work Item is realized and external authorities provide the required verification records. Its explicit execution status coordinates work but cannot prove those facts.

### A hotfix bypasses the lifecycle

**Symptom.** An urgent commit reaches the mainline with no Work Item because the incident was called a hotfix.

**Cause.** Urgency was treated as permission to enter at the line of code instead of at the lifecycle.

**Correction.** Integral has no bypass category called hotfix. Urgent work may compress Discovery and Design to the smallest honest Intent, Requirement and Work Item, but it still enters through the cycle and carries the same provenance. A future adoption process may reconstruct history for code that predates the framework; it does not authorize new unlinked code.

### A Constraint is written with no Intent above it

**Symptom.** A Specification collects rules nobody can trace to a purpose. Arguments about them cannot be settled, because there is nothing to settle them against.

**Cause.** A preference or an observation was filed as a Constraint.

**Correction.** Name the Intent the Constraint serves. If none exists, it is not a Constraint. A preference belongs in a Decision, which preserves what lost and why. An observation may belong in a Source, which records when the underlying material was consulted.

### An internal foundational document is automatically treated as a Source

**Symptom.** A risk policy, data-treatment policy or design system is copied into Source artifacts even when the same scope owns and may change its normative content. Conversely, a document written inside the company is rejected as a Source even though another authority governs it.

**Cause.** External was read as _outside the company_ instead of _outside the consuming decision boundary_.

**Correction.** Classify authority, not provenance. A separately governed policy is a Source to the work that consumes it, whether its authority is internal or external to the organization. A policy governed inside Integral is expressed through its own Specification, Constraints and Decisions. A founding document that constitutes the right to govern is a Charter, not evidence cited by the authority it creates.

### A Scope inherits a Charter instead of carrying one

**Symptom.** A directory is called a Scope and receives Canon even though no document defines its purpose, jurisdiction or authority. Its owner is inferred from an ancestor Charter.

**Cause.** Parent membership was confused with local constitution.

**Correction.** Every HQ and Scope carries exactly one root `charter.md`. Nesting derives the parent and the local Charter defines the child jurisdiction. Within one repository, the accepted git revision introducing that Charter records the parent's authorization; cross-repository delegation requires a portable authorization contract. Without a local Charter the directory is not a Scope and cannot own `docs/specs/` or `docs/sources/` Canon.

### The Canon root is treated as a generic documentation tree

**Symptom.** Paths such as `identity/docs/models/` appear, and an agent must read their contents to learn whether `models` is canonical, implementation material or exploration.

**Cause.** File format and familiar folder names were allowed to substitute for the ontology.

**Correction.** `docs/` is the reserved Canon root, not a catch-all. Canon exists only under its `specs/` and `sources/` collections; exploration belongs in `discovery/`; a new jurisdiction is a child directory with exactly one root `charter.md`; implementation remains in code repositories.

### One aggregate layout is treated as constitutional

**Symptom.** A change to file placement is treated as requiring a Charter amendment even though artifact meaning, identity, authority and membership remain unchanged.

**Cause.** One representation was confused with the semantic model it implements.

**Correction.** The Charter reserves the Canon boundary and collections; the accepted representation Specification owns artifact files and aggregate layout. Change that Specification when the representation changes, and amend the Charter only when a constitutional invariant changes.

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
├── discovery/                  ignored, non-canonical
├── docs/                        reserved Canon root
│   ├── index.md                 generated once Canon materializes
│   ├── specs/                   Specifications
│   └── sources/                 Sources
└── <child-scope>/
    ├── charter.md
    └── ...
```

`charter.md` makes the containing directory a Scope. Canon exists only below
that Scope's `docs/specs/` and `docs/sources/`; child Scope membership derives from
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

### The thirteen conceptual relations

```text
Derivation     based-on  specifies  respects  narrows  informed-by
               satisfies  implements  follows
Reference      references
Membership     part-of
Coordination   depends-on  conflicts-with
Lifecycle      supersedes
```

Their serialized names, direction and shape belong to the representation Specification.

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
A dependency belongs to the dependent; membership to the constituent.
Reverse navigation is derived. The identifier states origin.

The nearest containing charter.md identifies the Scope. Only that
Scope's docs/specs/ and docs/sources/ hold Canon.

WI part-of WP part-of SPEC@baseline resolves membership transitively.
Capability and Constraint membership is intrinsic to the Specification.

A relation type exists to answer one question: if the other end
changes, what happens to me?

Gates check that the graph is well formed. They never check that
it is right.

Mess is allowed before promotion. Inconsistency is not allowed after.

Knowledge that cannot be reached within a context budget does not
exist for whoever writes most of the code today.
```
