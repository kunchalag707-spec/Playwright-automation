# Playwright Python Automation

Page Object Model (POM) test suite using Playwright and pytest.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
playwright install
```

Copy `.env.example` to `.env` and set your app URL and credentials.

## Run tests

```bash
pytest
pytest tests/test_login.py
pytest -m smoke
pytest --headed --browser chromium
```

## Structure

- `tests/` — pytest specs
- `pages/` — page objects
- `utils/` — config, logger, test data
- `api/` — HTTP client for API checks
- `conftest.py` — shared fixtures
