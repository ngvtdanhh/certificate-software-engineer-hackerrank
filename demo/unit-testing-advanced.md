# 🧪 Advanced Unit Testing in Python – HackerRank Style

This demo covers **realistic unit testing patterns** used in technical interviews and backend applications. It includes:

- ✅ Isolated test cases
- 🧪 Edge case handling
- 🧱 Mocking external APIs
- 🧠 Reasoning about failures and test coverage

---

## 📘 Case Study: `auth_service.py`

We want to test this authentication logic:

```python
# auth_service.py
def authenticate(username, password, user_db):
    if username not in user_db:
        return "User not found"
    if user_db[username]["locked"]:
        return "Account locked"
    if user_db[username]["password"] != password:
        return "Invalid credentials"
    return "Login success"
```

## 🔍 Test Plan

| Test Case ID | Description         | Input                  | Expected Output       |
| ------------ | ------------------- | ---------------------- | --------------------- |
| TC01         | Valid credentials   | user, correct password | "Login success"       |
| TC02         | User does not exist | unknown\_user          | "User not found"      |
| TC03         | Locked account      | user, any password     | "Account locked"      |
| TC04         | Incorrect password  | user, wrong password   | "Invalid credentials" |

🧪 Test Implementation with unittest

```python
# test_auth_service.py
import unittest
from auth_service import authenticate

class TestAuthService(unittest.TestCase):
    def setUp(self):
        self.user_db = {
            "alice": {"password": "pass123", "locked": False},
            "bob": {"password": "qwerty", "locked": True}
        }

    def test_valid_credentials(self):
        result = authenticate("alice", "pass123", self.user_db)
        self.assertEqual(result, "Login success")

    def test_user_not_found(self):
        result = authenticate("charlie", "pass123", self.user_db)
        self.assertEqual(result, "User not found")

    def test_account_locked(self):
        result = authenticate("bob", "qwerty", self.user_db)
        self.assertEqual(result, "Account locked")

    def test_invalid_password(self):
        result = authenticate("alice", "wrongpass", self.user_db)
        self.assertEqual(result, "Invalid credentials")

if __name__ == '__main__':
    unittest.main()
```

## 📌 Extra: Mocking External API Calls

If your function uses requests.get(), use unittest.mock:

```pythom
@patch('auth.requests.get')
def test_external_user_validation(self, mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"valid": True}
```

## 🔧 Run the Tests

```pythom
python3 -m unittest test_auth_service.py
```

## 📈 Final Notes

- Treat test design like coding – clear structure, naming, and logic

- Use setUp() for reusable objects

- Use mocks to isolate dependencies (DBs, APIs)

- Tests are part of your codebase, not an afterthought

