from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import login_helper

def test_login_exitoso(driver):
    login_helper(driver)

    saludo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//p[contains(text(), 'Buenos días')]")
        )
    )

    assert saludo.is_displayed()
    assert "Buenos días" in saludo.text