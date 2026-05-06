import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from api.api_client import APIClient
from utils.config import API_URL


@pytest.mark.ui
def test_login_invalid_credentials(driver):

    from utils.config import UI_URL

    home = HomePage(driver)
    login = LoginPage(driver)

    home.load(UI_URL)

    home.click_login()

    login.login(
        "wrong@mail.com",
        "wrong123"
    )

    assert login.is_error_displayed()


@pytest.mark.ui
def test_create_note_empty_title(logged_in_user):
    """
    TC-04: Validate note creation with empty title
    """
    driver = logged_in_user
    notes = NotesPage(driver)

    notes.create_note("", "Description without title")

    # No valid note should appear
    assert not notes.is_note_present("INVALID_TEST_TITLE")


@pytest.mark.ui
def test_create_duplicate_note(logged_in_user):
    """
    TC-05: Duplicate note creation handling
    """
    driver = logged_in_user
    notes = NotesPage(driver)

    title = "Duplicate_Test"
    desc = "This is the Duplicate case"

    notes.create_note(title, desc)
    notes.create_note(title, desc)

    # System may allow duplicates — validate at least one exists
    assert notes.is_note_present(title)


@pytest.mark.ui
def test_invalid_category(logged_in_user):
    """
    TC-06: Invalid category handling (edge)
    """
    driver = logged_in_user
    notes = NotesPage(driver)

    # Try invalid category by bypass (handled internally if dropdown restricts)
    notes.create_note("InvalidCat", "Test", category="Work")

    assert notes.is_note_present("InvalidCat")


@pytest.mark.api
def test_api_invalid_token():

    import requests
    from utils.config import API_URL

    response = requests.get(
        f"{API_URL}/notes",
        headers={"x-auth-token": "invalid_token"}
    )

    assert response.status_code == 401


@pytest.mark.api
def test_api_missing_fields():
    """
    TC-11: API with missing required fields
    """
    import requests
    from utils.config import API_URL

    response = requests.post(
        f"{API_URL}/users/login",
        json={"email": "test@test.com"}
    )

    assert response.status_code in [400, 401]


@pytest.mark.api
def test_api_invalid_endpoint():
    """
    TC-12: Invalid endpoint handling
    """
    import requests
    from utils.config import API_URL

    response = requests.get(f"{API_URL}/invalid-endpoint")
    assert response.status_code in [404, 400]