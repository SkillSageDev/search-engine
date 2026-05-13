<!-- .github/PULL_REQUEST_TEMPLATE.md -->

<!--
  PR TITLE FORMAT: type(scope): Short imperative summary — no period at the end
  
  Examples:
    feat(api): Add POST /api/documents endpoint for file upload
    fix(indexer): Prevent zero-division on empty document tokens
    chore: Add .gitignore and .dockerignore
    ci: Add GitHub Actions linting and test pipeline

  Use the imperative present tense: "Add" not "Added", "Fix" not "Fixed".
  Capitalize the first letter after the colon. Keep it under 72 characters.
-->

## Summary

<!--
  2–4 sentences. Answer: What does this PR do and why is it needed?
  Use present tense: "This PR adds...", "This PR fixes..."
  Explain the VALUE, not just the action. Think: what problem does this solve?
  Delete this comment and the example before submitting.
-->

> **Example:**
> This PR implements the document ingestion pipeline, allowing users to upload
> `.txt` files through the API and have them indexed immediately. The inverted
> index is updated in memory and persisted to disk after each upload, ensuring
> documents survive server restarts.

---

## Changes Made

<!--
  Bullet list of specific, concrete changes. Use past tense: "Added", "Fixed".
  Each bullet = one file or one logical action. Be specific about file paths.
  Aim for 3–8 bullets. More than 8 bullets means the PR should be split.
  Delete this comment and the example before submitting.
-->

> **Example:**
> - Added `backend/app/api/routes/documents.py` with `POST /api/documents` handler.
> - Implemented file type validation — rejects non-`.txt` uploads with a `400` response.
> - Generated `UUID4` as `doc_id` server-side to prevent collisions.
> - Called `InvertedIndex.add_document()` to tokenize and index uploaded file content.
> - Wrote unit tests in `backend/tests/test_api.py` covering upload, rejection, and response shape.

-

---

## How to Test

<!--
  Numbered steps. Order matters — use numbered list, not bullets.
  Each step starts with an imperative verb: "Run", "Open", "Upload", "Verify".
  Specific enough that someone who has never seen the code can follow them.
  Delete this comment and the example before submitting.
-->

> **Example:**
> 1. Start the backend: `docker compose up backend`
> 2. Upload a sample document:
>    ```
>    curl -X POST http://localhost:8000/api/documents \
>      -F "file=@data/sample_docs/frankenstein.txt"
>    ```
> 3. Verify the response contains `doc_id` and `term_count`.
> 4. Search for a term: `GET /api/search?q=monster`
> 5. Confirm the uploaded document appears in results with a relevance score.

1.

---

## Screenshots

<!--
  Required if ANY page, component, or UI element changed visually.
  Add a before/after pair if you modified existing UI.
  If no UI changed, write: "N/A — [brief reason why]"
  Delete this comment and the example before submitting.
-->

> **Example (no UI change):** N/A — this PR modifies backend logic only.
>
> **Example (with UI change):** Before and after adding the result score badge:
> [before screenshot] → [after screenshot]

---

## Breaking Changes

<!--
  List anything that changes existing behavior that other code depends on.
  If the API response shape changes, mention it. If a route is renamed, mention it.
  If nothing breaks, write: "None."
  Delete this comment and the example before submitting.
-->

> **Example (breaking):** The `/api/search` response now returns `results` instead of
> `data`. Any client that reads `response.data` will receive `undefined`.
>
> **Example (none):** None.

---

## Related Issues

<!--
  Link the GitHub issue this PR resolves using "Closes #N" syntax.
  GitHub automatically closes the issue when the PR is merged.
  
  If there is no related issue (small chores, housekeeping):
  → Write: "No related issue. [One sentence explaining why no issue was needed.]"
  → Or: Delete this entire section.
  
  Never write "Closes N/A" or leave it blank. Both look accidental.
  Delete this comment and the example before submitting.
-->

> **Example (with issue):** Closes #5
>
> **Example (no issue):** No related issue. This is a housekeeping task that does
> not require prior discussion or feature scoping.

---

## Checklist

<!--
  Check every box that applies before requesting a review.
  Unchecked boxes are fine — they signal to the reviewer what is still pending.
  Delete items that genuinely do not apply (e.g., "Screenshots" for a backend-only PR).
-->

- [ ] PR title follows the format: `type(scope): Short imperative summary`
- [ ] Code follows project style (BEM for CSS, type hints and docstrings for Python)
- [ ] Tests added or updated for all new behavior
- [ ] All existing tests pass locally: `pytest backend/tests/`
- [ ] `docker compose up` runs without errors
- [ ] No `.env`, credentials, or secrets are included in this PR
- [ ] The example text in each section has been deleted from this body
