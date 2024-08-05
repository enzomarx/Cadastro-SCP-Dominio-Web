import time
import pyautogui
import pandas as pd


tabela = pd.read_csv(r"C:\Users\PC\Desktop\DATAS-SCP1.csv")
pyautogui.PAUSE = 1

time.sleep(1)
pyautogui.hotkey('alt', 'a')
pyautogui.hotkey('shift', 's')
pyautogui.click(x=438, y=170) #Volta para a primeira

def inclui_data(linha):
    time.sleep(0.2)
    pyautogui.hotkey('shift', 'e')
    mat = tabela.loc[linha, "mat"]
    pyautogui.write(str(mat))
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('del')
    data = tabela.loc[linha, "data"]
    pyautogui.write(str(data))
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.hotkey('shift', 'g')
    pyautogui.hotkey('shift', 'y')
    time.sleep(0.2)
    pyautogui.click(x=491, y=173)

for linha in range(len(tabela)):
    inclui_data(linha)