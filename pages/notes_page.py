from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class NotesPage(BasePage):

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

    def create_note(self, title, description, category="Home"):

        import time

        # Wait and click Add Note
        add_btn = self.wait.until(
            EC.element_to_be_clickable(
                self.add_note_btn
            )
        )

        try:
            add_btn.click()

        except:
            self.driver.execute_script(
                "arguments[0].click();",
                add_btn
            )

        # Wait for popup
        self.wait.until(
            EC.visibility_of_element_located(
                self.note_title_input
            )
        )

        # Small stabilization wait
        time.sleep(1)

        # Enter title
        self.enter_text(
            self.note_title_input,
            title
        )

        # Enter description
        self.enter_text(
            self.note_description_input,
            description
        )

        # Select category
        category_option = (
            By.XPATH,
            f"//option[text()='{category}']"
        )

        self.click(self.category_dropdown)

        self.wait.until(
            EC.element_to_be_clickable(
                category_option
            )
        )

        self.click(category_option)

        # Click Create
        self.click(self.create_btn)

        # Positive case
        if title.strip() != "":

            self.wait.until(
                EC.invisibility_of_element_located(
                    self.create_btn
                )
            )

        # Negative case
        else:

            self.wait.until(
                EC.visibility_of_element_located(
                    self.validation_message
                )
            )

        time.sleep(1)

    def is_note_present(self, title):

        locator = (
            By.XPATH,
            f"//*[contains(text(),'{title}')]"
        )

        return self.is_visible(locator)

    def delete_first_note(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.delete_btn
            )
        )

        self.click(self.delete_btn)

    def is_empty_message_displayed(self):

        return self.is_visible(
            self.empty_message
        )

    def is_validation_message_displayed(self):

        return self.is_visible(
            self.validation_message
        )

    def is_duplicate_error_displayed(self):

        return self.is_visible(
            self.duplicate_message
        )