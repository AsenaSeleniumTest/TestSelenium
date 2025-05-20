#!/usr/bin/env python3
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def test_driver_test():
    """ test url match """
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(service = service,options = options)
    driver.maximize_window()
    driver.get("https://duckduckgo.com/")
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,"//input[@name='q']").send_keys("The dev-friendly football API")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    driver.find_element(By.XPATH,"//span[text()='The dev-friendly football API']").click()
    url = driver.current_url()
    assert url == "https://www.football-data.org/"