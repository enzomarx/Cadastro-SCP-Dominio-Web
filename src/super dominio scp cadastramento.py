import pyautogui
import pandas as pd
import time
pyautogui.PAUSE = 0.70
tabela = pd.read_csv(r'C:\Users\PC\Desktop\csv para cadastro scp.csv')
time.sleep(5)
#Iniciar Dentro do Dominio
pyautogui.click(x=289, y=60)
pyautogui.click(x=362, y=298)
pyautogui.click(x=657, y=226)
#Loop principal
for linha in tabela.index:
    pyautogui.click(x=1461, y=271)
    time.sleep(1)
    pyautogui.click(x=606, y=222)
    pyautogui.write(str(tabela.loc[linha, "MAT"]))
    pyautogui.press('enter')
    time.sleep(1)
    #pyautogui.click(x=576, y=319)
    #pyautogui.write(str(tabela.loc[linha, "DATA"]))
    pyautogui.click(x=843, y=283)
    pyautogui.write(str(tabela.loc[linha, "SOCIO"]))
    pyautogui.click(x=1470, y=312)
    pyautogui.click(x=1061, y=608)
    time.sleep(1)
