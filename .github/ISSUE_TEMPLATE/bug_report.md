---
name: Bug Report
about: Report something that is broken or behaving incorrectly
title: "fix(scope): [Short description of the bug]"
labels: bug
assignees: ""
---

<!--
  BEFORE FILING: Search existing issues to check if this bug was already reported.

  scope is the area where the bug lives:
    scripts | ir | api | frontend | docker | ci

  Use this template when something is BROKEN or behaving INCORRECTLY.
  If the code works but needs improvement, use Technical Task instead.
  If you want a new capability, use Feature Request instead.

  Fill out every section below. Incomplete reports may be closed.
-->

## What Happened

<!--
  Describe the bug in one clear paragraph.
  Focus on observable behavior: what did you see that was wrong?
  Include the exact error message if there is one.

  When to delete: Never. This is the core of a bug report.
  Delete this comment and the example before submitting.
-->

> **Example:** When running `python scripts/fetch_corpus.py` on Windows, the
> script crashes with `UnicodeEncodeError: 'charmap' codec can't encode character`
> after downloading the first book. On Linux the same command completes successfully.

## What Was Expected

<!--
  Describe what should have happened if the bug did not exist.
  One or two sentences is enough.

  When to delete: Never.
  Delete this comment and the example before submitting.
-->

> **Example:** All 11 books should download successfully and be saved to
> `data/sample_docs/` regardless of the operating system.

## Steps to Reproduce

<!--
  Numbered steps. Be exact. Another developer should be able to trigger
  this bug by following these steps on a fresh clone of the repo.
  Include the exact commands, inputs, file names, and OS if relevant.

  When to delete: Never.
  Delete this comment and the example before submitting.
-->

> **Example:**
> 1. Clone the repo on a Windows machine.
> 2. Install dependencies: `pip install -r backend/requirements.txt`
> 3. Run: `python scripts/fetch_corpus.py`
> 4. Observe the `UnicodeEncodeError` after the first book downloads.

1.
2.
3.

## Error Output

<!--
  Paste the exact error message, stack trace, or terminal output here.
  Copy it exactly — do not paraphrase an error message.

  When to delete: Delete this section only if the bug produces no error output
    (e.g., a silent wrong result like incorrect search rankings).
  Delete this comment and the example before submitting.
-->

> **Example:**
> ```
> UnicodeEncodeError: 'charmap' codec can't encode character '\u2014'
> in position 4218: character maps to <undefined>
> ```

```
paste error output here
```

## Environment

<!--
  Fill in what is relevant to this bug. Delete lines that are not.
  Platform-specific bugs (like this encoding issue) need the OS.
  Frontend bugs need the browser.
-->

- **OS:** [e.g., Windows 11, macOS 14, Ubuntu 24.04]
- **Python version:** [e.g., 3.12.3]
- **Docker version:** [e.g., 26.1.1] *(delete if not relevant)*
- **Browser:** [e.g., Chrome 124] *(delete if not a frontend bug)*

## Additional Context

<!--
  Anything else that helps: screenshots, links to related issues, things you
  already tried. Delete this section if you have nothing to add.
-->
