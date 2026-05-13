---
name: Bug Report
about: Report something that is broken or behaving incorrectly
title: "fix: [Short description of the bug]"
labels: bug
assignees: ""
---

<!--
  BEFORE FILING: Search existing issues to check if this bug was already reported.
  Fill out every section below. Incomplete reports will be closed.
-->

## What Happened

<!--
  Describe the bug. One clear paragraph.
  Focus on observable behavior — what did you see that was wrong?
  Example: "When I upload a .txt file larger than 1MB, the server returns a 500
  error instead of a validation error message."
-->

> **Example:** When I upload a `.txt` file larger than 1MB through the upload form,
> the server returns a generic `500 Internal Server Error` instead of the expected
> `413 Request Too Large` message.

---

## What Was Expected

<!--
  Describe what *should* have happened if the bug did not exist.
-->

> **Example:** The server should return a `400` response with the message
> `{"error": "File exceeds the 5MB limit."}` so the frontend can display it to
> the user.

---

## Steps to Reproduce

<!--
  Numbered steps. Be specific. Another developer should be able to trigger
  the bug by following these steps exactly.
-->

> **Example:**
> 1. Start the backend: `docker compose up backend`
> 2. Prepare a `.txt` file larger than 1MB (e.g., Moby Dick from Project Gutenberg).
> 3. Upload it: `curl -X POST http://localhost:8000/api/documents -F "file=@moby_dick.txt"`
> 4. Observe the response — a `500` error is returned instead of a `400`.

1.
2.
3.

---

## Environment

<!--
  Fill in your environment details. These help identify platform-specific bugs.
-->

- **OS:** [e.g., macOS 14, Windows 11, Ubuntu 24.04]
- **Python version:** [e.g., 3.12.3]
- **Docker version:** [e.g., 26.1.1]
- **Browser (if frontend bug):** [e.g., Chrome 124]

---

## Error Output

<!--
  Paste any error messages, stack traces, or logs here.
  Use a code block (triple backticks) for terminal output.
-->

Paste error output here

---

## Additional Context

<!--
  Anything else that might help: screenshots, links to related issues,
  attempts you already made to fix it. Delete this section if not needed.
-->

