import pyautogui
from time import sleep
import threading
import keyboard

class Auto_Clicker():
    def __init__(self, interval):
        self.interval = interval
        self.running = False


    def start_clicking(self):
        self.running = True 
        while self.running:
            pyautogui.click()
            sleep(self.interval)

    def stop_clicking(self):
        self.running = False
    
def alternar_autoclicker(clicker):
    if not clicker.running:
        print("--> AutoClicker INICIADO")
        threading.Thread(target=clicker.start_clicking, daemon=True).start()
    else:
        print("--> AutoClicker PARADO")
        clicker.stop_clicking()

if __name__ == '__main__':
    interval = float(input("Digite o intervalo que deseja (em segundos):"))
    clicker = Auto_Clicker(interval)


    print("\nPressione 'Q' para iniciar/parar o autoclicker")
    print("Pressione 'ESC' para fechar o programa totalmente\n")

    keyboard.add_hotkey("q", lambda: alternar_autoclicker(clicker))

    keyboard.wait("esc")
    print('Saindo do programa')