from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
def main():
    driver = webdriver.Chrome()
    driver.get("https://forms.yandex.ru/u/6549a7a5e010db14cf2e6e68/")
    for i in range(15):
        my_page = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/form/div/div[2]/div/div[1]/label[3]').click()
        time.sleep(1)
        indiv = '//*[@id="root"]/div/main/form/div/div[3]/div/div[1]/label[1]'
        url = '//*[@id="root"]/div/main/form/div/div[3]/div/div[1]/label[2]'
        pol = [indiv, url]
        random_pol = random.choices(pol, weights=[90, 10])[0]
        driver.find_element(By.XPATH, random_pol).click()
        time.sleep(1)
        menee_goda='//*[@id="root"]/div/main/form/div/div[4]/div/div[1]/label[1]'
        ot_goda_do_pati='//*[@id="root"]/div/main/form/div/div[4]/div/div[1]/label[2]'
        ot_pati='//*[@id="root"]/div/main/form/div/div[4]/div/div[1]/label[3]'
        bisness_time=[menee_goda, ot_goda_do_pati, ot_pati]
        random_bisness_time = random.choices(bisness_time, weights=[10, 60, 30])[0]
        driver.find_element(By.XPATH, random_bisness_time).click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/form/div/div[5]/div/div[1]/label[1]').click()
        time.sleep(1)
        sobstvenik = '//*[@id="root"]/div/main/form/div/div[6]/div/div[1]/label[1]'
        sotrudnik = '//*[@id="root"]/div/main/form/div/div[6]/div/div[1]/label[4]'
        dolchost = [sobstvenik, sotrudnik]
        random_dolchost = random.choices(dolchost, weights=[90, 10])[0]
        driver.find_element(By.XPATH, random_dolchost).click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/form/div/div[7]/div/div[1]/label[1]').click()
        time.sleep(1)
        med
        tabletki
        soch_uslugi
        ritual
        mycop
        taxi
        avtoremont
        selskoe
        animals
        oil
        wood
        shop
        streetfood
        optov
        inoe

