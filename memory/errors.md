# Errors

Command failures and integration errors.

---

## ERR-20260502 edit tool × Chinese UTF-8

**When**: 2026-05-02, during hct-0211 wiki ingest
**Tool**: `edit` (file editing tool)
**Symptom**: "Could not find edits[n] in file. The oldText must match exactly..."

**Root cause**: The `edit` tool's string matching fails on Chinese/UTF-8 multibyte characters. Even exact copies of the same text from the file won't match.

**Fix**: Use Python script via `exec` for all Chinese-content file modifications:
```bash
python3 << 'PYEOF'
with open('file.md', 'r') as f: c = f.read()
c = c.replace('old', 'new')
with open('file.md', 'w') as f: f.write(c)
PYEOF
```

**Rule**: Never use `edit` on files containing Chinese. First attempt with Python.

---
