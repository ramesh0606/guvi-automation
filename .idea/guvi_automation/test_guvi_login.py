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
def test_zenclass_login(setup_and_teardown):
    assert driver.find_element(By.XPATH,
                               "//span[contains(text(), 'Sessions Roadmap')]").is_displayed(), "user Login is failed:"


@pytest.mark.functional
def test_zenclass_portal_logout(setup_and_teardown):
    driver.find_element(By.CLASS_NAME, "profileIcon").click()
    driver.find_element(By.XPATH, "//*[contains(text(),'Logout')]").click()
    assert driver.find_element(By.XPATH,
                               "//button[contains(text(),'Login')]").is_displayed(), "logout is not succesful, please cheeck for reason"


@pytest.mark.functional
def test_is_profile_page_displayed(setup_and_teardown):
    driver.find_element(By.CLASS_NAME, "profileIcon").click()
    driver.find_element(By.XPATH, "//*[contains(text(),'Profile')]").click()
    expected_profile_text = "My Profile"
    actual_profile_text = driver.find_element(By.XPATH, "//h1[@class=\"heading\"]").text
    assert actual_profile_text.__eq__(expected_profile_text), " test is failed due to name mismatch"


@pytest.mark.functional
def test_is_profile_email_sameas_login_email(setup_and_teardown):
    driver.find_element(By.CLASS_NAME, "profileIcon").click()
    driver.find_element(By.XPATH, "//*[contains(text(),'Profile')]").click()
    print("searching for an element: ", driver.find_element(By.XPATH, "//input[@name='name']"))
    print("tag_name: ", driver.find_element(By.XPATH, "//input[@name='name']").tag_name)
    print("class: ", driver.find_element(By.XPATH, "//input[@name='name']").get_attribute("value"))
    # expected_profile_text="s"
    # actual_profile_text=driver.find_element(By.XPATH, "//h1[@class=\"heading\"]").text
    # assert actual_profile_text.__eq__(expected_profile_text) , " test is failed due to name mismatch"


@pytest.mark.functional
def test_is_class_page_displayed(setup_and_teardown):
    expected_text = "Join the class on time!"
    actual_text = driver.find_element(By.XPATH, "//h3[contains(@class,'classhead m-0 text-white')]").text
    print("current url:", driver.current_url)
    assert actual_text.__eq__(expected_text), "text is not match:"

@pytest.mark.newcase
def test_left_side_available_options_count(setup_and_teardown):
    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.XPATH, "//li[@class=\"logo-fixed\"]")).perform()
    left_side_elements = driver.find_elements(By.XPATH, "//nav[@class='main-menu']/ul/div")
    print("left_side_elements :", len(left_side_elements))
    assert len(left_side_elements) == 17, "left side menu counts are not equal"
    # our test is to check whether particual task name is availbale or not.
    # but, still we will validate the total number of tasks. even total tasks are not equal, test case should not fail, it should continue.
    # in such cases, we should use soft assertions
    first_part = "//nav[@class='main-menu']/ul/div["
    last_part = "]/li/span/div/div[2]"
    left_menus = []
    for count in range(1, len(left_side_elements) + 1):
        print("count", first_part + str(count) + last_part)
        driver.set_page_load_timeout(50)
        left_menu_name = driver.find_element(By.XPATH, first_part + str(count) + last_part).text
        left_menus.append(left_menu_name)
    print(left_menus)
