from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import json

data = {}
data['movies'] = []
egybest_link='https://fool.egybest.life'

driver = webdriver.Chrome(executable_path='webdriver/chromedriver.exe')
driver.get('https://fool.egybest.life/movies')
html = driver.find_element_by_tag_name('html')
for i in range(120):
    html.send_keys(Keys.END)
    sleep(1)
product_titles = driver.find_elements_by_xpath("//a[@class='movie']")
id=0
for title in product_titles:
    id+=1
    html=title.get_attribute('outerHTML')
    #print(html)
    title_begin=html.find('<span class="title">')
    title_end=html.find('</span> <span class="ribbon ')
    film_url_from=html.find('<a href="')
    film_url_to=html.find('" class="movie"')
    film_url=html[film_url_from:film_url_to]
    img_begin=html.find('<img src="https')
    img_to=html.find('" alt=')
    title_with_span=html[title_begin:title_end]
    title_clean=title_with_span[20:180]
    film_url=film_url[9:150]
    film_url=egybest_link+film_url
    print ("film-url:",film_url)
    image_url=html[img_begin:img_to]
    image_url=image_url[10:150]
    print("title:",title_with_span[20:180])
    print("image-url:",image_url)
    data['movies'].append({
        'id':id,
        'title':title_clean,
        'cover_url':image_url,
        'film_url':film_url
    })

with open('Allfilms.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)



driver.close()