import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def setup_and_teardown():
    # write code to open a browser
    global driver
    option = Options()
    option.add_experimental_option("detach", True)
    driver = WebDriver(options=option)
    driver.get("https://www.zenclass.in/login")
    driver.implicitly_wait(40)
    print(driver.title)
    driver.maximize_window()
    driver.find_element(By.NAME, "email").send_keys("rameshsanapathi@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("Jasnika@31012022")
    driver.find_element(By.XPATH, "//button[@type=\"submit\"]").click()
    yield
    driver.close()

@pytest.mark.atp
def test_search_for_send_message_chat(setup_and_teardown):
    assert driver.find_element(By.XPATH, "//*[contains(text(),' Send message ')]").is_displayed()