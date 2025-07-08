# 🧪 Software Testing – Essentials & Best Practices

This note summarizes key software testing concepts relevant for practical coding and software development interviews.

---

## 🧠 1. Why Testing Matters

- Ensures **correctness** and **reliability**
- Catches **bugs** early → saves time & cost
- Required for CI/CD pipelines and production-grade systems

---

## 🧾 2. Types of Testing

| Type             | Scope                       | Examples                 |
|------------------|-----------------------------|--------------------------|
| Unit Testing     | Test individual functions   | `assertEqual()`, mocks  |
| Integration Test | Test interaction between modules | DB, API calls          |
| Functional Test  | Test overall behavior       | End-to-end flows         |
| Regression Test  | Recheck after changes       | Legacy features          |
| Edge/Boundary    | Test under extreme inputs   | Overflow, empty values   |

---

## 🔧 3. Tools & Frameworks

| Language   | Frameworks                  |
|------------|-----------------------------|
| Python     | `unittest`, `pytest`        |
| Java       | `JUnit`, `TestNG`           |
| JavaScript | `Jest`, `Mocha`, `Cypress`  |
| C++        | `GoogleTest`, `Catch2`      |

```python
# Example: Python unit test
import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
```

## 🧪 4. Best Practices

🧩 Test small, isolated units (pure functions easiest to test)

✅ Use descriptive test names (test_invalid_login_fails)

🔁 Automate wherever possible

🔍 Don’t test only the “happy path”

🧱 Set up mocks/fakes for external services (e.g., DB, API)

## 💡 HackerRank & Interviews

- Expect to explain test cases (e.g., edge cases)

- Mention testing when designing systems or writing functions

- Bonus: Write simple unit test if allowed in coding test

## 📌 Final Tips

- Always write testable code (pure functions, clear I/O)

- Consider coverage, but prioritize meaningful tests

- Testing = Communication: Show that you care about quality
