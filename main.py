from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

att = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service = att)

navegador.get("https://web.whatsapp.com/")

contatos = ['Meu numero']
mensagem = """Testando automatizacao basica Whatssap
Apenas um teste """

def clicar(i):
    elemento = navegador.find_element('xpath',f'{i}').click()
    return elemento
def texto(i,texto):
    elemento = navegador.find_element('xpath',f'{i}').send_keys(f"{texto}")
    return elemento
def enter(i):
    elemento = navegador.find_element('xpath',f'{i}').send_keys(Keys.ENTER)
    return elemento
clicar('//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span')
texto('//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p','Meu numero')
enter('//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p')
texto('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]',mensagem)
for contador in range(0,10):
    cnt = f"Contando: {contador}"
    elemento = navegador.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys(cnt)
    enter('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')
time.sleep(2)
