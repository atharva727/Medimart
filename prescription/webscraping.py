from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

def get1mg(medicines, driver):
    meds = []
    totalPrice = 0
    mg = {}

    for med in medicines:
        url='https://www.1mg.com/search/all?name='+med
        driver.get(url) 
        
        d = {}
        try:
            d['name'] = driver.find_element(By.CLASS_NAME,'style__pro-title___3zxNC').text
            d['price']=driver.find_element(By.CLASS_NAME,'style__price-tag___B2csA').text.split("₹")[-1]
            d['link'] = driver.find_element(By.CSS_SELECTOR, '.style__horizontal-card___1Zwmt a').get_attribute('href')
        except:
            d = {'name':None,'price':0,'link':None}
        
        totalPrice+= float(d['price'])
        totalPrice = round(totalPrice,2)
        meds.append(d)

    mg = {'medicines':meds,'totalPrice':totalPrice,'name':'1 MG'}
    return mg

def getNetmed(medicines, driver):
    meds = []
    totalPrice = 0
    netmed = {}
    
    for med in medicines:
        url= 'https://www.netmeds.com/catalogsearch/result/' + med + '/all'
        driver.get(url) 
        
        d = {}
        try:
            d['name'] = driver.find_element(By.CLASS_NAME, 'clsgetname').text
            d['price'] = driver.find_element(By.ID, 'final_price').text.split("₹")[-1]
            d['link']  = driver.find_element(By.CLASS_NAME, 'category_name').get_attribute('href')
        except:
            d = {'name':None,'price':0,'link':None}

        totalPrice+= float(d['price'])
        totalPrice = round(totalPrice,2)
        meds.append(d)

    netmed = {'medicines':meds,'totalPrice':totalPrice,'name':'NETMEDS'}
    return netmed

def getApollo(medicines, driver):
    meds = []
    totalPrice = 0
    apollo = {}
    for med in medicines:
        url= 'https://www.apollopharmacy.in/search-medicines/' + med
        page = requests.get(url)

        soup = BeautifulSoup(page.content, "html.parser")
        
        d = {}
        try:
            d['name']  = soup.find_all("p", class_="ProductCard_productName__f82e9")[0].text
            d['price'] =soup.find_all("div", class_="ProductCard_priceGroup__V3kKR")[0].text.split("₹")[-1]
            d['link']  = 'https://www.apollopharmacy.in/'+ soup.find_all("a", class_="ProductCard_proDesMain__LWq_f")[0].get('href')
        except:
            d = {'name':None,'price':0,'link':None}
        
        totalPrice+= float(d['price'])
        totalPrice = round(totalPrice,2)
        meds.append(d)

    apollo = {'medicines':meds,'totalPrice':totalPrice,'name':'APOLLO'}
    return apollo

def getPharmeasy(medicines, driver):
    meds = []
    totalPrice = 0
    pharmeasy = {}
    for med in medicines:

        url= 'https://pharmeasy.in/search/all?name=' + med
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser") 
        
        d = {}
        try:            
            d['name']  = soup.find_all("h1", class_="ProductCard_medicineName__8Ydfq")[0].text
            d['price'] =soup.select(".ProductCard_gcdDiscountContainer__CCi51 span")[0].text.split("₹")[-1]
            d['link']  = 'https://pharmeasy.in/' + soup.find_all("a", class_="ProductCard_medicineUnitWrapper__eoLpy")[0].get('href')
        except:
            d = {'name':None,'price':0,'link':None}
        
        totalPrice+= float(d['price'])
        totalPrice = round(totalPrice,2)
        meds.append(d)
    
    pharmeasy = {'medicines':meds,'totalPrice':totalPrice,'name':'PHARMEASY'}        
    return pharmeasy                  