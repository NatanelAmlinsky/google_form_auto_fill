import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(service=Service("C:\\Users\\natan\\Documents\\ChromeDriver\\chromedriver.exe"))
driver.implicitly_wait(10)
count = 0
while True:
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdN9A35duXUCvEbNedwbfKGd0eLY2NY802Vsf2zNsxR-y-cCw/viewform')

    mvp = ["//*[@id='i7']/div[3]", "//*[@id='i10']/div[3]/div", "//*[@id='i13']/div[3]/div",
           "//*[@id='i16']/div[3]/div"]
    opoy = ["//*[@id='i23']/div[3]/div", "//*[@id='i26']/div[3]/div", "//*[@id='i29']/div[3]/div",
            "//*[@id='i32']/div[3]/div"]
    dpoy = ["//*[@id='i39']/div[3]/div", "//*[@id='i42']/div[3]/div", "//*[@id='i45']/div[3]/div",
            "//*[@id='i48']/div[3]/div",
            "//*[@id='i51']/div[3]/div", "//*[@id='i54']/div[3]/div", "//*[@id='i57']/div[3]/div"]

    # generate a random index
    random_index_mvp = random.randint(0, len(mvp) - 1)
    random_index_opoy = random.randint(0, len(opoy) - 1)
    random_index_dpoy = random.randint(0, len(dpoy) - 1)
    # get the random value from the list
    random_value_mvp = mvp[random_index_mvp]
    random_value_opoy = opoy[random_index_opoy]
    random_value_dpoy = dpoy[random_index_dpoy]

    driver.find_element(By.XPATH, value=random_value_mvp).click()
    #   scrool down to the element
    element1 = driver.find_element(By.XPATH, value=random_value_mvp)
    driver.execute_script("arguments[0].scrollIntoView();", element1)

    driver.find_element(By.XPATH, value=random_value_opoy).click()
    #   scrool down to the element
    element2 = driver.find_element(By.XPATH, value=random_value_opoy)
    driver.execute_script("arguments[0].scrollIntoView();", element2)

    driver.find_element(By.XPATH, value=random_value_dpoy).click()
    #   scrool down to the element
    element3 = driver.find_element(By.XPATH, value=random_value_dpoy)
    driver.execute_script("arguments[0].scrollIntoView();", element3)

    driver.find_element(By.XPATH, value="//*[@id='i73']/div[3]/div").click()
    #   scrool down to the element
    element4 = driver.find_element(By.XPATH, value="//*[@id='i73']/div[3]/div")  # עומר גולדנברג מזכרת בתיה
    driver.execute_script("arguments[0].scrollIntoView();", element4)

    driver.find_element(By.XPATH, value="//*[@id='i98']/div[3]/div").click()
    #   scrool down to the element
    element5 = driver.find_element(By.XPATH, value="//*[@id='i98']/div[3]/div")  # מזכרת בתיה
    driver.execute_script("arguments[0].scrollIntoView();", element5)

    driver.find_element(By.XPATH, value="//*[@id='i126']/div[3]/div").click()
    #   scrool down to the element
    element6 = driver.find_element(By.XPATH, value="//*[@id='i126']/div[3]/div")  # מזכרת בתיה
    driver.execute_script("arguments[0].scrollIntoView();", element6)

    driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[3]/div/div[1]/div/span/span").click()
    count += 1
