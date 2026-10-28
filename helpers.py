from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL_LOGIN = "https://tst.lebane.app/"

def login_helper(driver):
    driver.get(URL_LOGIN)
    wait = WebDriverWait(driver, 15)

    usuario = wait.until(
        EC.visibility_of_element_located((By.NAME, "email"))
    )
    usuario.send_keys("qapruebatec1@lebane.app")

    password = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password.send_keys("x2EWs0s*tQ.Rhfn")

    boton = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type='submit']")
        )
    )
    boton.click()