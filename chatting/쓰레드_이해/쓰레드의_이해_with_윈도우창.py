import pyautogui
import time
import threading


def print_numbers():
    for i in range(10):
        time.sleep(1)
        print(i)

thread1 = threading.Thread(target=print_numbers)
thread1.start()

pyautogui.alert('코딩유치원 자주 찾아와주세요.')




