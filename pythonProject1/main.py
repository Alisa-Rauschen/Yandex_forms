from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#import os
#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.keys import Keys
import random
def main():
    driver = webdriver.Chrome()
    driver.get("https://forms.yandex.ru/u/6549a667eb614615da0849a3/")
    for i in range(15):
        time.sleep(1)
        my_page = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/form/div/div[2]/div/div[1]/label[3]').click()
        time.sleep(1)
        men = '//*[@id="root"]/div/main/form/div/div[3]/div/div[1]/label[1]'
        women = '//*[@id="root"]/div/main/form/div/div[3]/div/div[1]/label[2]'
        pol = [men, women]
        random_pol = random.choices(pol, weights=[40, 60])[0]
        my_page = driver.find_element(By.XPATH, random_pol).click()
        time.sleep(1)
        v18_24 = '//*[@id="root"]/div/main/form/div/div[4]/div/div[1]/label[1]'
        v25_34 = '//*[@id="root"]/div/main/form/div/div[4]/div/div[1]/label[2]'
        v35_44 = '//*[@id="root"]/div/main/form/div/div[4]/div/div[1]/label[3]'
        v45_54 = '//*[@id="root"]/div/main/form/div/div[4]/div/div[1]/label[4]'
        v55_64 = '//*[@id="root"]/div/main/form/div/div[4]/div/div[1]/label[5]'
        v64_ = '//*[@id="root"]/div/main/form/div/div[4]/div/div[1]/label[6]'
        vosrast = [v18_24, v25_34, v35_44, v45_54, v55_64, v64_]
        random_vosrast = random.choices(vosrast, weights=[10, 20, 25, 20, 15, 10])[0]
        my_page = driver.find_element(By.XPATH, random_vosrast).click()
        time.sleep(0.5)
        rabota = '//*[@id="root"]/div/main/form/div/div[5]/div/div[1]/label[1]'
        bez_rabota = '//*[@id="root"]/div/main/form/div/div[5]/div/div[1]/label[2]'
        student = '//*[@id="root"]/div/main/form/div/div[5]/div/div[1]/label[3]'
        domohoz = '//*[@id="root"]/div/main/form/div/div[5]/div/div[1]/label[4]'
        pensioner = '//*[@id="root"]/div/main/form/div/div[5]/div/div[1]/label[5]'
        samozan = '//*[@id="root"]/div/main/form/div/div[5]/div/div[1]/label[6]'
        preprinim = '//*[@id="root"]/div/main/form/div/div[5]/div/div[1]/label[7]'
        inoe = '//*[@id="root"]/div/main/form/div/div[5]/div/div[1]/label[8]'
        status = [rabota, bez_rabota, student, domohoz, pensioner, samozan, preprinim, inoe]
        if random_vosrast == v18_24:
            random_status = random.choices(status, weights=[20, 10, 50, 2, 0, 10, 2, 6])[0]
            driver.find_element(By.XPATH, random_status).click()
        elif random_vosrast == v25_34:
            random_status = random.choices(status, weights=[45, 5, 20, 12, 0, 10, 2, 6])[0]
            driver.find_element(By.XPATH, random_status).click()
        elif random_vosrast == v35_44:
            random_status = random.choices(status, weights=[50, 6, 10, 15, 5, 9, 5, 1])[0]
            driver.find_element(By.XPATH, random_status).click()
        elif random_vosrast == v45_54:
            random_status = random.choices(status, weights=[50, 5, 5, 14, 10, 8, 3, 5])[0]
            driver.find_element(By.XPATH, random_status).click()
        elif random_vosrast == v55_64:
            random_status = random.choices(status, weights=[28, 13, 2, 20, 28, 8, 1, 3])[0]
            driver.find_element(By.XPATH, random_status).click()
        else:
            random_status = random.choices(status, weights=[10, 5, 0.0002, 20, 60, 1, 1, 3])[0]
            driver.find_element(By.XPATH, random_status).click()
        time.sleep(0.5)
        school= '//*[@id="root"]/div/main/form/div/div[6]/div/div[1]/label[1]'
        hich_school = '//*[@id="root"]/div/main/form/div/div[6]/div/div[1]/label[2]'
        koled = '//*[@id="root"]/div/main/form/div/div[6]/div/div[1]/label[3]'
        bakalavr = '//*[@id="root"]/div/main/form/div/div[6]/div/div[1]/label[4]'
        spez = '//*[@id="root"]/div/main/form/div/div[6]/div/div[1]/label[5]'
        science = '//*[@id="root"]/div/main/form/div/div[6]/div/div[1]/label[6]'
        inoe_2 = '//*[@id="root"]/div/main/form/div/div[6]/div/div[1]/label[7]'
        obrazov = [school, hich_school, koled, bakalavr, spez, science, inoe_2]
        if random_vosrast == v18_24:
            random_obrazov = random.choices(obrazov, weights=[5, 15, 37, 20, 12, 1, 10])[0]
            driver.find_element(By.XPATH, random_obrazov).click()
        elif random_vosrast == v25_34:
            random_obrazov = random.choices(obrazov, weights=[5, 10, 29, 20, 19, 7, 10])[0]
            driver.find_element(By.XPATH, random_obrazov).click()
        elif random_vosrast == v35_44:
            random_obrazov = random.choices(obrazov, weights=[5, 15, 30, 15, 25, 9, 1])[0]
            driver.find_element(By.XPATH, random_obrazov).click()
        elif random_vosrast == v45_54:
            random_obrazov = random.choices(obrazov, weights=[10, 10, 35, 10, 20, 10, 5])[0]
            driver.find_element(By.XPATH, random_obrazov).click()
        elif random_vosrast == v55_64:
            random_obrazov = random.choices(obrazov, weights=[10, 15, 40, 5, 15, 5, 10])[0]
            driver.find_element(By.XPATH, random_obrazov).click()
        else:
            random_obrazov = random.choices(obrazov, weights=[5, 5, 50, 2, 25, 10, 3])[0]
            driver.find_element(By.XPATH, random_obrazov).click()
        # my_page = driver.find_element(By.XPATH, random.choices(obrazov, weights=[5, 15, 37, 17, 18, 5, 3])[0]).click()
        time.sleep(0.5)
        for g in range (1, 37, 1):
            mnogo = '//*[@id="root"]/div/main/form/div/div[8]/div/div[1]/div[{}]/button[1]'.format(g)
            norm = '//*[@id="root"]/div/main/form/div/div[8]/div/div[1]/div[{}]/button[2]'.format(g)
            malo = '//*[@id="root"]/div/main/form/div/div[8]/div/div[1]/div[{}]/button[3]'.format(g)
            nety = '//*[@id="root"]/div/main/form/div/div[8]/div/div[1]/div[{}]/button[4]'.format(g)
            hz = '//*[@id="root"]/div/main/form/div/div[8]/div/div[1]/div[{}]/button[5]'.format(g)
            otvet = [mnogo, norm, malo, nety, hz]
            if random_vosrast == v18_24:
                random_otvet = random.choices(otvet, weights=[33, 60, 1, 1, 5])[0]
                driver.find_element(By.XPATH, random_otvet).click()
                time.sleep(0.3)
            elif random_vosrast == v25_34:
                random_otvet = random.choices(otvet, weights=[27, 66, 1, 1, 5])[0]
                driver.find_element(By.XPATH, random_otvet).click()
                time.sleep(0.4)
            elif random_vosrast == v35_44:
                random_otvet = random.choices(otvet, weights=[27, 65, 1, 1, 6])[0]
                driver.find_element(By.XPATH, random_otvet).click()
                time.sleep(0.5)
            elif random_vosrast == v45_54:
                random_otvet = random.choices(otvet, weights=[29, 61, 3, 1, 6])[0]
                driver.find_element(By.XPATH, random_otvet).click()
                time.sleep(0.6)
            elif random_vosrast == v55_64:
                random_otvet = random.choices(otvet, weights=[34, 60, 1, 1, 4])[0]
                driver.find_element(By.XPATH, random_otvet).click()
                time.sleep(0.7)
            else:
                random_otvet = random.choices(otvet, weights=[33, 60, 1, 1, 5])[0]
                driver.find_element(By.XPATH, random_otvet).click()
                time.sleep(0.9)
        time.sleep(1)
        for q in range (10, 13, 1):
            for z in range (1, 37, 1):
                mnogo = '//*[@id="root"]/div/main/form/div/div[{}]/div/div[1]/div[{}]/button[1]'.format(q, z)
                norm = '//*[@id="root"]/div/main/form/div/div[{}]/div/div[1]/div[{}]/button[2]'.format(q, z)
                malo = '//*[@id="root"]/div/main/form/div/div[{}]/div/div[1]/div[{}]/button[3]'.format(q, z)
                nety = '//*[@id="root"]/div/main/form/div/div[{}]/div/div[1]/div[{}]/button[4]'.format(q, z)
                hz = '//*[@id="root"]/div/main/form/div/div[{}]/div/div[1]/div[{}]/button[5]'.format(q, z)
                otvet = [mnogo, norm, malo, nety, hz]
                if random_vosrast == v18_24:
                    random_otvet = random.choices(otvet, weights=[33, 60, 1, 1, 5])[0]
                    driver.find_element(By.XPATH, random_otvet).click()
                    time.sleep(0.1)
                elif random_vosrast == v25_34:
                    random_otvet = random.choices(otvet, weights=[30, 63, 1, 1, 5])[0]
                    driver.find_element(By.XPATH, random_otvet).click()
                    time.sleep(0.3)
                elif random_vosrast == v35_44:
                    random_otvet = random.choices(otvet, weights=[27, 65, 1, 1, 6])[0]
                    driver.find_element(By.XPATH, random_otvet).click()
                    time.sleep(0.5)
                elif random_vosrast == v45_54:
                    random_otvet = random.choices(otvet, weights=[30, 60, 3, 1, 7])[0]
                    driver.find_element(By.XPATH, random_otvet).click()
                    time.sleep(0.6)
                elif random_vosrast == v55_64:
                    random_otvet = random.choices(otvet, weights=[33, 60, 1, 1, 5])[0]
                    driver.find_element(By.XPATH, random_otvet).click()
                    time.sleep(0.7)
                else:
                    random_otvet = random.choices(otvet, weights=[31, 60, 4, 1, 4])[0]
                    driver.find_element(By.XPATH, random_otvet).click()
                    time.sleep(0.9)
        for x in range (1, 37, 1):
            mnogo = '//*[@id="root"]/div/main/form/div/div[14]/div/div[1]/div[{}]/button[1]'.format(x)
            norm = '//*[@id="root"]/div/main/form/div/div[14]/div/div[1]/div[{}]/button[2]'.format(x)
            malo = '//*[@id="root"]/div/main/form/div/div[14]/div/div[1]/div[{}]/button[3]'.format(x)
            nety = '//*[@id="root"]/div/main/form/div/div[14]/div/div[1]/div[{}]/button[4]'.format(x)
            otvet = [mnogo, norm, malo, nety]
            if random_vosrast == v18_24:
                random_otvet = random.choices(otvet, weights=[5, 65, 23, 6])[0]
                driver.find_element(By.XPATH, random_otvet).click()
                time.sleep(0.2)
            elif random_vosrast == v25_34:
                random_otvet = random.choices(otvet, weights=[5, 66, 23, 6])[0]
                driver.find_element(By.XPATH, random_otvet).click()
                time.sleep(0.3)
            elif random_vosrast == v35_44:
                random_otvet = random.choices(otvet, weights=[6, 74, 14, 5])[0]
                driver.find_element(By.XPATH, random_otvet).click()
                time.sleep(0.4)
            elif random_vosrast == v45_54:
                random_otvet = random.choices(otvet, weights=[5, 69, 17, 9])[0]
                driver.find_element(By.XPATH, random_otvet).click()
                time.sleep(0.6)
            elif random_vosrast == v55_64:
                random_otvet = random.choices(otvet, weights=[8, 65, 10, 16])[0]
                driver.find_element(By.XPATH, random_otvet).click()
                time.sleep(0.7)
            else:
                random_otvet = random.choices(otvet, weights=[5, 70, 9, 16])[0]
                driver.find_element(By.XPATH, random_otvet).click()
                time.sleep(0.8)
        for v in range(1, 7, 1):
            mnogo = '//*[@id="root"]/div/main/form/div/div[15]/div/div[1]/div[{}]/button[1]'.format(v)
            norm = '//*[@id="root"]/div/main/form/div/div[15]/div/div[1]/div[{}]/button[2]'.format(v)
            malo = '//*[@id="root"]/div/main/form/div/div[15]/div/div[1]/div[{}]/button[3]'.format(v)
            nety = '//*[@id="root"]/div/main/form/div/div[15]/div/div[1]/div[{}]/button[4]'.format(v)
            hz = '//*[@id="root"]/div/main/form/div/div[15]/div/div[1]/div[{}]/button[5]'.format(v)
            otvet = [mnogo, norm, malo, nety, hz]
            if random_vosrast == v18_24:
                random_otvet = random.choices(otvet, weights=[33, 60, 1, 1, 5])[0]
                driver.find_element(By.XPATH, random_otvet).click()
                time.sleep(1)
            elif random_vosrast == v25_34:
                random_otvet = random.choices(otvet, weights=[27, 66, 1, 1, 5])[0]
                driver.find_element(By.XPATH, random_otvet).click()
                time.sleep(1)
            elif random_vosrast == v35_44:
                random_otvet = random.choices(otvet, weights=[27, 65, 1, 1, 6])[0]
                driver.find_element(By.XPATH, random_otvet).click()
                time.sleep(1)
            elif random_vosrast == v45_54:
                random_otvet = random.choices(otvet, weights=[25, 63, 3, 1, 9])[0]
                driver.find_element(By.XPATH, random_otvet).click()
                time.sleep(1)
            elif random_vosrast == v55_64:
                random_otvet = random.choices(otvet, weights=[28, 60, 1, 1, 10])[0]
                driver.find_element(By.XPATH, random_otvet).click()
                time.sleep(1)
            else:
                random_otvet = random.choices(otvet, weights=[28, 60, 1, 1, 10])[0]
                driver.find_element(By.XPATH, random_otvet).click()
                time.sleep(1)
        for s in range(1, 37, 1):
            mnogo = '//*[@id="root"]/div/main/form/div/div[17]/div/div[1]/div[{}]/button[1]'.format(s)
            norm = '//*[@id="root"]/div/main/form/div/div[17]/div/div[1]/div[{}]/button[2]'.format(s)
            malo = '//*[@id="root"]/div/main/form/div/div[17]/div/div[1]/div[{}]/button[3]'.format(s)
            nety = '//*[@id="root"]/div/main/form/div/div[17]/div/div[1]/div[{}]/button[4]'.format(s)
            otvet = [mnogo, norm, malo, nety]
            if random_vosrast == v18_24:
                random_otvet = random.choices(otvet, weights=[5, 25, 64, 6])[0]
                driver.find_element(By.XPATH, random_otvet).click()
                time.sleep(0.2)
            elif random_vosrast == v25_34:
                random_otvet = random.choices(otvet, weights=[5, 36, 53, 6])[0]
                driver.find_element(By.XPATH, random_otvet).click()
                time.sleep(0.3)
            elif random_vosrast == v35_44:
                random_otvet = random.choices(otvet, weights=[7, 24, 68, 5])[0]
                driver.find_element(By.XPATH, random_otvet).click()
                time.sleep(0.4)
            elif random_vosrast == v45_54:
                random_otvet = random.choices(otvet, weights=[4, 47, 40, 9])[0]
                driver.find_element(By.XPATH, random_otvet).click()
                time.sleep(0.5)
            elif random_vosrast == v55_64:
                random_otvet = random.choices(otvet, weights=[8, 45, 20, 16])[0]
                driver.find_element(By.XPATH, random_otvet).click()
                time.sleep(0.7)
            else:
                random_otvet = random.choices(otvet, weights=[5, 55, 24, 16])[0]
                driver.find_element(By.XPATH, random_otvet).click()
                time.sleep(0.9)
        for l in range(18, 20, 1):
            for k in range(1, 37, 1):
                mnogo = '//*[@id="root"]/div/main/form/div/div[{}]/div/div[1]/div[{}]/button[1]'.format(l, k)
                norm = '//*[@id="root"]/div/main/form/div/div[{}]/div/div[1]/div[{}]/button[2]'.format(l, k)
                malo = '//*[@id="root"]/div/main/form/div/div[{}]/div/div[1]/div[{}]/button[3]'.format(l, k)
                nety = '//*[@id="root"]/div/main/form/div/div[{}]/div/div[1]/div[{}]/button[4]'.format(l, k)
                otvet = [mnogo, norm, malo, nety]
                if random_vosrast == v18_24:
                    random_otvet = random.choices(otvet, weights=[5, 65, 24, 6])[0]
                    driver.find_element(By.XPATH, random_otvet).click()
                    time.sleep(0.2)
                elif random_vosrast == v25_34:
                    random_otvet = random.choices(otvet, weights=[5, 66, 23, 6])[0]
                    driver.find_element(By.XPATH, random_otvet).click()
                    time.sleep(0.3)
                elif random_vosrast == v35_44:
                    random_otvet = random.choices(otvet, weights=[2, 74, 18, 5])[0]
                    driver.find_element(By.XPATH, random_otvet).click()
                    time.sleep(0.4)
                elif random_vosrast == v45_54:
                    random_otvet = random.choices(otvet, weights=[4, 67, 20, 9])[0]
                    driver.find_element(By.XPATH, random_otvet).click()
                    time.sleep(0.5)
                elif random_vosrast == v55_64:
                    random_otvet = random.choices(otvet, weights=[8, 65, 10, 16])[0]
                    driver.find_element(By.XPATH, random_otvet).click()
                    time.sleep(0.7)
                else:
                    random_otvet = random.choices(otvet, weights=[5, 65, 14, 16])[0]
                    driver.find_element(By.XPATH, random_otvet).click()
                    time.sleep(0.9)
        no_problem = '//*[@id="root"]/div/main/form/div/div[20]/div/div[1]/label[6]'
        neznau = '//*[@id="root"]/div/main/form/div/div[20]/div/div[1]/label[7]'
        last_otcet = [no_problem, neznau]
        random_last_otcet = random.choices(last_otcet, weights=[90, 10])[0]
        my_page = driver.find_element(By.XPATH, random_last_otcet).click()
        time.sleep(1)
        da_chast= '//*[@id="root"]/div/main/form/div/div[21]/div/div[1]/label[2]'
        da_vse = '//*[@id="root"]/div/main/form/div/div[21]/div/div[1]/label[3]'
        neto = '//*[@id="root"]/div/main/form/div/div[21]/div/div[1]/label[5]'
        tochno_last_otcet = [da_chast, da_vse, neto]
        random_tochno_last_otcet = random.choices(tochno_last_otcet, weights=[1, 2, 97])[0]
        my_page = driver.find_element(By.XPATH, random_tochno_last_otcet).click()
       # vremi = [11, 7, 23, 1]
       # random_vremi = random.choices(vremi)
       # time.sleep(random_vremi)
        time.sleep(20)
        my_page = driver.find_element(By.CSS_SELECTOR, '#root > div > main > form > div > div.SurveyPage-Buttons > button').click()
        time.sleep(10)
        print("количество пройденных анкет: " + str(i))
        time.sleep(1)
        my_page = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/section[1]/div/a').click()
        time.sleep(10)


if __name__ == "__main__":
    main()