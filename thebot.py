import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])


driver=webdriver.Chrome(executable_path=r'C:\Users\91829\Desktop\modules\chromedriver.exe',chrome_options=options)
driver.get('https://www.reddit.com/r/Anxiety/')
lst=[]
driver.implicitly_wait(10)


start=time.time()
SCROLL_PAUSE_TIME = 0.5

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.implicitly_wait(10)

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")

##    #this condition is to reach bottom
##    if new_height == last_height:
##        break


    if time.time()-start>500:
        break
   
    
    last_height = new_height
    




for i in range(5,600):
    print(i)
    text=f"/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[4]/div[{i}]/div/div/div[3]/div[3]/div/div/p"
    try:
        ele=driver.find_element_by_xpath(text)
        value=ele.get_attribute('innerHTML')
        lst.append(value)
    except:
        continue



driver.quit()


df=pd.DataFrame({"comments":lst})
df.to_csv("reddit_anxiety.csv")


