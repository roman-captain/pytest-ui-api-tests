import json
import random
import pytest
import requests
from pathlib import Path

PETSTORE_URL = "https://petstore.swagger.io/v2"


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "base_url": "https://github.com",
        "viewport": {"width": 1280, "height": 800},
    }


@pytest.fixture(scope="session")
def api_base_url():
    return PETSTORE_URL


@pytest.fixture(scope="session")
def pet_schema():
    return json.loads((Path(__file__).parent / "schemas/pet_schema.json").read_text())


@pytest.fixture
def created_pet(api_base_url):
    pet_id = random.randint(10_000_000, 99_999_999)
    payload = {"id": pet_id, "name": "PyDog", "status": "available"}
    r = requests.post(f"{api_base_url}/pet", json=payload)
    assert r.status_code == 200
    yield pet_id
    cleanup = requests.delete(f"{api_base_url}/pet/{pet_id}")
    assert cleanup.status_code in [200, 404]
