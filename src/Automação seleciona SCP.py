import pyautogui
import pandas as pd
import time

def ts0(): # tempo de espera de 0.3 segundos
    time.sleep(0.3)


def ts(): # tempo de espera de 1.5 segundos
    time.sleep(1.5)
    
def abrdmn(): # Abre domínio
    pyautogui.press("win")
    ts()
    pyautogui.write("https://www.dominioweb.com.br/")
    ts()
    pyautogui.press("enter")
    ts()
    pyautogui.click(x=639, y=361)
    ts()
    pyautogui.write("login")
    ts()
    pyautogui.press("tab")
    ts()
    pyautogui.write("Senha")
    ts()
    pyautogui.press("enter")
    
def lgnusr(): # Faz login de usuário
    ts()
    pyautogui.doubleClick(x=470, y=202)
    time.sleep(5)
    pyautogui.write("USUARIO")
    ts()
    pyautogui.press("tab")
    ts()
    pyautogui.write("SENHA")
    ts()
    pyautogui.press("enter")
    
def abrrelscp(): # Falta mapear
    ts()

def mrcscpbpc(): # Marca SCP por lote
    time.sleep(4.7)   
    ts0()
    pyautogui.click(x=507, y=578) #1
    ts0()    
    pyautogui.click(x=507, y=561)
    ts0()
    pyautogui.click(x=507, y=544)
    ts()
    pyautogui.click(x=507, y=527)
    ts()
    pyautogui.click(x=507, y=510)
    ts()
    pyautogui.click(x=507, y=493)
    ts()
    pyautogui.click(x=507, y=476)
    ts0()
    pyautogui.click(x=507, y=459)
    ts0()
    pyautogui.click(x=507, y=442)
    ts0()
    pyautogui.click(x=507, y=425) #10
    ts0()
    pyautogui.click(x=507, y=408)
    ts0()
    pyautogui.click(x=507, y=391)
    ts0()
    pyautogui.click(x=507, y=374)
    ts0()
    pyautogui.click(x=507, y=357)
    ts0()
    pyautogui.click(x=507, y=340)
    ts0()
    pyautogui.click(x=507, y=323)
    ts0()
    pyautogui.click(x=507, y=306)
    ts()
    pyautogui.click(x=845, y=283)

for linha in range(30):
    mrcscpbpc()
       
    
        
    

  