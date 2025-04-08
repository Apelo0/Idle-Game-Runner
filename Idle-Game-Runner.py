import ctypes
import time
import threading

def show_message():
    ctypes.windll.user32.MessageBoxW(0, "Game Started!", "Idle Game Runner", 1)

def run_background():
    while True:
        time.sleep(60)

if __name__ == "__main__":
    show_message()
    bg_thread = threading.Thread(target=run_background, daemon=True)
    bg_thread.start()
    while True:
        time.sleep(3600)
