from selenium import webdriver
import time
browser=webdriver.Chrome()
browser.get("https://mail.163.com")
browser.maximize_window()
browser.find_element_by_id("lbNormal").click()
browser.switch_to.frame(0)
browser.find_element_by_name("email").send_keys("gaoyangainiyibeizi")
browser.find_element_by_name("password").send_keys("199456")
browser.find_element_by_id("dologin").click()
browser.switch_to.frame("x-URS-iframe1565518371208.9683")
browser.find_element_by_id("auto-id-1565518371608").click()
time.sleep(10)