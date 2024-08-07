import pyautogui
import time

try:
    while True:
        # Obtém a posição atual do cursor
        x, y = pyautogui.position()
        
        # Move o cursor para uma nova posição
        pyautogui.moveTo(x + 2, y + 2)
        
        # Espera 5 segundos antes de mover o cursor novamente
        time.sleep(5)
except KeyboardInterrupt:
    print("\nPrograma encerrado pelo usuário.")
