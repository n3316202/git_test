import random
class UpDownGame:
    def __init__(self):
        self.answer = 0
        self.attemps = 0

    def set_answer(self):
        self.answer = random.randint(1,100)
    
    def input_answer(self):
        
        while True:
            try:
                self.answer = int(input("1부터 100 사이의 숫자를 입력하세요.> "))
                break
            except:
                print("잘못된 입력입니다")
                print("1부터 100 사이의 숫자를 입력하세요.")
        
    def run(self):
        self.set_answer()
        print("정답(테스트용 나중에 주석 처리 예정정) : ",self.answer)

        while self.attemps < 10:
            self.attemps += 1
            user_input = int(input("1부터 100 사이의 숫자를 입력하세요.> "))
            
            if user_input == self.answer:
                print("정답입니다.")
                break
            elif user_input > self.answer:
                print("Down")
            else:
                print("Up")
        
        print("시도 횟수 : ",self.attemps)

updown_game = UpDownGame()
updown_game.run()