from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

### version amelioré de ce meme code 

freebitcoin = webdriver.Chrome()

freebitcoin.get("https://freebitco.in/")

## Attendre jusqu'à ce que l'élément de bannière apparaisse (no thanks, allow) (timeout de 10 secondes)
def pass_banner(xpath):
    wait = WebDriverWait(freebitcoin, 10)
    no_thanks_banner_home = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    no_thanks_banner_home.click()



#passer le banner
pass_banner('/html/body/div[17]/div[1]/div[2]/div/div[1]')

# appuyer sur le boutton login
login_button= freebitcoin.find_element(By.XPATH, "/html/body/div[2]/div/nav/section/ul/li[10]/a")
login_button.click()


#####   authentification    #####
Email_address_auth= freebitcoin.find_element(By.XPATH, "/html/body/div[4]/div/div/div[3]/div[4]/div/fieldset/div/div[2]/div/input")
password_auth=freebitcoin.find_element(By.XPATH, "/html/body/div[4]/div/div/div[3]/div[4]/div/fieldset/div/div[3]/div/input")
Email_address_auth.send_keys("boulmelh.mohamed.rafik@gmail.com")
password_auth.send_keys("1zTWem3CzKNPaStm")

##login
login= freebitcoin.find_element(By.XPATH, "/html/body/div[4]/div/div/div[3]/div[4]/div/fieldset/div/div[5]/div/p/button")
login.click()


pass_banner('/html/body/div[24]/div[1]/div[2]/div/div[1]')



time.sleep(1500)

 
#/html/body/div[17]/div[1]/div[2]/div/div[1]
#login: boulmelh.mohamed.rafik@gmail.com /html/body/div[4]/div/div/div[3]/div[4]/div/fieldset/div/div[5]/div/p/button
#password : 1zTWem3CzKNPaStm