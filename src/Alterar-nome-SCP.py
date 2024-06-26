import pandas as pd
import pyautogui
import time

time.sleep(4)
pyautogui.PAUSE = 1

tabela = pd.read_csv(r'C:\Users\PC\Desktop\Cadastro-SCP-Dominio-Web\data\matsocioscp.csv')

for linha in tabela.index:
    pyautogui.click(1089, 209) #clica em Editar
    mat = tabela.loc[linha, "mat"]
    pyautogui.write(str(tabela.loc[linha, "mat"]))
    pyautogui.hotkey("shift", "ctrl", "left", "left", "left", "left", "left", "left")
    socio = tabela.loc[linha, "SOCIO"]
    pyautogui.write(str(tabela.loc[linha, "SOCIO"]))
    pyautogui.click(x=1036, y=244) #clica em gravar


