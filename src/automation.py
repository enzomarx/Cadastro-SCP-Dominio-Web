import pyautogui
import pandas as pd
import time

pyautogui.PAUSE = 0.80

pyautogui.click(x=1462, y=229) # resolução 1920 x 1080 125x
time.sleep(2)

tabela = pd.read_csv(r"C:\Users\PC\Desktop\Guia Erros.csv") # Seu CSV caminho

for linha in tabela.index:
    pyautogui.press('delete')
    pyautogui.press('delete')
    pyautogui.press('delete')
    pyautogui.press('delete')
    mat = tabela.loc[linha, "mat"]  # Acessa a primeira coluna (0-indexed)
    pyautogui.write(str(tabela.loc[linha, "mat"]))
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1.5)
    empresa = tabela.loc[linha, "empresa"]  # Supondo que 'MAT' é a segunda coluna
    pyautogui.write(str(tabela.loc[linha, "empresa"]))
    pyautogui.click(x=602, y=221)
    time.sleep(2)
    pyautogui.click(x=647, y=287)
    time.sleep(2)
    pyautogui.click(x=567, y=319)
    pyautogui.write("29122014")
    pyautogui.click(x=535, y=398)
    pyautogui.write('012024')
    pyautogui.click(x=688, y=286)  
    pyautogui.write('MEDICALMAIS SERVICOS EM SAUDE SCP MAT.')
    mat = tabela.loc[linha, "mat"]  # Acessa a primeira coluna (0-indexed)
    pyautogui.write(str(tabela.loc[linha, "mat"]))
    pyautogui.click(x=884, y=286)
    pyautogui.click(x=884, y=286)  
    pyautogui.doubleClick(x=675, y=434)
    pyautogui.write('MEDICALMAIS SERVICOS EM SAUDE')
    pyautogui.click(x=936, y=560)
    pyautogui.press('up')
    pyautogui.press('enter')
    time.sleep(0.50)
    pyautogui.click(x=1463, y=311)
    time.sleep(0.50)
    pyautogui.click(1030, 637)
    time.sleep(1.25)
 
    


