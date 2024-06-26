import time
import pyautogui 
import pandas as pd      

cont = 18
def ts0():
    time.sleep(1.5)
def ts():
    time.sleep(3)

def trocanumscp():
    ts()
    pyautogui.press('right')
    ts()
    pyautogui.press('backspace')
    time.sleep(1)
    pyautogui.press('backspace')

def prepambctrlcv():
    #ts()
    #pyautogui.click(x=1037, y=177) #clica em 
    pyautogui.click(x=732, y=458) #OK em ''este cód já existe''
    ts()
    pyautogui.click(x=1034, y=178) #clica em
    ts()
    pyautogui.click(x=463, y=176) #volta para a SCP 1
        
def criaracumul():
    global cont
    cont += 1  
    
    ts()
    pyautogui.rightClick(x=789, y=392) #abre menu de copiar
    ts0()    
    pyautogui.click(x=863, y=521) #clica em copiar registro
    ts()
    pyautogui.hotkey('shift', 'n') #aperta em novo
    ts()
    pyautogui.rightClick(x=789, y=392) #abre menu de colar
    ts0()
    pyautogui.click(x=863, y=545) #clica em colar registro
    ts()
    pyautogui.click(x=403, y=175)  #clica em código  
    ts()
    pyautogui.hotkey('del') #apaga código padrão
    ts()
    pyautogui.write(str(cont))
    ts()
    pyautogui.doubleClick(x=474, y=202) #clica no nome da SCP
    trocanumscp()
    ts()
    pyautogui.write(str(cont))
    ts()
    pyautogui.click(x=462, y=301) #clica na descrição da SCP
    trocanumscp()
    ts()
    pyautogui.write(str(cont))
    ts()
    pyautogui.click(x=362, y=332) #clica no sub menu Notas
    ts0()
    pyautogui.click(x=471, y=668) #clica na seleção de SCP
    ts()
    pyautogui.write(str(cont))
    ts()
    pyautogui.click(x=1036, y=244) #clica em gravar
    ts()
    ts()

for _ in range(25):   
    criaracumul()
    prepambctrlcv()