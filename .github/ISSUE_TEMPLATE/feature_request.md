---
name: Feature Request
about: Propose a new feature or improvement to the search engine
title: "feat: [Short description of the feature]"
labels: enhancement
assignees: ""
---

<!--
  BEFORE FILING: Check if this feature was already requested or is in progress.
  A good feature request explains the problem first, then proposes a solution.
  The best features come from real needs — describe the problem you are solving.
-->

## Problem

<!--
  Describe the problem or limitation this feature addresses.
  Start with "Currently..." to ground the reader in the current state.
  Do NOT describe the solution here — just the problem.
-->

> **Example:** Currently, uploaded documents are searchable but there is no way
> to view a list of all indexed documents or remove one. If a user uploads the
> wrong file, they have no way to delete it except by resetting the entire index.

---

## Proposed Solution

<!--
  Describe what you want to happen. Be specific about:
  - What new endpoint, UI element, or behavior would be added
  - What inputs it accepts and what outputs it produces
  - What it does NOT do (scope boundaries)
-->

> **Example:** Add a `DELETE /api/documents/{doc_id}` endpoint that removes a
> document from both the inverted index and the document metadata store. The
> endpoint should return `204 No Content` on success and `404` if the doc_id
> does not exist. It does not need to compress or rebuild the index — just remove
> the document's postings.

---

## Acceptance Criteria

<!--
  A checklist that defines "done." The PR that implements this feature must
  satisfy every checkbox before it can be merged.
  Write these from the user's perspective: "User can...", "System returns..."
-->

> **Example:**
> - [ ] `DELETE /api/documents/{doc_id}` returns `204 No Content` on success.
> - [ ] Returns `404 Not Found` if the `doc_id` does not exist.
> - [ ] Removes all postings for the document from the inverted index.
> - [ ] Removes the document's entry from `_doc_metadata` and `_doc_lengths`.
> - [ ] Persists the updated index to disk after deletion.
> - [ ] Unit tests cover the success path, the 404 path, and persistence.

- [ ]
- [ ]
- [ ]

---

## Why This Matters

<!--
  One paragraph explaining why this feature is worth building.
  Who benefits? What becomes possible that wasn't before?
  This helps prioritize features against each other.
-->

> **Example:** Without document deletion, the search engine is effectively append-only.
> This becomes a problem during development (testing with sample files) and would
> be a blocker for any real user who uploads the wrong document. Adding deletion
> completes the basic CRUD lifecycle and makes the system practically usable.

---

## Additional Context

<!--
  Relevant links, prior art, screenshots of similar features elsewhere,
  or technical constraints to be aware of. Delete if not needed.
-->
