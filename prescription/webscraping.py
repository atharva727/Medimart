from selenium.webdriver.common.by import By

def get1mg(medicines, driver):
    mg = []
    for med in medicines:
        url='https://www.1mg.com/search/all?name='+med
        driver.get(url) 
        
        d = {}
        d['title'] = driver.find_element(By.CLASS_NAME,'style__pro-title___3zxNC').text
        d['price']=driver.find_element(By.CLASS_NAME,'style__price-tag___B2csA').text
        d['link'] = driver.find_element(By.CSS_SELECTOR, '.style__horizontal-card___1Zwmt a').get_attribute('href')
        
        mg+=[d]
        
    return mg

def getNetmed(medicines, driver):
    netmed = []
    for med in medicines:
        url= 'https://www.netmeds.com/catalogsearch/result/' + med + '/all'
        driver.get(url) 
        
        d = {}
        d['title'] = driver.find_element(By.CLASS_NAME, 'clsgetname').text
        d['price'] = driver.find_element(By.ID, 'final_price').text
        d['link']  = driver.find_element(By.CLASS_NAME, 'category_name').get_attribute('href')

        netmed+=[d]
        
    return netmed

def getApollo(medicines, driver):
    apollo = []
    for med in medicines:
        url= 'https://www.apollopharmacy.in/search-medicines/' + med
        driver.get(url) 
        
        d = {}
        
        d['title']  = driver.find_element(By.CLASS_NAME, 'ProductCard_productName__f82e9').text
        d['price'] =driver.find_element(By.CLASS_NAME,'ProductCard_priceGroup__V3kKR').text[3:]
        d['link']  = driver.find_element(By.CLASS_NAME, 'ProductCard_proDesMain__LWq_f').get_attribute('href')

        apollo+=[d]
        
    return apollo

def getPharmeasy(medicines, driver):
    pharmeasy = []
    for med in medicines:
        url= 'https://pharmeasy.in/search/all?name=' + med
        driver.get(url) 
        
        d = {}

        d['title']=driver.find_element(By.CLASS_NAME,'ProductCard_medicineName__8Ydfq').text
        d['price']=driver.find_element(By.CSS_SELECTOR,'.ProductCard_gcdDiscountContainer__CCi51 span').text
        d['link'] = driver.find_element(By.CLASS_NAME,'ProductCard_defaultWrapper__nxV0R').get_attribute('href')
        pharmeasy+=[d]
        
    return pharmeasy                  



