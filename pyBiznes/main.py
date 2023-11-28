from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

def main():
    driver = webdriver.Chrome()
    driver.get("https://forms.yandex.ru/u/6549a750eb614615820849ae/")
    for o in range(17):
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
            random_status = random.choices(status, weights=[25, 13, 1, 20, 28, 8, 5, 3])[0]
            driver.find_element(By.XPATH, random_status).click()
        else:
            random_status = random.choices(status, weights=[10, 5, 0.0002, 20, 60, 1, 1, 3])[0]
            driver.find_element(By.XPATH, random_status).click()
        time.sleep(0.5)
        nol_child = '//*[@id="root"]/div/main/form/div/div[6]/div/div[1]/label[1]'
        odin_child = '//*[@id="root"]/div/main/form/div/div[6]/div/div[1]/label[2]'
        dva_child = '//*[@id="root"]/div/main/form/div/div[6]/div/div[1]/label[3]'
        tri_child = '//*[@id="root"]/div/main/form/div/div[6]/div/div[1]/label[4]'
        deti = [nol_child, odin_child, dva_child, tri_child]
        if random_vosrast == v18_24:
            random_deti = random.choices(deti, weights=[50, 30, 20, 0])[0]
            driver.find_element(By.XPATH, random_deti).click()
        elif random_vosrast == v25_34:
            random_deti = random.choices(deti, weights=[30, 30, 30, 10])[0]
            driver.find_element(By.XPATH, random_deti).click()
        elif random_vosrast == v35_44:
            random_deti = random.choices(deti, weights=[40, 50, 5, 5])[0]
            driver.find_element(By.XPATH, random_deti).click()
        elif random_vosrast == v45_54:
            random_deti = random.choices(deti, weights=[30, 25, 35, 10])[0]
            driver.find_element(By.XPATH, random_deti).click()
        elif random_vosrast == v55_64:
            random_deti = random.choices(deti, weights=[10, 20, 40, 30])[0]
            driver.find_element(By.XPATH, random_deti).click()
        else:
            random_deti = random.choices(deti, weights=[5, 20, 30, 45])[0]
            driver.find_element(By.XPATH, random_deti).click()
        time.sleep(0.5)

        school = '//*[@id="root"]/div/main/form/div/div[7]/div/div[1]/label[1]'
        hich_school = '//*[@id="root"]/div/main/form/div/div[7]/div/div[1]/label[2]'
        koled = '//*[@id="root"]/div/main/form/div/div[7]/div/div[1]/label[3]'
        bakalavr = '//*[@id="root"]/div/main/form/div/div[7]/div/div[1]/label[4]'
        spez = '//*[@id="root"]/div/main/form/div/div[7]/div/div[1]/label[5]'
        science = '//*[@id="root"]/div/main/form/div/div[7]/div/div[1]/label[6]'
        inoe_2 = '//*[@id="root"]/div/main/form/div/div[7]/div/div[1]/label[7]'
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
        time.sleep(0.5)

        net_eda = '//*[@id="root"]/div/main/form/div/div[8]/div/div[1]/label[1]'
        net_odechda = '//*[@id="root"]/div/main/form/div/div[8]/div/div[1]/label[2]'
        net_stiralka = '//*[@id="root"]/div/main/form/div/div[8]/div/div[1]/label[3]'
        net_machina = '//*[@id="root"]/div/main/form/div/div[8]/div/div[1]/label[4]'
        net_kvartira = '//*[@id="root"]/div/main/form/div/div[8]/div/div[1]/label[5]'
        vst_est = '//*[@id="root"]/div/main/form/div/div[8]/div/div[1]/label[6]'
        mat_polochenie = [net_eda, net_odechda, net_stiralka, net_machina, net_kvartira, vst_est]
        if random_vosrast == v18_24:
            random_mat_polochenie = random.choices(mat_polochenie, weights=[0, 1, 5, 70, 20, 3])[0]
            driver.find_element(By.XPATH, random_mat_polochenie).click()
        elif random_vosrast == v25_34:
            random_mat_polochenie = random.choices(mat_polochenie, weights=[0, 2, 5, 60, 30, 3])[0]
            driver.find_element(By.XPATH, random_mat_polochenie).click()
        elif random_vosrast == v35_44:
            random_mat_polochenie = random.choices(mat_polochenie, weights=[0, 0, 10, 55, 32, 3])[0]
            driver.find_element(By.XPATH, random_mat_polochenie).click()
        elif random_vosrast == v45_54:
            random_mat_polochenie = random.choices(mat_polochenie, weights=[0, 1, 5, 60, 32, 3])[0]
            driver.find_element(By.XPATH, random_mat_polochenie).click()
        elif random_vosrast == v55_64:
            random_mat_polochenie = random.choices(mat_polochenie, weights=[0, 1, 5, 70, 22, 3])[0]
            driver.find_element(By.XPATH, random_mat_polochenie).click()
        else:
            random_mat_polochenie = random.choices(mat_polochenie, weights=[0, 0, 5, 80, 12, 3])[0]
            driver.find_element(By.XPATH, random_mat_polochenie).click()
        time.sleep(1)
        for i in range (1, 9, 1):# вклады
            est_sechas = '//*[@id="root"]/div/main/form/div/div[10]/div[2]/div[1]/div[{}]/button[1]'.format(i)
            est_v_etom_gody = '//*[@id="root"]/div/main/form/div/div[10]/div[2]/div[1]/div[{}]/button[2]'.format(i)
            nety_v_etom_gody = '//*[@id="root"]/div/main/form/div/div[10]/div[2]/div[1]/div[{}]/button[3]'.format(i)
            vkladi = [est_sechas, est_v_etom_gody, nety_v_etom_gody]
            if random_vosrast == v18_24:
                random_mat_vkladi = random.choices(vkladi, weights=[50, 13, 37])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
            elif random_vosrast == v25_34:
                random_mat_vkladi = random.choices(vkladi, weights=[45, 26, 29])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
            elif random_vosrast == v35_44:
                random_mat_vkladi = random.choices(vkladi, weights=[40, 30, 30])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
            elif random_vosrast == v45_54:
                random_mat_vkladi = random.choices(vkladi, weights=[15, 67, 18])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
            elif random_vosrast == v55_64:
                random_mat_vkladi = random.choices(vkladi, weights=[35, 35, 30])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
            else:
                random_mat_vkladi = random.choices(vkladi, weights=[30, 20, 50])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
        time.sleep(1)
        for i in range (1, 11, 1): # кредиты
            est_sechas = '//*[@id="root"]/div/main/form/div/div[12]/div[2]/div[1]/div[{}]/button[1]'.format(i)
            est_v_etom_gody = '//*[@id="root"]/div/main/form/div/div[12]/div[2]/div[1]/div[{}]/button[2]'.format(i)
            nety_v_etom_gody = '//*[@id="root"]/div/main/form/div/div[12]/div[2]/div[1]/div[{}]/button[3]'.format(i)
            vkladi = [est_sechas, est_v_etom_gody, nety_v_etom_gody]
            if random_vosrast == v18_24:
                random_mat_vkladi = random.choices(vkladi, weights=[30, 40, 30])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
            elif random_vosrast == v25_34:
                random_mat_vkladi = random.choices(vkladi, weights=[30, 30, 40])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
            elif random_vosrast == v35_44:
                random_mat_vkladi = random.choices(vkladi, weights=[40, 30, 30])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
            elif random_vosrast == v45_54:
                random_mat_vkladi = random.choices(vkladi, weights=[10, 47, 43])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
            elif random_vosrast == v55_64:
                random_mat_vkladi = random.choices(vkladi, weights=[10, 50, 40])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
            else:
                random_mat_vkladi = random.choices(vkladi, weights=[10, 58, 32])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
        time.sleep(1)
        for i in range (1, 5, 1): # cards
            est_sechas = '//*[@id="root"]/div/main/form/div/div[14]/div[2]/div[1]/div[{}]/button[1]'.format(i)
            est_v_etom_gody = '//*[@id="root"]/div/main/form/div/div[14]/div[2]/div[1]/div[{}]/button[2]'.format(i)
            nety_v_etom_gody = '//*[@id="root"]/div/main/form/div/div[14]/div[2]/div[1]/div[{}]/button[3]'.format(i)
            vkladi = [est_sechas, est_v_etom_gody, nety_v_etom_gody]
            if random_vosrast == v18_24:
                random_mat_vkladi = random.choices(vkladi, weights=[80, 15, 5])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
            elif random_vosrast == v25_34:
                random_mat_vkladi = random.choices(vkladi, weights=[75, 20, 5])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
            elif random_vosrast == v35_44:
                random_mat_vkladi = random.choices(vkladi, weights=[75, 20, 5])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
            elif random_vosrast == v45_54:
                random_mat_vkladi = random.choices(vkladi, weights=[70, 25, 5])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
            elif random_vosrast == v55_64:
                random_mat_vkladi = random.choices(vkladi, weights=[75, 20, 5])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
            else:
                random_mat_vkladi = random.choices(vkladi, weights=[80, 15, 5])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
        time.sleep(1)

        est = '//*[@id="root"]/div/main/form/div/div[16]/div/div[1]/label[1]'
        nety_sechas = '//*[@id="root"]/div/main/form/div/div[16]/div/div[1]/label[2]'
        nety_vobche = '//*[@id="root"]/div/main/form/div/div[16]/div/div[1]/label[3]'
        polsovalis_schetom = [est, nety_sechas, nety_vobche]
        if random_vosrast == v18_24:
            random_polsovalis_schetom = random.choices(polsovalis_schetom, weights=[80, 19, 1])[0]
            driver.find_element(By.XPATH, random_polsovalis_schetom).click()
        elif random_vosrast == v25_34:
            random_polsovalis_schetom = random.choices(polsovalis_schetom, weights=[83, 16, 1])[0]
            driver.find_element(By.XPATH, random_polsovalis_schetom).click()
        elif random_vosrast == v35_44:
            random_polsovalis_schetom = random.choices(polsovalis_schetom, weights=[73, 25, 2])[0]
            driver.find_element(By.XPATH, random_polsovalis_schetom).click()
        elif random_vosrast == v45_54:
            random_polsovalis_schetom = random.choices(polsovalis_schetom, weights=[80, 18, 2])[0]
            driver.find_element(By.XPATH, random_polsovalis_schetom).click()
        elif random_vosrast == v55_64:
            random_polsovalis_schetom = random.choices(polsovalis_schetom, weights=[75, 23, 2])[0]
            driver.find_element(By.XPATH, random_polsovalis_schetom).click()
        else:
            random_polsovalis_schetom = random.choices(polsovalis_schetom, weights=[70, 27, 3])[0]
            driver.find_element(By.XPATH, random_polsovalis_schetom).click()
        time.sleep(1)

        for i in range (1, 5, 1): # Пользовались ли Вы следующими типами дистанционного доступа к банковскому счету (расчетному счету, счету по вкладу, счету платежной карты) за последние 12 месяцев?
            da = '//*[@id="root"]/div/main/form/div/div[17]/div[2]/div[1]/div[{}]/button[1]'.format(i)
            Net = '//*[@id="root"]/div/main/form/div/div[17]/div[2]/div[1]/div[{}]/button[2]'.format(i)
            vkladi = [da, Net]
            if random_vosrast == v18_24:
                random_mat_vkladi = random.choices(vkladi, weights=[95, 5])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
            elif random_vosrast == v25_34:
                random_mat_vkladi = random.choices(vkladi, weights=[95, 5])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
            elif random_vosrast == v35_44:
                random_mat_vkladi = random.choices(vkladi, weights=[90, 10])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
            elif random_vosrast == v45_54:
                random_mat_vkladi = random.choices(vkladi, weights=[80, 20])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
            elif random_vosrast == v55_64:
                random_mat_vkladi = random.choices(vkladi, weights=[70, 30])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
            else:
                random_mat_vkladi = random.choices(vkladi, weights=[70, 30])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
        time.sleep(1)

        for i in range (1, 4, 1): #Какими из перечисленных страховых продуктов (услуг) Вы пользовались за последние 12 месяцев?
            est_sechas = '//*[@id="root"]/div/main/form/div/div[19]/div[2]/div[1]/div[{}]/button[1]'.format(i)
            est_v_etom_gody = '//*[@id="root"]/div/main/form/div/div[19]/div[2]/div[1]/div[{}]/button[2]'.format(i)
            nety_v_etom_gody = '//*[@id="root"]/div/main/form/div/div[19]/div[2]/div[1]/div[{}]/button[3]'.format(i)
            vkladi = [est_sechas, est_v_etom_gody, nety_v_etom_gody]
            if random_vosrast == v18_24:
                random_mat_vkladi = random.choices(vkladi, weights=[5, 65, 30])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
            elif random_vosrast == v25_34:
                random_mat_vkladi = random.choices(vkladi, weights=[5, 66, 29])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
            elif random_vosrast == v35_44:
                random_mat_vkladi = random.choices(vkladi, weights=[5, 65, 30])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
            elif random_vosrast == v45_54:
                random_mat_vkladi = random.choices(vkladi, weights=[10, 70, 20])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
            elif random_vosrast == v55_64:
                random_mat_vkladi = random.choices(vkladi, weights=[10, 65, 25])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
            else:
                random_mat_vkladi = random.choices(vkladi, weights=[10, 70, 20])[0]
                driver.find_element(By.XPATH, random_mat_vkladi).click()
        time.sleep(1)

        for i in range (1, 9, 1): #Насколько Вы удовлетворены работой/сервисом следующих финансовых организаций при оформлении и/или использовании финансовых услуг или в любых других случаях, когда Вы сталкивались с ними?
            polnosti_net = '//*[@id="root"]/div/main/form/div/div[22]/div/div[1]/div[{}]/button[1]'.format(i)
            skoree_net = '//*[@id="root"]/div/main/form/div/div[22]/div/div[1]/div[{}]/button[2]'.format(i)
            skoree_da = '//*[@id="root"]/div/main/form/div/div[22]/div/div[1]/div[{}]/button[3]'.format(i)
            polnosti_da = '//*[@id="root"]/div/main/form/div/div[22]/div/div[1]/div[{}]/button[4]'.format(i)
            hz = '//*[@id="root"]/div/main/form/div/div[22]/div/div[1]/div[{}]/button[5]'.format(i)
            otveta = [polnosti_net, skoree_net, skoree_da, polnosti_da, hz]
            if random_vosrast == v18_24:
                random_otveta = random.choices(otveta, weights=[2, 17, 52, 27, 2])[0]
                driver.find_element(By.XPATH, random_otveta).click()
            elif random_vosrast == v25_34:
                random_otveta = random.choices(otveta, weights=[2, 17, 47, 22, 2])[0]
                driver.find_element(By.XPATH, random_otveta).click()
            elif random_vosrast == v35_44:
                random_otveta = random.choices(otveta, weights=[2, 17, 52, 27, 2])[0]
                driver.find_element(By.XPATH, random_otveta).click()
            elif random_vosrast == v45_54:
                random_otveta = random.choices(otveta, weights=[2, 22, 42, 32, 2])[0]
                driver.find_element(By.XPATH, random_otveta).click()
            elif random_vosrast == v55_64:
                random_otveta = random.choices(otveta, weights=[2, 22, 42, 32, 2])[0]
                driver.find_element(By.XPATH, random_otveta).click()
            else:
                random_otveta = random.choices(otveta, weights=[2, 17, 57, 22, 2])[0]
                driver.find_element(By.XPATH, random_otveta).click()
        time.sleep(1)

        for s in range(1, 9, 1):#Насколько Вы доверяете следующим финансовым организациям?
            doveria_nol = '//*[@id="root"]/div/main/form/div/div[23]/div/div[1]/div[{}]/button[1]'.format(s)
            doveria_vseravno_net = '//*[@id="root"]/div/main/form/div/div[23]/div/div[1]/div[{}]/button[2]'.format(s)
            nemnogo_doveria = '//*[@id="root"]/div/main/form/div/div[23]/div/div[1]/div[{}]/button[3]'.format(s)
            verim = '//*[@id="root"]/div/main/form/div/div[23]/div/div[1]/div[{}]/button[4]'.format(s)
            ne_stalkivalsa = '//*[@id="root"]/div/main/form/div/div[23]/div/div[1]/div[{}]/button[5]'.format(s)
            urovni_doveria =[doveria_nol, doveria_vseravno_net, nemnogo_doveria, verim, ne_stalkivalsa]
            if random_vosrast == v18_24:
                random_urovni_doveria = random.choices(urovni_doveria, weights=[2, 17, 52, 27, 2])[0]
                driver.find_element(By.XPATH, random_urovni_doveria).click()
            elif random_vosrast == v25_34:
                random_urovni_doveria = random.choices(urovni_doveria, weights=[2, 17, 47, 22, 2])[0]
                driver.find_element(By.XPATH, random_urovni_doveria).click()
            elif random_vosrast == v35_44:
                random_urovni_doveria = random.choices(urovni_doveria, weights=[2, 17, 52, 27, 2])[0]
                driver.find_element(By.XPATH, random_urovni_doveria).click()
            elif random_vosrast == v45_54:
                random_urovni_doveria = random.choices(urovni_doveria, weights=[2, 22, 42, 32, 2])[0]
                driver.find_element(By.XPATH, random_urovni_doveria).click()
            elif random_vosrast == v55_64:
                random_urovni_doveria = random.choices(urovni_doveria, weights=[2, 22, 42, 32, 2])[0]
                driver.find_element(By.XPATH, random_urovni_doveria).click()
            else:
                random_urovni_doveria = random.choices(urovni_doveria, weights=[2, 12, 52, 22, 2])[0]
                driver.find_element(By.XPATH, random_urovni_doveria).click()
        time.sleep(1)

        for s in range(1, 20, 1): #Насколько Вы удовлетворены следующими продуктами/услугами финансовых организаций при их оформлении и/или использовании или в любых других случаях, когда Вы сталкивались с ними?
            doveria_nol = '//*[@id="root"]/div/main/form/div/div[24]/div/div[1]/div[{}]/button[1]'.format(s)
            doveria_vseravno_net = '//*[@id="root"]/div/main/form/div/div[24]/div/div[1]/div[{}]/button[2]'.format(s)
            nemnogo_doveria = '//*[@id="root"]/div/main/form/div/div[24]/div/div[1]/div[{}]/button[3]'.format(s)
            verim = '//*[@id="root"]/div/main/form/div/div[24]/div/div[1]/div[{}]/button[4]'.format(s)
            ne_stalkivalsa = '//*[@id="root"]/div/main/form/div/div[24]/div/div[1]/div[{}]/button[5]'.format(s)
            urovni_doveria =[doveria_nol, doveria_vseravno_net, nemnogo_doveria, verim, ne_stalkivalsa]
            if random_vosrast == v18_24:
                random_urovni_doveria = random.choices(urovni_doveria, weights=[2, 17, 52, 27, 2])[0]
                driver.find_element(By.XPATH, random_urovni_doveria).click()
            elif random_vosrast == v25_34:
                random_urovni_doveria = random.choices(urovni_doveria, weights=[2, 17, 47, 22, 2])[0]
                driver.find_element(By.XPATH, random_urovni_doveria).click()
            elif random_vosrast == v35_44:
                random_urovni_doveria = random.choices(urovni_doveria, weights=[2, 17, 52, 27, 2])[0]
                driver.find_element(By.XPATH, random_urovni_doveria).click()
            elif random_vosrast == v45_54:
                random_urovni_doveria = random.choices(urovni_doveria, weights=[2, 22, 42, 32, 2])[0]
                driver.find_element(By.XPATH, random_urovni_doveria).click()
            elif random_vosrast == v55_64:
                random_urovni_doveria = random.choices(urovni_doveria, weights=[2, 22, 42, 32, 2])[0]
                driver.find_element(By.XPATH, random_urovni_doveria).click()
            else:
                random_urovni_doveria = random.choices(urovni_doveria, weights=[2, 17, 57, 22, 2])[0]
                driver.find_element(By.XPATH, random_urovni_doveria).click()
        time.sleep(1)

        for s in range(1, 14, 1): #Если говорить о Вашем населенном пункте, насколько Вы удовлетворены...?
            doveria_nol = '//*[@id="root"]/div/main/form/div/div[25]/div/div[1]/div[{}]/button[1]'.format(s)
            doveria_vseravno_net = '//*[@id="root"]/div/main/form/div/div[25]/div/div[1]/div[{}]/button[2]'.format(s)
            nemnogo_doveria = ('//*[@id="root"]/div/main/form/div/div[25]/div/div[1]/div[{}]/button[3]').format(s)
            verim = '//*[@id="root"]/div/main/form/div/div[25]/div/div[1]/div[{}]/button[4]'.format(s)
            ne_stalkivalsa = '//*[@id="root"]/div/main/form/div/div[25]/div/div[1]/div[{}]/button[5]'.format(s)
            urovni_doveria =[doveria_nol, doveria_vseravno_net, nemnogo_doveria, verim, ne_stalkivalsa]
            if random_vosrast == v18_24:
                random_urovni_doveria = random.choices(urovni_doveria, weights=[2, 17, 52, 27, 2])[0]
                driver.find_element(By.XPATH, random_urovni_doveria).click()
            elif random_vosrast == v25_34:
                random_urovni_doveria = random.choices(urovni_doveria, weights=[2, 17, 47, 22, 2])[0]
                driver.find_element(By.XPATH, random_urovni_doveria).click()
            elif random_vosrast == v35_44:
                random_urovni_doveria = random.choices(urovni_doveria, weights=[2, 17, 52, 27, 2])[0]
                driver.find_element(By.XPATH, random_urovni_doveria).click()
            elif random_vosrast == v45_54:
                random_urovni_doveria = random.choices(urovni_doveria, weights=[2, 22, 42, 32, 2])[0]
                driver.find_element(By.XPATH, random_urovni_doveria).click()
            elif random_vosrast == v55_64:
                random_urovni_doveria = random.choices(urovni_doveria, weights=[2, 22, 42, 32, 2])[0]
                driver.find_element(By.XPATH, random_urovni_doveria).click()
            else:
                random_urovni_doveria = random.choices(urovni_doveria, weights=[2, 17, 57, 22, 2])[0]
                driver.find_element(By.XPATH, random_urovni_doveria).click()
        time.sleep(1)

        for s in range(1, 7, 1): #Какие каналы обслуживание есть практически везде в Вашем населенном пункте, а каких не хватает?
            doveria_nol_ = '//*[@id="root"]/div/main/form/div/div[26]/div[2]/div[1]/div[{}]/button[1]'.format(s)
            doveria_vseravno_net_ = '//*[@id="root"]/div/main/form/div/div[26]/div[2]/div[1]/div[{}]/button[2]'.format(s)
            nemnogo_doveria_ = '//*[@id="root"]/div/main/form/div/div[26]/div[2]/div[1]/div[{}]/button[3]'.format(s)
            verim_ = '//*[@id="root"]/div/main/form/div/div[26]/div[2]/div[1]/div[{}]/button[4]'.format(s)
            ne_stalkivalsa_ = '//*[@id="root"]/div/main/form/div/div[26]/div[2]/div[1]/div[{}]/button[5]'.format(s)
            urovni_doveria_ =[doveria_nol_, doveria_vseravno_net_, nemnogo_doveria_, verim_, ne_stalkivalsa_]
            if random_vosrast == v18_24:
                random_urovni_doveria_ = random.choices(urovni_doveria_, weights=[1, 1, 14, 70, 14])[0]
                driver.find_element(By.XPATH, random_urovni_doveria_).click()

            elif random_vosrast == v25_34:
                random_urovni_doveria_ = random.choices(urovni_doveria_, weights=[1, 1, 19, 60, 19])[0]
                driver.find_element(By.XPATH, random_urovni_doveria_).click()

            elif random_vosrast == v35_44:
                random_urovni_doveria_ = random.choices(urovni_doveria_, weights=[1, 1, 14, 70, 14])[0]
                driver.find_element(By.XPATH, random_urovni_doveria_).click()

            elif random_vosrast == v45_54:
                random_urovni_doveria_ = random.choices(urovni_doveria_, weights=[1, 1, 19, 60, 19])[0]
                driver.find_element(By.XPATH, random_urovni_doveria_).click()

            elif random_vosrast == v55_64:
                random_urovni_doveria_ = random.choices(urovni_doveria_, weights=[1, 1, 24, 60, 14])[0]
                driver.find_element(By.XPATH, random_urovni_doveria_).click()

            else:
                random_urovni_doveria_ = random.choices(urovni_doveria_, weights=[1, 1, 26, 55, 17])[0]
                driver.find_element(By.XPATH, random_urovni_doveria_).click()
        if random_vosrast == v18_24:
            time.sleep(95)


        elif random_vosrast == v25_34:
            time.sleep(103)


        elif random_vosrast == v35_44:
            time.sleep(111)


        elif random_vosrast == v45_54:
            time.sleep(117)


        elif random_vosrast == v55_64:
            time.sleep(127)


        else:
            time.sleep(138)

        driver.find_element(By.CSS_SELECTOR,'#root > div > main > form > div > div.SurveyPage-Buttons > button').click()
        #time.sleep(10)
        print("количество пройденных анкет: " + str(o))
        time.sleep(10)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/section[1]/div/a').click()
        time.sleep(10)


if __name__ == "__main__":
    main()