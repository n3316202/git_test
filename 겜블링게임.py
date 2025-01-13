import random

class Person:
    def __init__(self, name):
        self.name = name
        self.list_numbers = []
    
    def set_list_numbers(self):
        input(self.name+ "의 차례입니다. <Enter> 키를 눌러주세요...")
        self.list_numbers = [random.randint(1, 3) for i in range(3)]
        print(self.name + "의 숫자는 " + str(self.list_numbers) + "입니다.")
    
    def get_list_numbers(self):
        return self.list_numbers



def main():

    while True:
        try:
            # 두 사람의 이름을 입력받음
            player1_name = input("첫 번째 사람의 이름을 입력하세요: ")
            player2_name = input("두 번째 사람의 이름을 입력하세요: ")
            break
        except:
            print("잘못된 입력입니다. 다시 입력하세요")
            continue
    
    # 두 사람의 Person 객체 생성
    tuple_player = (Person(player1_name), Person(player2_name))

    is_stop = False
    while True:
        
        for player in tuple_player:
            player.set_list_numbers()
            
            if len(set(player.get_list_numbers())) == 1:# 세 숫자가 모두 같으면
                print(player.name +  "가 이겼습니다!" + str(player.get_list_numbers()))
                is_stop = True
                break

        if is_stop:
            break 

if __name__ == "__main__":
    main()