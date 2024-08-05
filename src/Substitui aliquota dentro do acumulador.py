import pandas as pd
import time
import pyautogui


def ts0():
    time.sleep(1.7)
def ts():
    time.sleep(4)
def ts00():
    time.sleep(1)    

def mudaliqt(): 
    ts()     
    pyautogui.click(x=505, y=333) #clica botão SPED
    ts0()
    pyautogui.hotkey('shift', 'u') #excluir aliquota
    ts0()  
    pyautogui.click(x=790, y=646) #inclui aliquota
    ts0()
    pyautogui.press('Down') #escolhe aliquota
    ts0()
    pyautogui.press('tab') #passa para prox campo
    ts00()
    pyautogui.press('tab') #passa para prox campo
    ts0()
    pyautogui.write('0') 
    ts0()
    pyautogui.press('right')
    ts0()
    pyautogui.write('65')
    ts0()
    pyautogui.press('tab') #passa para prox campo
    ts0()
    pyautogui.write('3')
    ts0()
    pyautogui.click(x=1036, y=244) #clica em gravar
    ts0()
    pyautogui.click(x=803, y=452) #lida com a vigência
    ts()
    pyautogui.hotkey('shift', 'c')
    ts0()
    pyautogui.click(x=519, y=177) #passa para o prox
    ts0()
    
for _ in range(5):
    mudaliqt()
        
