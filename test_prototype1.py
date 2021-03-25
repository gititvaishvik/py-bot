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
#from selenium.webdriver.chrome.options import Options
import csv
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
#chrome_options.add_experimental_option('useAutomationExtension', False)
class TestPrototype1():
  def setup_method(self):
    self.driver = webdriver.Firefox(executable_path="C:\\Users\\ms\\Documents\\auto\\geckodriver-v0.24.0-win64\\geckodriver.exe")
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_prototype1(self,row):
    self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLScMCfxO9vFZnsLMl8rqpQ8yYfxZRMUKM_OTWd9UM2Hxil4QhQ/viewform")
    self.driver.set_window_size(842, 554)
    
    self.driver.find_element(By.CSS_SELECTOR, ".freebirdFormviewerViewNumberedItemContainer:nth-child(1) .quantumWizTextinputPaperinputInput").click()
    self.driver.find_element(By.CSS_SELECTOR, ".freebirdFormviewerViewNumberedItemContainer:nth-child(1) .quantumWizTextinputPaperinputInput").send_keys(row[0])
    self.driver.find_element(By.CSS_SELECTOR, ".freebirdFormviewerViewNumberedItemContainer:nth-child(2) .quantumWizTextinputPaperinputInput").send_keys(row[1])
    self.driver.find_element(By.CSS_SELECTOR, ".quantumWizTextinputPapertextareaInput").send_keys(row[2])
    self.driver.find_element(By.CSS_SELECTOR, ".appsMaterialWizButtonPaperbuttonLabel").click()
    self.driver.find_element(By.LINK_TEXT, "Submit another response").click()

test1= TestPrototype1()
test1.setup_method()
entry = "C:\\Users\\ms\\Documents\\auto\\test.csv"

fields = []
rows = []
with open(entry, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
      
    # extracting field names through first row
    fields = next(csvreader)
  
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
    
for row in rows[:4]:
  test1.test_prototype1(row)