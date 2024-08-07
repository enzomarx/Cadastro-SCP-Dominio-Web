import time
import pyautogui
import pandas as pd


tabela = pd.read_csv(r'C:\Users\EnzoVM\Downloads\enzo_extracted_updated.csv')
pyautogui.PAUSE = 1

pyautogui.hotkey('alt', 'a') #
pyautogui.hotkey('shift', 's')
pyautogui.click(x=438, y=170) #Volta para a primeira
pyautogui.click(x=356, y=246) #clica na data
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(x=451, y=280)

def inclui_sc(linha):
    time.sleep(3)  
    pyautogui.click(x=451, y=280)
    time.sleep(2)    
    pyautogui.click(266, 307)
    time.sleep(1)  
    pyautogui.press('tab')
    data = tabela.loc[linha, "data"]
    pyautogui.write(str(data))
    pyautogui.press('tab')
    pyautogui.write(str('179,28'))
    pyautogui.press('tab')
    time.sleep(1)  
    pyautogui.hotkey('shift', 'n') #aperta em incluir
    time.sleep(1)
    cpf = tabela.loc[linha, "cpf"]
    pyautogui.write(str(cpf))
    pyautogui.press('tab')
    pyautogui.write('83,67') #preenche participação
    pyautogui.press('tab')
    pyautogui.write('150') #quotas integralizadas
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('1') #valor da quota
    pyautogui.press('tab')
    pyautogui.write('150') #capital integralizado
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.hotkey('shift', 'n')

def inclui_ost():
    pyautogui.sleep(1)
    pyautogui.write(str("CNPJ"))
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('29,28') #quotas integralizadas
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('1') #valor da quota
    pyautogui.press('tab')
    pyautogui.write('29,28') #capital integralizado
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.hotkey('shift', 'g') 
    time.sleep(0.80)
    pyautogui.hotkey('shift', 'y') 
    time.sleep(0.80)
    time.sleep(0.80)    
    pyautogui.click(x=493, y=172) #seta
    time.sleep(0.80 )



    
for linha in range(len(tabela)):
    inclui_sc(linha)
    inclui_ost()