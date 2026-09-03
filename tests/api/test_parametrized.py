import pytest
import requests


@pytest.mark.api
@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_find_by_status(api_base_url, status):
    r = requests.get(f"{api_base_url}/pet/findByStatus", params={"status": status})
    assert r.status_code == 200
    body = r.json()
    assert isinstance(body, list)
    for pet in body:
        assert pet.get("status") == status


@pytest.mark.api
@pytest.mark.parametrize("pet_id,allowed_statuses", [
    (0,                   [400, 404]),
    (-1,                  [400, 404]),
    # Shared public sandbox: anyone can create a pet under this id,
    # so an existing record is a valid outcome for the boundary check.
    (2_147_483_647,       [200, 404]),
    (999_999_999_999,     [400, 404, 500]),
])
def test_boundary_pet_ids(api_base_url, pet_id, allowed_statuses):
    r = requests.get(f"{api_base_url}/pet/{pet_id}")
    assert r.status_code in allowed_statuses, (
        f"ID {pet_id}: expected one of {allowed_statuses}, got {r.status_code}"
    )
