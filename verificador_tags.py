#%%

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager as Chrome
import pandas as pd
import time
import pyautogui as pg
import pyperclip as pc

def abrir_chrome():

    tags=["P2UCYLG9Y","LQCP2QPPR","2G0PLPPY8","LLYYG0PC","QYUR8P0CL","8P8PLQUGC","YQ9CLGR82","PGRR0YVLQ","2QU8YCGR2","PVQUQCGU","90PYRV8PJ","VGPCV9UG","9J9YCV8GG","LGJ2VR29","9Y2RP2C80","Jonata CR","YYL2C00J0","8U0VL98CL","PQGLQ880P","J208UP902","2888R8QQ8","2Q9QP0","9VQQ28YJJ"]
    #iniciar inserção de tags manualmente, mas posteriormente inserir analise via planilha


    for tag in tags:
        driver = webdriver.Chrome(Chrome().install())
        driver.get(f"https://royaleapi.com/player/{tag}")
        time.sleep(2)
        campo_pesquisa = driver.find_elements_by_css_selector("h1.ui    header")


        if (campo_pesquisa == ""): 
            print(f"a tag {tag} é inválida")
        else:
            print(f"a tag {tag} é válida")

    
    #selecionar url
    # pg.keyDown("ctrl")
    # pg.press("l")
    # pg.keyUp("ctrl")
    
    # time.sleep(3)
    
    #copiar url
    # pg.keyDown("ctrl")
    # pg.press("c")
    # pg.keyUp("ctrl")
    
    
    # campo_pesquisa = pc.paste()
    # time.sleep(3)
    # print(campo_pesquisa)



abrir_chrome()
# %%
