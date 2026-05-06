import pytest
from api.api_client import APIClient


@pytest.mark.api

def test_get_notes_api():
    """
    TC-08: Validate GET /notes returns expected structure and performance
    """
    api = APIClient()


    response = api.get_notes()

    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)

    # Performance
    assert response.elapsed.total_seconds() < 2


@pytest.mark.api
def test_delete_note_api():
    """
    TC-09: Validate DELETE /notes works independently
    """
    api = APIClient()

    response = api.get_notes()
    notes = response.json()["data"]

    assert len(notes) > 0, "No notes available to delete"

    note_id = notes[0]["id"]

    delete_response = api.delete_note(note_id)
    assert delete_response.status_code == 200

    # Verify deletion
    updated = api.get_notes().json()["data"]
    assert not any(n["id"] == note_id for n in updated), "Note not deleted"