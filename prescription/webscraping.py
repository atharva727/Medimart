from selenium.webdriver.common.by import By

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
        meds.append(d)

    netmed = {'medicines':meds,'totalPrice':totalPrice,'name':'NETMEDS'}
    return netmed

def getApollo(medicines, driver):
    meds = []
    totalPrice = 0
    apollo = {}
    for med in medicines:
        url= 'https://www.apollopharmacy.in/search-medicines/' + med
        driver.get(url) 
        
        d = {}
        try:
            d['name']  = driver.find_element(By.CLASS_NAME, 'ProductCard_productName__f82e9').text
            d['price'] =driver.find_element(By.CLASS_NAME,'ProductCard_priceGroup__V3kKR').text.split("₹")[-1]
            d['link']  = driver.find_element(By.CLASS_NAME, 'ProductCard_proDesMain__LWq_f').get_attribute('href')
        except:
            d = {'name':None,'price':0,'link':None}
        
        totalPrice+= float(d['price'])
        meds.append(d)

    apollo = {'medicines':meds,'totalPrice':totalPrice,'name':'APOLLO'}
    return apollo

def getPharmeasy(medicines, driver):
    meds = []
    totalPrice = 0
    pharmeasy = {}
    for med in medicines:
        url= 'https://pharmeasy.in/search/all?name=' + med
        driver.get(url) 
        
        d = {}
        try:
            d['name']=driver.find_element(By.CLASS_NAME,'ProductCard_medicineName__8Ydfq').text
            d['price']=driver.find_element(By.CSS_SELECTOR,'.ProductCard_gcdDiscountContainer__CCi51 span').text.split("₹")[-1]
            d['link'] = driver.find_element(By.CLASS_NAME,'ProductCard_defaultWrapper__nxV0R').get_attribute('href')
        except:
            d = {'name':None,'price':0,'link':None}
        
        totalPrice+= float(d['price'])
        meds.append(d)
    
    pharmeasy = {'medicines':meds,'totalPrice':totalPrice,'name':'PHARMEASY'}        
    return pharmeasy                  