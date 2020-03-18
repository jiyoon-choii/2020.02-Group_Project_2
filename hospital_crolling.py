from selenium import webdriver
from urllib. request import urlopen
import time
from base64 import b64encode
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()

options.add_argument('headless')
options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
driver = webdriver.Chrome("./chromedriver.exe", chrome_options=options)
href = list()
name = list()
addr = list()
for k in range(1,10) :
    url = 'https://store.naver.com/hospitals/list?page={0}&query=%EB%B6%80%EC%82%B0%EA%B4%91%EC%97%AD%EC%8B%9C%20%EB%B3%91%EC%9B%90&queryType=hospital&sessionid=Cr6K7TsxHTrMVkzBcWkASQ%3D%3D&sortingOrder=precision'.format(k)
    #url = base_url.format(n+1)

    driver.get(url)
    time.sleep(1)
    item=driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/div/div[2]/ul').find_elements_by_class_name('name')
    # href = list()
    for i in item :
        href.append(i.get_attribute('href'))
    # print(href) 
    # name = list()
    # addr = list()
    for j in href:
        driver.get(j)
        name.append(driver.find_element_by_class_name('name').text)
        addr.append(driver.find_element_by_class_name('addr').text)

print(name)
    # print(name)

# name = list()
# small_addr = list()
# for i in item :
#     name.append(c.find_element_by_class_name('name').text)
#     small_addr.append(c.find_element_by_class_name('addr').text)




'''
item = list()
print(webpage)
name = webpage.find_elements_by_class_name('name')
print(name)
'''
'''    
for n in [1]: 
    url = base_url.format(n+1)
    webpage = driver.get(url)
    item = list()
    print(webpage)
    name = webpage.find_elements_by_class_name('name')
    print(name)
'''
'''
    item.append(webpage.find_elements_by_class_name('name').get_attribute("href")) 
    for p in item :
        name = list()
        small_addr = list()
        for c in item :
            name.append(c.find_element_by_class_name('name').text)
            small_addr.append(c.find_element_by_class_name('addr').text)
'''
print('------------')

    



# name = list()
# small_addr = list()

# count = 1
# for url in url_list :
#     driver.get(url)

#     hospitals = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/div/div[2]/ul')
#     hospital = hospitals.find_element_by_xpath('//*[@id="_business_11559181"]/div/div/div[1]/span/a').get_attribute("href")

#     for tmp in hospital :
#         name.append(tmp.find_element_by_class_name('name').text)
#         small_addr.append(tmp.find_element_by_class_name('addr').text)

# print('***************')
    

# for i in url_list:
#         driver.get(i)
#         time.sleep(1)
#         tmp = driver.find_element_by_xpath('//*[@id="app"]')
#         item = tmp.find_element_by_tag_name('li')
#         try:
#             name = item.find_element_by_class_name('name').text
#         except Exception as e:
#             continue
#     count += 1