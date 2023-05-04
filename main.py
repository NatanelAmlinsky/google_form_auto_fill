import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(service=Service("<PATH OF THE DRIVER.EXE>"))
driver.implicitly_wait(10)
count = 0
while True:
    #   get url function
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdN9A35duXUCvEbNedwbfKGd0eLY2NY802Vsf2zNsxR-y-cCw/viewform')
    # Lists of XPATH element locators in purpose to random use.
    list_element1 = ["//*[@id='i7']/div[3]", "//*[@id='i10']/div[3]/div", "//*[@id='i13']/div[3]/div",
           "//*[@id='i16']/div[3]/div"]
    list_element2 = ["//*[@id='i23']/div[3]/div", "//*[@id='i26']/div[3]/div", "//*[@id='i29']/div[3]/div",
            "//*[@id='i32']/div[3]/div"]
    list_element3 = ["//*[@id='i39']/div[3]/div", "//*[@id='i42']/div[3]/div", "//*[@id='i45']/div[3]/div",
            "//*[@id='i48']/div[3]/div",
            "//*[@id='i51']/div[3]/div", "//*[@id='i54']/div[3]/div", "//*[@id='i57']/div[3]/div"]

    # generate a random index
    random_index_1 = random.randint(0, len(list_element1) - 1)
    random_index_2 = random.randint(0, len(list_element2) - 1)
    random_index_3 = random.randint(0, len(list_element3) - 1)
    # get the random value from the list
    random_value_1 = list_element1[random_index_1]
    random_value_2 = list_element2[random_index_2]
    random_value_3 = list_element3[random_index_3]

    driver.find_element(By.XPATH, value=random_value_1).click()
    # #   scrool down to the element, You don't really need it.
    # element1 = driver.find_element(By.XPATH, value=random_value_1)
    # driver.execute_script("arguments[0].scrollIntoView();", element1)

    driver.find_element(By.XPATH, value=random_value_2).click()
    # #   scrool down to the element, You don't really need it.
    # element2 = driver.find_element(By.XPATH, value=random_value_2)
    # driver.execute_script("arguments[0].scrollIntoView();", element2)

    driver.find_element(By.XPATH, value=random_value_3).click()
    # #   scrool down to the element, You don't really need it.
    # element3 = driver.find_element(By.XPATH, value=random_value_3)
    # driver.execute_script("arguments[0].scrollIntoView();", element3)

    driver.find_element(By.XPATH, value="//*[@id='i73']/div[3]/div").click()
    # #   scrool down to the element, You don't really need it.
    # element4 = driver.find_element(By.XPATH, value="//*[@id='i73']/div[3]/div")  # עומר גולדנברג מזכרת בתיה
    # driver.execute_script("arguments[0].scrollIntoView();", element4)

    driver.find_element(By.XPATH, value="//*[@id='i98']/div[3]/div").click()
    # #   scrool down to the element, You don't really need it.
    # element5 = driver.find_element(By.XPATH, value="//*[@id='i98']/div[3]/div")  # מזכרת בתיה
    # driver.execute_script("arguments[0].scrollIntoView();", element5)

    driver.find_element(By.XPATH, value="//*[@id='i126']/div[3]/div").click()
    # #   scrool down to the element, You don't really need it.
    # element6 = driver.find_element(By.XPATH, value="//*[@id='i126']/div[3]/div")  # מזכרת בתיה
    # driver.execute_script("arguments[0].scrollIntoView();", element6)

    driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[3]/div/div[1]/div/span/span").click()
    count += 1
