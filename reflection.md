# Lab 5: Static Code Analysis — Issues, Fixes, and Reflection

## 📋 Identified Issues and Fixes

| *Issue Type* | *Line(s)* | *Description* | *Fix Approach* |
|----------------|--------------|-----------------|------------------|
| Mutable default argument | 7 | logs=[] is a shared mutable default; leads to unexpected behavior between calls. | Change default to None and initialize within function. |
| Bare except | 18 | Catches all exceptions silently, hides real errors. | Catch specific exceptions (e.g., KeyError, TypeError) or log them properly. |
| Dangerous use of eval | 58 | eval() executes arbitrary code, creating a severe security risk. | Remove eval; use safer alternatives (e.g., logging, function calls). |
| File not opened using with | 25, 31 | Manual open/close without context manager; may leak resources. | Use with open(...) as f: pattern. |
| No encoding specified in open() | 25, 31 | Could cause encoding issues on some systems. | Specify encoding="utf-8". |
| Naming convention | Several | Functions like addItem, removeItem, etc. are not in snake_case. | Rename to add_item, remove_item, etc. |
| Missing docstrings | Many | No function/module documentation. | Add concise docstrings for readability and maintainability. |
| Unused import | 2 | logging imported but never used. | Remove or properly implement logging. |

---

## ✅ Summary of Fixes

- Removed unsafe eval() call.
- Fixed mutable default argument (logs=[] → None).
- Replaced bare except with specific exception handling.
- Used with open(...) context managers for file I/O.
- Added UTF-8 encoding specification.
- Renamed functions to follow snake_case style.
- Added docstrings for all functions and the module.
- Removed unused logging import.
- Used f-strings for clean, modern string formatting.

---

## 💬 Reflection

### 1. Which issues were easiest and hardest to fix?
- *Easiest:* Adding docstrings and renaming functions to match PEP 8 conventions — mechanical but improved readability.
- *Hardest:* Fixing the mutable default argument and removing eval() — required understanding potential runtime and security issues.

### 2. Were there any false positives?
- Pylint flagged “unused import logging,” which was valid since logging wasn’t yet implemented. However, if future enhancements add logging, that warning could be safely ignored.

### 3. How would you integrate static analysis into a workflow?
- Integrate *Pylint, **Flake8, and **Bandit* into CI/CD pipelines.
- Add pre-commit hooks to prevent committing code that fails static checks.
- Run static analysis locally before each commit to ensure continuous quality enforcement.

### 4. Improvements after applying fixes
- Code now adheres to PEP 8, making it easier to read and maintain.
- File handling is more reliable with context managers and explicit encoding.
- Removed a critical security vulnerability (eval()).
- Increased clarity through type hints and docstrings.
- Overall, the code is cleaner, safer, and easier to extend in future.

---

*Author:* Sai Amarnath G (PES1UG23AM255)  
*Date:* 2025-10-16  
*Course:* Lab 5 — Static Code Analysis