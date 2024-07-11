import pyautogui
import time

pyautogui.PAUSE = 1.20
# Iterar 1500 vezes
for _ in range(1550):
    pyautogui.click(x=722, y=222)
    pyautogui.click(x=571, y=360)
    pyautogui.click(x=529, y=317)
    pyautogui.write('30/12/2014')
    pyautogui.click(x=450, y=424)
    pyautogui.click(x=454, y=453)
    pyautogui.click(x=450, y=728)
    pyautogui.click(x=648, y=757)
    pyautogui.write('LIVRO DIARIO SCP')
    pyautogui.click(x=1456, y=313)
    pyautogui.click(x=1056, y=609)
    time.sleep(2)  
