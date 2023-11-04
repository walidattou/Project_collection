from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import requests



Links = []
name = []



options = Options()
options.add_argument('headless')


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)


driver.get("https://9animetv.to")

main_page = driver.current_window_handle




driver.find_element(By.NAME ,'keyword').send_keys("My Dress Up Darling")
searchB = driver.find_element(By.XPATH,('//*[@id="search-form"]/div/div'))
ActionChains(driver).double_click(searchB).perform()
driver.switch_to.window(main_page)
ActionChains(driver).double_click(searchB).perform()




url = driver.current_url
re = requests.get(url)
content = re.text
soup = BeautifulSoup(content,'html.parser')

for x in soup.find_all(name='a',class_='dynamic-name'):
    y = x.get('title')
    name.append(y)
for x in soup.find_all(name='a',class_='film-poster-ahref'):
    y = x.get('href')
    Links.append(y)

del name[len(Links):100]

S = 'Results : \n'
for i in range(0,len(Links)):   
    S += name[i] + ':\n'
    S += Links[i]+'\n'

with open('results.txt', 'w') as f:     
        f.write(S)
