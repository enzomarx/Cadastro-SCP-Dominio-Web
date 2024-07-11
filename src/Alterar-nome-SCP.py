import pandas as pd
import pyautogui
import time
        

def ts():
    time.sleep(1.5)

time.sleep(2)    

tabela = pd.read_csv(r'C:\Users\Winlitepro\Desktop\Cadastro-SCP-Dominio-Web\data\matsocioscp.csv')


for linha in tabela.index:
    pyautogui.click(1089, 209) #clica em Editar
    ts()
    mat = tabela.loc[linha, "mat"]
    pyautogui.write(str(mat))
    ts()
    pyautogui.press("tab")
    ts()
    pyautogui.press("tab")
    ts()
    pyautogui.press("backspace")
    ts()
    socio = tabela.loc[linha, "socio"]
    pyautogui.write(str(socio))
    ts()
    pyautogui.write(" SCP ")
    ts()
    pyautogui.write(str(mat))
    ts()
    pyautogui.click(x=1082, y=244) #clica em gravar
    ts()
    pyautogui.click(x=750, y=462) #clica em yes
    time.sleep(3)


