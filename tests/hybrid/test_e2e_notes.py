import pytest
from pages.notes_page import NotesPage
from api.api_client import APIClient
import time


# =========================
# TS-13: UI → API CONSISTENCY
# =========================
@pytest.mark.ui
def test_ui_to_api_consistency(logged_in_user):
    """
    TC-13: Validate note created via UI appears correctly in API
    """

    driver = logged_in_user #store the driver instance from the fixture
    notes = NotesPage(driver)  

    api = APIClient()
    

    # Unique data
    title = f"UI_API_{int(time.time())}"
    description = "This is UI to API validation"
    category = "Work"

    # Step 1: Create via UI
    notes.create_note(title, description, category)

    # Step 2: Fetch via API
    response = api.get_notes()
    assert response.status_code == 200

    data = response.json()["data"]   #gets notes list

    # Step 3: Validate
    matched_note = next((n for n in data if n["title"] == title), None)

    assert matched_note is not None, "Note not found in API"
    assert matched_note["description"] == description, "Description mismatch"
    assert matched_note["category"] == category, "Category mismatch"


# =========================
# TS-14: API → UI DELETE SYNC
# =========================
@pytest.mark.ui
def test_api_to_ui_delete_sync(logged_in_user):
    """
    TC-14: Validate note deletion via API reflects in UI
    """

    driver = logged_in_user
    notes = NotesPage(driver)

    api = APIClient()
    

    # Unique note
    title = f"Delete_{int(time.time())}"
    desc = "This is a delete sync test"
    #create note via UI
    notes.create_note(title, desc)

    # Fetch from API
    response = api.get_notes()
    assert response.status_code == 200

    data = response.json()["data"]
    note = next((n for n in data if n["title"] == title), None)

    assert note is not None

    # Delete via API
    delete_response = api.delete_note(note["id"])
    assert delete_response.status_code == 200

    # UI polling
    for _ in range(5):
        driver.refresh()
        notes.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        if not notes.is_note_present(title):
            break
        time.sleep(1) #allows backend to sync

    assert not notes.is_note_present(title), \
        "Deleted note still visible in UI"


# =========================
# TS-15: FULL END-TO-END FLOW
# =========================
@pytest.mark.ui
def test_ui_api_full_cycle(logged_in_user):
    """
    TC-15: Full E2E flow
    UI Create → API Validate → API Delete → UI Validate
    """

    driver = logged_in_user
    notes = NotesPage(driver)

    api = APIClient()


    # Unique data
    title = f"E2E_{int(time.time())}"
    description = "This is a full cycle test"
    category = "Work"

    # Step 1: Create via UI
    notes.create_note(title, description, category)

    # Step 2: Validate in API
    response = api.get_notes()
    assert response.status_code == 200

    data = response.json()["data"]
    matched_note = next((n for n in data if n["title"] == title), None)

    assert matched_note is not None, "Note not found in API"

    note_id = matched_note["id"]

    # Step 3: Delete via API
    delete_response = api.delete_note(note_id)
    assert delete_response.status_code == 200

    # Step 4: Validate UI
    for _ in range(5):
        driver.refresh()
        notes.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        if not notes.is_note_present(title):
            break
        time.sleep(1)

    assert not notes.is_note_present(title), \
        "Note still visible after deletion"