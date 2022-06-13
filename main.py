from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

URL_SITE = 'http://sistemas.migracion.gob.bo/reservasweb/#/reservaweb'
XPATH_CITY = '//div[@class="row mt-3"]/div[10]//a/text()'

# function
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
driver_path = '.\chromedriver.exe'


def get_html():
    driver = webdriver.Chrome(driver_path, chrome_options=options)

    # inicial pantalla
    driver.set_window_position(0, 0)
    driver.maximize_window()
    time.sleep(1)

    # abrir pagina
    driver.get(URL_SITE)

    try:
        # Cerrando alerta del sitio
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,  '//div[@class="modal-body"]//a[1]'))).click()

        # Ingresando a pasaporte
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.btn btn-outline-info mr-2'.replace(' ', '.')))).click()

        # Ingresar a registro
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.btn btn-primary'.replace(' ', '.')))).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//form//div[@class="row"][2]//div[@class="col-12 col-md-4"]//div[@class="form-group"][1]//input[@class="form-control"]')))\
            .send_keys('Gildder')

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//form//div[@class="row"][2]//div[@class="col-12 col-md-4"]//div[@class="form-group"][2]//input[@class="form-control"]')))\
            .send_keys('Guerrero')

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//form//div[@class="row"][2]//div[@class="col-12 col-md-4"]//div[@class="form-group"][3]//input[@class="form-control"]')))\
            .send_keys('Ramirez')

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//form//div[@class="row"][2]//div[@class="col-12 col-md-8"]//div[@class="col-12 col-md-4"]//select[@class="custom-select"]')))\
            .send_keys('CEDULA DE IDENTIDAD')

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//form//div[@class="row"][2]//div[@class="col-12 col-md-8"]//div[@class="col-12 col-md-5"]//input[@class="form-control"]')))\
            .send_keys('7734247')

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//form//div[@class="row"][2]//div[@class="col-12 col-md-8"]//div[@class="row form-group"][2]//input[@id="tooltip-target-1"]')))\
            .send_keys('gilberet@hotmail.com')

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//form//div[@class="row"][2]//div[@class="col-12 col-md-8"]//div[@class="row form-group"][2]//div[@class="col-12 col-md-6"][2]//input')))\
            .send_keys('60991648')

        fecha = '//form//div[@class="row"][2]//div[@class="col-12 col-md-8"]//div[@class="row form-group"][3]//div[@class="col-12 col-md-3"][1]//select//option[contains(.,"-")]/@value'
        horas = '//form//div[@class="row"][2]//div[@class="col-12 col-md-8"]//div[@class="row form-group"][3]//div[@class="col-12 col-md-3"][2]//select//option[contains(.,":")]/text()'
        time.sleep(10)
    finally:
        driver.quit()


# main


def run():
    get_html()


if __name__ == '__main__':
    run()
