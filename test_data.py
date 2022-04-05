from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

@pytest.fixture()
def setUp():
    global driver,name,address,pincode,mobile,email,password,confirmpass
    name = input("enter the name: ")
    address = input("enter the address: ")
    pincode = input("enter the pincode: ")
    mobile = input("enter the mobile no: ")
    email = input("enter the email id: ")
    password = input("enter the password: ")
    confirmpass = input("enter the confirm password: ")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    print("testcase started")
    driver.maximize_window()
    yield
    time.sleep(10)
    driver.close()
    print("testcase completed")

def test_data(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/userdata.php")
    driver.find_element_by_name("name").send_keys(name)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input[1]").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[3]/td[2]/select/option[2]").click()
    time.sleep(1)
    driver.find_element_by_name("Address").send_keys(address)
    time.sleep(1)
    driver.find_element_by_name("Pincode").send_keys(pincode)
    time.sleep(1)
    driver.find_element_by_name("Mobile").send_keys(mobile)
    time.sleep(1)
    driver.find_element_by_name("Email").send_keys(email)
    time.sleep(1)
    driver.find_element_by_name("pass").send_keys(password)
    time.sleep(1)
    driver.find_element_by_name("cnfpass").send_keys(confirmpass)
    time.sleep(1)
    driver.find_element_by_name("fcheckbox").click()
    time.sleep(2)
    driver.find_element_by_name("subbtn").send_keys(Keys.ENTER)
