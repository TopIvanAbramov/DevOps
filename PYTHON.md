### **Python best practices**

- Use .gitignore to skip unnecessary files
- Use prod ready [Flask](https://flask.palletsprojects.com/en/2.0.x/) framework
- Describe all dependencies in requirements.txt file
- Use linter for code optimization ([Pylinter](https://pypi.org/project/pylint/))
- Containerize app for easier deployment
- Allow app configuration using environment variables

### **Unit test best practices**

- Use prod ready [Pytest](https://docs.pytest.org/en/6.2.x/) framework to write unit tests
- Tests should be fast, simple and deterministic
- Separate tests from implementation code
- Use TDD approach
- Increase test coverage
- Use naming conventions for every test
- Encapsulate unit tests in CI flow