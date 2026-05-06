import allure
import time
import pytest
from pages.notes_page import NotesPage


@pytest.mark.ui
def test_create_note_ui(logged_in_user):
    """
    TC-03: Validate note creation
    """

    driver = logged_in_user
    notes = NotesPage(driver)

    title = "Automation Note FINAL"
    description = "Created after proper wait"

    notes.create_note(title, description)

    assert notes.is_note_present(title), "Note creation failed!" 
    """
    TC-07:Validate note appears instantly in UI (validated via is_note_present())
    """

    


@allure.feature("UI Validation")
@allure.story("Validate note appears instantly in UI")
def test_note_appears_instantly_ui(logged_in_user):

    notes = NotesPage(logged_in_user)

    title = "Instant UI Note"
    description = "UI Validation Check"

    # Create note
    notes.create_note(title, description)

    # Wait briefly for UI rendering
    time.sleep(2)

    # Validate note visible immediately
    assert notes.is_note_present(title)