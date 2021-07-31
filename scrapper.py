#%%

from bs4 import BeautifulSoup as bsoup
import re
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager as Chrome
import pyautogui as pg



    


def cadastros_clan_lol():
    
    tags=["P2UCYLG9Y", "LQCP2QPPR","8P8PLQUGC", "LLYYG0PC","QYUR8P0CL","YQ9CLGR82","PGRR0YVLQ","2QU8YCGR2","PVQUQCGU","90PYRV8PJ","VGPCV9UG","9J9YCV8GG","LGJ2VR29","9Y2RP2C80","Jonata CR","YYL2C00J0","8U0VL98CL","PQGLQ880P","J208UP902","2888R8QQ8","2Q9QP0","9VQQ28YJJ"]
    
    with open ('cadastros.csv','w') as cadastros: 
        escritor = csv.writer(cadastros, delimiter=",")
        for tag in tags:
            driver = webdriver.Chrome(Chrome().install())
            driver.get(f"https://royaleapi.com/player/{tag}")
            content = driver.page_source.encode("utf-8").strip() #pegar conteúdo da página
            soup = bsoup(content,'lxml') #realizar parse do conteúdo em content
            title = soup.find("h1", class_="header").text.strip()
            images = soup.find_all("img", class_= ["ui", "small","image"])
            image_link = images[2]['src'].strip()

            print(title)
            print(image_link)
            try:
                escritor.writerow([title, tag, image_link])
            except Exception as e:
                print(e)

            #remover emojis        
            print("Sucesso!")
            driver.quit()
            
            
            # insert_csv_data(title, tag, image_link)





# def insert_csv_data(title, tag, image_link):
    
   
        
      


    

cadastros_clan_lol()
# %%

# %%
