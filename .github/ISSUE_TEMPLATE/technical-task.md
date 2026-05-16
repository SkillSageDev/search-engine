---
name: Technical Task
about: Refactoring, code quality, exception handling, or internal engineering work with no direct user-facing change
title: "type(scope): [Short description of the task]"
labels: technical-task
assignees: ""
---

<!--
  type is one of: refactor | chore | test | ci | perf | docs
  scope is the module or area being changed:
    scripts | ir | api | frontend | docker | ci | github

  Use this template for internal engineering work:
    - Adding exception handling to an existing module
    - Restructuring code without changing external behavior
    - Improving test coverage for existing logic
    - Adding type hints or docstrings to existing functions
    - Moving code between files (extract module, split class)
    - Updating dependencies or build configuration
    - Improving developer tooling (Makefile, CI steps, templates)

  If something is BROKEN and visible to users, use Bug Report instead.
  If you are adding new user-facing functionality, use Feature Request instead.

  The key distinction: does this change what the application CAN DO for a user?
    Yes -> Feature Request
    No, but it was broken -> Bug Report
    No, and it worked fine -> Technical Task
-->

## What and Why

<!--
  One paragraph. Answer two questions only:
    1. What is the current state of the code that needs to change?
    2. Why does it need to change? (reliability, readability, testability, consistency)

  Do NOT describe the solution here. Describe the problem with the current state.
  A reviewer reading this should understand the motivation before seeing the fix.

  When to delete: Never. This is the foundation of the task.
  Delete this comment and the example before submitting.
-->

> **Example:** `scripts/fetch_corpus.py` has no request timeout and catches no
> specific exceptions. A hung server makes the script hang indefinitely with no
> feedback or exit path, and a single failed book download crashes the entire
> run with a raw Python traceback instead of a clean error message and summary.

## Proposed Changes

<!--
  Describe specifically what will change. Name the files and the behaviors.
  This is not a full implementation plan — just enough for a reviewer to
  understand the scope and verify that the right things were changed.
  Use past tense as if describing completed work: "Added", "Replaced", "Moved".

  When to delete: Never.
  Delete this comment and the example before submitting.
-->

> **Example:**
> - Added `timeout=30` to all `httpx` requests in `scripts/fetch_corpus.py`.
> - Wrapped each book download in a per-book `try/except` block so one failure
>   does not abort the remaining downloads.
> - Replaced `if response.status_code == 200` checks with `raise_for_status()`
>   to catch all 4xx and 5xx responses, not just non-200.
> - Added explicit `encoding="utf-8"` to `write_text()` to prevent crashes on
>   Windows where the system default encoding is `cp1252`.
> - Added a summary table at the end: downloaded / skipped / failed counts.
> - Script now exits with code `1` if any download failed, `0` on full success.

## Acceptance Criteria

<!--
  What must be true for this task to be considered complete?
  Write from the perspective of a reviewer checking the PR.

  This checklist is a starting point. The implementer may add or adjust items
  when opening the PR if edge cases emerge during development.

  When to delete: Never. This defines "done."
  Delete this comment and the example before submitting.
-->

> **Example:**
> - [ ] Script runs without error on Linux, macOS, and Windows.
> - [ ] A single failed download does not abort the rest — the loop continues.
> - [ ] Script exits with code `1` when any book failed, `0` when all succeed.
> - [ ] All HTTP requests have an explicit `timeout=30`.
> - [ ] `encoding="utf-8"` is specified on every file write.
> - [ ] All constants are `UPPER_SNAKE_CASE` per PEP 8.
> - [ ] All functions have type hints and docstrings.
> - [ ] No existing behavior visible to users changes.

- [ ]
- [ ]
- [ ]

## Does This Change Any External Behavior?

<!--
  Answer yes or no, then explain in one sentence.

  External behavior means: API response shape, CLI arguments, file formats,
  config key names, environment variable names — anything another system or
  user depends on.

  "No." with a period signals you checked and confirmed. It is not the same
  as leaving this blank.

  When to delete: Never. This forces you to think about impact before coding.
  Delete this comment and the examples before submitting.
-->

> **Example (no):** No. The script produces the same output files in the same
> location. Error handling is internal — only exit codes change.
>
> **Example (yes):** Yes. The `index.json` format gains a `version` key.
> Existing index files without this key will be re-indexed on next startup.

## Additional Context

<!--
  Links to related code, prior discussions, or relevant documentation.
  Delete this section if you have nothing to add.
-->
