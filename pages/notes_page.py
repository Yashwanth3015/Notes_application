from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage


class NotesPage(BasePage):

    # =====================================================
    # LOCATORS
    # =====================================================

    add_note_btn = (
        By.XPATH,
        "//button[contains(text(),'Add Note')]"
    )

    note_title_input = (
        By.ID,
        "title"
    )

    note_description_input = (
        By.ID,
        "description"
    )

    category_dropdown = (
        By.ID,
        "category"
    )

    create_btn = (
        By.XPATH,
        "//button[text()='Create']"
    )

    note_card = (
        By.CLASS_NAME,
        "card"
    )

    delete_btn = (
        By.XPATH,
        "//button[contains(@class,'btn-danger')]"
    )

    empty_message = (
        By.XPATH,
        "//*[contains(text(),'No Notes Found')]"
    )

    validation_message = (
        By.XPATH,
        "//*[contains(text(),'Title')]"
    )

    duplicate_message = (
        By.XPATH,
        "//*[contains(text(),'already exists')]"
    )

    # =====================================================
    # CREATE NOTE
    # =====================================================

    def create_note(
        self,
        title,
        description,
        category="Home"
    ):

        import time

        # -----------------------------------------
        # STABILIZATION
        # -----------------------------------------

        time.sleep(1)

        # -----------------------------------------
        # CLICK ADD NOTE
        # -----------------------------------------

        self.click(
            self.add_note_btn
        )

        # -----------------------------------------
        # ENTER TITLE
        # -----------------------------------------

        self.enter_text(
            self.note_title_input,
            title
        )

        # -----------------------------------------
        # ENTER DESCRIPTION
        # -----------------------------------------

        self.enter_text(
            self.note_description_input,
            description
        )

        # -----------------------------------------
        # SELECT CATEGORY
        # -----------------------------------------

        category_option = (
            By.XPATH,
            f"//option[text()='{category}']"
        )

        self.click(
            self.category_dropdown
        )

        self.click(
            category_option
        )

        # -----------------------------------------
        # CREATE NOTE
        # -----------------------------------------

        self.click(
            self.create_btn
        )

        # -----------------------------------------
        # EMPTY TITLE VALIDATION
        # -----------------------------------------

        if title.strip() == "":

            self.wait.until(
                EC.visibility_of_element_located(
                    self.validation_message
                )
            )

        else:

            try:

                self.wait.until(
                    EC.invisibility_of_element_located(
                        self.create_btn
                    )
                )

            except TimeoutException:
                pass

        time.sleep(1)

    # =====================================================
    # NOTE PRESENT CHECK
    # =====================================================

    def is_note_present(self, title):

        locator = (
            By.XPATH,
            f"//*[contains(text(),'{title}')]"
        )

        return self.is_visible(
            locator
        )

    # =====================================================
    # DELETE NOTE
    # =====================================================

    def delete_first_note(self):

        self.click(
            self.delete_btn
        )

    # =====================================================
    # EMPTY MESSAGE
    # =====================================================

    def is_empty_message_displayed(self):

        return self.is_visible(
            self.empty_message
        )

    # =====================================================
    # VALIDATION MESSAGE
    # =====================================================

    def is_validation_message_displayed(self):

        return self.is_visible(
            self.validation_message
        )

    # =====================================================
    # DUPLICATE ERROR
    # =====================================================

    def is_duplicate_error_displayed(self):

        return self.is_visible(
            self.duplicate_message
        )