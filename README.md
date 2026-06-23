# pytest-ui-api-tests

Full-stack test suite built with **pytest** + **Playwright** (UI) + **requests** (API).

---

## Stack

| Layer | Tool |
|-------|------|
| Test runner | pytest |
| UI automation | playwright-python (sync API) |
| API client | requests |
| Schema validation | jsonschema |
| Keyword-driven tests | Robot Framework + RequestsLibrary |
| CI | GitHub Actions (push + daily cron) |

---

## Structure

```
pytest-ui-api-tests/
├── conftest.py          # fixtures: browser config, API base URL, pet schema, created_pet
├── pytest.ini           # markers: api, ui, smoke
├── requirements.txt
├── schemas/
│   └── pet_schema.json  # JSON Schema for contract testing
├── robot/
│   └── petstore_api.robot  # Robot Framework: keyword-driven API tests (CRUD)
└── tests/
    ├── api/
    │   ├── test_pet_crud.py       # POST / GET / PUT with schema validation
    │   └── test_parametrized.py   # @parametrize: status values + boundary IDs
    └── ui/
        └── test_github_nav.py     # GitHub navigation: Sign in, Pricing, Sign up
```

---

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

---

## Run

```bash
# All tests
pytest -v

# API only
pytest -m api -v

# UI only
pytest -m ui -v

# Robot Framework
robot robot/petstore_api.robot
```

---

## Key concepts demonstrated

- **Fixtures with scope**: `session` for shared resources, `function` for per-test setup/teardown
- **Yield fixtures**: setup + teardown in one function (`created_pet` creates and deletes the pet)
- **Random IDs**: avoids collisions in parallel CI runs
- **jsonschema validation**: contract testing (validates types + required fields + enum values)
- **Boundary Value Testing**: edge case IDs: `0`, `-1`, `int32 MAX`, `int64 overflow`
- **get_by_role()**: accessibility-aware locators, stable against DOM changes
- **Robot Framework**: keyword-driven syntax — tests readable by non-technical stakeholders; `*** Settings ***`, `*** Variables ***`, `*** Test Cases ***` sections; runs independently from pytest
