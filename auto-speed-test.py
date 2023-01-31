from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException

class wait_for_testing_complete(object):

    def __init__(self):
        pass

    def __call__(self, driver):
        try:
            driver.find_element(By.XPATH, "//span[@class='spanSuccess-css-su' and text()[contains(.,'Successfully')]]")        
        except NoSuchElementException:
            return False
        return True

def run_test():
    options = Options()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    
    driver.get("https://speedtest.btwholesale.com/")
    
    driver.find_element(By.XPATH, '//button[text()="GO"]').click()            

    WebDriverWait(driver, 60).until(wait_for_testing_complete())
     
    download_speed = float(driver.find_element(By.XPATH, '//div[text()="DOWNLOAD"]/../../div[@class="row"][2]/div/h3').text)
    download_unit = driver.find_element(By.XPATH, '//div[text()="DOWNLOAD"]/../../div[@class="row"][3]/div').text    
    upload_speed = float(driver.find_element(By.XPATH, '//div[text()="UPLOAD"]/../../div[@class="row"][2]/div/h3').text)
    upload_unit = driver.find_element(By.XPATH, '//div[text()="UPLOAD"]/../../div[@class="row"][3]/div').text
    
    driver.close()

    return download_speed, download_unit, upload_speed, upload_unit

if __name__ == "__main__":
    download_speed, download_unit, upload_speed, upload_unit = run_test()
    
    print("Download {} {}".format(download_speed, download_unit))
    print("Upload {} {}".format(upload_speed, upload_unit))