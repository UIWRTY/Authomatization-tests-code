# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestQahunter():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_qahunter(self):
    self.driver.get("http://test.qahunter.ru/")
    self.driver.set_window_size(1536, 824)
    self.driver.find_element(By.LINK_TEXT, "Войти/зарегистрироваться").click()
    self.driver.find_element(By.ID, "formInput#text").click()
    self.driver.find_element(By.ID, "formInput#text").send_keys("mi")
    self.driver.find_element(By.ID, "formInput#passowrd").send_keys("qwerty033")
    self.driver.find_element(By.CSS_SELECTOR, ".btn--lg").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dev__name").click()
    self.driver.find_element(By.CSS_SELECTOR, ".column--2of3").click()

import time
time sleep(5)
  
