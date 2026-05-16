---
name: Feature Request
about: Propose new user-facing functionality or a meaningful behavioral addition
title: "feat(scope): [Short description of the feature]"
labels: enhancement
assignees: ""
---

<!--
  BEFORE FILING: Check if this feature was already requested or is in progress.

  scope is the area being extended:
    search | indexer | api | frontend | upload | docker

  Use this template for new functionality that changes what the application
  can DO for a user — a new endpoint, a new UI element, a new behavior.

  If the code is broken, use Bug Report instead.
  If the code works but needs internal improvement with no user-facing change,
  use Technical Task instead.

  A good feature request explains the problem first, then proposes a solution.
  The best features come from real needs.
-->

## Problem

<!--
  Describe the problem or limitation this feature addresses.
  Start with "Currently..." to ground the reader in the present state.
  Do NOT describe the solution here — just the problem.
  One paragraph.

  When to delete: Never. The problem justifies the feature.
  Delete this comment and the example before submitting.
-->

> **Example:** Currently, uploaded documents are searchable but there is no way
> to view a list of all indexed documents or remove one. If a user uploads the
> wrong file, they have no way to delete it without resetting the entire index.

## Proposed Solution

<!--
  Describe what you want to happen. Be specific:
    - What new endpoint, UI element, or behavior would be added?
    - What inputs does it accept and what does it return?
    - What does it NOT do? (Define the scope boundary explicitly)

  When to delete: Never.
  Delete this comment and the example before submitting.
-->

> **Example:** Add a `DELETE /api/documents/{doc_id}` endpoint that removes a
> document from the inverted index and the metadata store. Returns `204 No Content`
> on success and `404` if the `doc_id` does not exist. It does not need to rebuild
> the index — just remove the document's postings and metadata entry.

## Acceptance Criteria

<!--
  A checklist that defines "done." The PR implementing this feature must satisfy
  every checkbox before it can be merged.
  Write from the user's or system's perspective: "User can...", "System returns..."

  This checklist is a starting point. The implementer may refine it when opening
  the PR if they discover edge cases during development.

  When to delete: Never. This is what "done" looks like.
  Delete this comment and the example before submitting.
-->

> **Example:**
> - [ ] `DELETE /api/documents/{doc_id}` returns `204 No Content` on success.
> - [ ] Returns `404 Not Found` if the `doc_id` does not exist.
> - [ ] Removes all postings for the document from the inverted index in memory.
> - [ ] Removes the document from `_doc_metadata` and `_doc_lengths`.
> - [ ] Persists the updated index to disk after deletion.
> - [ ] Unit tests cover the success path, the 404 path, and index persistence.

- [ ]
- [ ]
- [ ]

## Why This Matters

<!--
  One paragraph explaining why this feature is worth building.
  Who benefits? What becomes possible that was not possible before?
  This section helps prioritize features against each other when there are many.

  When to delete: Delete this section if the value is already self-evident
    from the Problem section and needs no further justification.
  Delete this comment and the example before submitting.
-->

> **Example:** Without document deletion, the search engine is append-only.
> During development this means a mis-uploaded test file pollutes every search
> session. Adding deletion completes the basic CRUD lifecycle and makes the
> system practically usable beyond the initial demo.

## Additional Context

<!--
  Relevant links, prior art, screenshots of similar features elsewhere, or
  technical constraints to be aware of. Delete if not needed.
-->
