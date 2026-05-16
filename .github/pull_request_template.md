<!-- .github/PULL_REQUEST_TEMPLATE.md -->

<!--
  PR TITLE FORMAT: type(scope): Short imperative summary

  type:  feat | fix | refactor | chore | test | docs | ci | perf
  scope: the module changed — scripts | ir | api | frontend | docker | ci

  Rules:
    - Use the imperative present tense: "Add" not "Added", "Fix" not "Fixed"
    - Capitalize the first letter after the colon
    - No period at the end of the title
    - Keep it under 72 characters

  Examples:
    feat(api): Add POST /api/documents endpoint for file upload
    fix(scripts): Prevent Windows encoding crash in fetch_corpus.py
    refactor(ir): Extract preprocessing logic into separate module
    chore: Add .gitignore and .dockerignore
    ci: Add GitHub Actions linting and test pipeline
-->

## Summary

<!--
  2-4 sentences. Answer: What does this PR do and why is it needed?
  Use present tense: "This PR adds...", "This PR fixes..."
  Explain the VALUE, not just the action — what problem does this solve?

  When to delete: Never. Every PR needs a summary.
  Delete this comment and the example before submitting.
-->

> **Example:**
> This PR implements the document ingestion pipeline, allowing users to upload
> `.txt` files through the API and have them indexed immediately. The inverted
> index is updated in memory and persisted to disk after each upload, ensuring
> documents survive server restarts.

## Changes Made

<!--
  Bullet list of specific, concrete changes. Use past tense: "Added", "Fixed".
  Each bullet = one file or one logical action. Include the file path.
  Aim for 3-8 bullets. More than 8 usually means the PR should be split.

  When to delete: Never. Always list what changed.
  Delete this comment and the example before submitting.
-->

> **Example:**
> - Added `backend/app/api/routes/documents.py` with `POST /api/documents` handler.
> - Implemented file type validation — rejects non-`.txt` uploads with a `400`.
> - Generated `UUID4` as `doc_id` server-side to prevent collisions.
> - Called `InvertedIndex.add_document()` to tokenize and index the uploaded file.
> - Wrote unit tests in `backend/tests/test_api.py` covering upload, rejection,
>   and response shape.

-

## How to Test

<!--
  Numbered steps. Order matters — use a numbered list, not bullets.
  Each step starts with an imperative verb: "Run", "Open", "Upload", "Verify".
  Specific enough that someone who has never seen this code can follow them.

  When to delete: Never. Always explain how to verify the change.
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
> 4. Search for a term from the document: `GET /api/search?q=monster`
> 5. Confirm the uploaded document appears in results with a relevance score.
> 6. Restart the backend and repeat step 4 to verify the document persists.

1.

## Screenshots

<!--
  Required if ANY visible page, component, or UI element changed visually.
  Add a before/after pair if you modified existing UI.

  When no UI changed: write "N/A - [one sentence reason why]"
  When to delete: Delete this section for backend-only PRs where N/A is
    completely obvious (e.g., a pure IR engine change with no possible UI impact).
    If there is any ambiguity, keep it and write N/A with the reason.
  Delete this comment and the example before submitting.
-->

> **Example (no UI change):** N/A - this PR modifies backend indexing logic only.
>
> **Example (with UI change):** Before and after adding the relevance score badge:
>
> Before: [screenshot] | After: [screenshot]

## Breaking Changes

<!--
  Does this PR change any existing behavior that another system or user depends on?
  This includes: API response shape, route paths, config key names, file formats,
  CLI arguments, or environment variable names.

  "None." with a period signals you checked and confirmed there are no breaking
  changes — it is not the same as leaving this blank.
  If something breaks: describe exactly what changes and who is affected.

  When to delete: Never. "None." is a valid and useful answer.
  Delete this comment and the example before submitting.
-->

> **Example (none):** None.
>
> **Example (breaking):** The `/api/search` response now returns `results` instead
> of `data`. Any client reading `response.data` will receive `undefined`.

## Related Issues

<!--
  Link the GitHub issue this PR resolves. GitHub closes it automatically on merge
  when you use "Closes #N" syntax.

  If there is no related issue: write one sentence explaining why no issue was
  needed, then delete the "Closes #" line. Small housekeeping tasks with no
  prior discussion or scoping do not always require an issue.

  Never write "Closes N/A" — it looks accidental.
  When to delete: Only if this has no issue AND the reason is explained inline.
  Delete this comment and the example before submitting.
-->

> **Example (with issue):** Closes #5
>
> **Example (no issue):** No related issue. This is a one-line housekeeping fix
> that did not require prior scoping or discussion.

Closes #

## Checklist

<!--
  This checklist is a guide, not a law.

  Before submitting:
    - Check every box that is complete and applies to this PR.
    - DELETE items that genuinely do not apply to this type of change.
      A docs-only PR has no Docker impact. A template update has no tests.
    - Do not leave inapplicable items unchecked — it looks like unfinished work.
    - Strikethrough with a reason is better than silent deletion when the
      reason is non-obvious:
      ~~Tests added~~ - developer utility, not application logic
-->

- [ ] PR title follows `type(scope): Short imperative summary`
- [ ] Code follows project style (BEM for CSS, type hints and docstrings for Python)
- [ ] Tests added or updated for all new behavior
- [ ] All existing tests pass locally: `pytest backend/tests/`
- [ ] `docker compose up` runs without errors
- [ ] No `.env`, credentials, or secrets are included in this PR
- [ ] The example text in each section has been deleted from this body
