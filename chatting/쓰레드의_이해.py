# import threading

# def my_function():
#     # 스레드에서 실행할 작업을 정의합니다.
#     print("Hello, I'm running in a thread!")

# # 스레드를 생성하고 시작합니다.
# thread = threading.Thread(target=my_function)
# thread.start()

import threading

def print_numbers():
    for i in range(1, 11):
        print(i)

def print_letters():
    for letter in 'abcdefghij':
        print(letter)

# 두 개의 스레드를 생성하고 시작합니다.
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)
thread1.start()
thread2.start()