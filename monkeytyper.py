from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from pynput.keyboard import Key, Controller
import random
keyboard = Controller()

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
driver = webdriver.Chrome(executable_path='./chromedriver')

driver.get("https://monkeytype.com")
time.sleep(5)
#letters = []
#letters = driver.find_elements_by_tag_name("letter")
#for letter in letters:
#    content.append(letter.get_attribute('content'))
for i in range(3):
    print("Get ready... {}".format(3 - i))
    time.sleep(1)

raw = driver.page_source
soup = BeautifulSoup(raw, "html.parser")
content = soup.find_all(class_ = "word")

count = 0
for word in content:
    newsoup = BeautifulSoup(str(word), "html.parser")
    final = (newsoup.find_all("letter"))
    for i in final:
        if count < len(word):
            scuff = random.randint(10, 100)
            if scuff == 50:
                keyboard.type(random.choice(alphabet))
                # keyboard.type(random.choice())
            else:
                keyboard.type(str(i.text))
                time.sleep(random.uniform(0.08, 0.0004))
            count += 1
        if count == len(word):
            keyboard.press(Key.space)
            keyboard.release(Key.space)
            count = 0