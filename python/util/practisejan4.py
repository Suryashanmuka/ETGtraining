from selenium import webdriver
from selenium.webdriver.common.by import by
from selenium.webdriver.common.keys import keys
driver = webdriver.chrome(executable_path='D:\\selenium\\chromedriver.exe')
driver.get("http://automationpractice.com/index.php?controller=search&orderby=position&orderway=desc&search_query=t+shirts&submit_search=")
assert "Search - My Store" in driver.title
elem = driver.find_element_by_name("search_query")
elem.clear()
elem.send_keys("t shirts")
elem.send_keys(Keys.RETURN)
assert "no results found" not in driver.page_source
driver.quit()