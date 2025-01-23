import threading

#쓰레드에서 args를 사용하는 방법

# 첫번째 실행할 쓰레드 함수
def first_thread(num,num2):
    #print("first_thread function START")    
    for i in range(num +  num2):
        print("+")    
    #print("first_thread function END")

# 두번째 실행할 쓰레드 함수
def second_thread(num,num2): 
    #print("second_thread function START")
    for i in range(num + num2):
        print("-") 
    #print("second_thread function END")

# thread 생성(각 숫자를 5회 출력)
thread1 = threading.Thread(target=first_thread, args=(300,500))
thread2 = threading.Thread(target=second_thread, args=(300,500))

# thread 시작
thread1.start()
thread2.start()

