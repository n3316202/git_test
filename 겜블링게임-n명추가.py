import random

class Person:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def turn(self):
        # 턴이 돌아오면 Enter키 입력받기
        input(f"[{self.name}]:")
    
    def random_num(self):
        # 랜덤숫자 3개 생성 후 일치하는지 확인
        num = [random.randint(1, 3) for _ in range(3)]
        print("\t".join(map(str, num)))
        
        # 모든 숫자가 일치하는지 확인
        return num[0] == num[1] == num[2]

class GamblingGame:
    def __init__(self):
        # 게임에 참여할 선수 숫자 입력
        num = int(input("갬블링 게임에 참여할 선수 숫자>> "))
        self.person = []
        
        # 선수들의 이름 입력 받기
        for i in range(num):
            name = input(f"{i + 1}번째 선수 이름>> ")
            self.person.append(Person(name))
    
    def run(self):
        while True:
            for p in self.person:
                p.turn()  # Enter 키를 입력받기
                
                if p.random_num():
                    print(f"{p.get_name()}님이 이겼습니다!")
                    return
                else:
                    print("아쉽군요!")

# 게임 실행
if __name__ == "__main__":
    game = GamblingGame()
    game.run()