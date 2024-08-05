from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


navegador = webdriver.Chrome(options=options)

# abrir navegador
navegador.get('https://forms.gle/u2DsS78Sp7GABkVq5')

pyautogui.sleep(5)

navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('Jose Oliveira')

pyautogui.sleep(1)

navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('JoseOliveira@gmail.com')

pyautogui.sleep(1)

navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys('Campo Limpo')

pyautogui.sleep(1)

navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('11934745245')

pyautogui.sleep(1)

navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys('nenhum')

pyautogui.sleep(3)

navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()

