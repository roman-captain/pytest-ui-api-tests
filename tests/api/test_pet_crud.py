import time

import jsonschema
import pytest
import requests


@pytest.mark.api
class TestPetCRUD:

    def test_create_pet(self, api_base_url, created_pet):
        assert isinstance(created_pet, int)

    def test_get_pet_schema(self, api_base_url, created_pet, pet_schema):
        r = requests.get(f"{api_base_url}/pet/{created_pet}")
        assert r.status_code == 200
        jsonschema.validate(instance=r.json(), schema=pet_schema)

    def test_get_pet_response_time(self, api_base_url, created_pet):
        start = time.time()
        r = requests.get(f"{api_base_url}/pet/{created_pet}")
        elapsed = time.time() - start
        assert r.status_code == 200
        assert elapsed < 3.0, f"Too slow: {elapsed:.2f}s"

    def test_update_pet_status(self, api_base_url, created_pet):
        payload = {"id": created_pet, "name": "PyDog", "status": "sold"}
        r = requests.put(f"{api_base_url}/pet", json=payload)
        assert r.status_code == 200
        assert r.json()["status"] == "sold"
