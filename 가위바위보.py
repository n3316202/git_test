import random


class RspGame:
    def __init__(self):
        
        self.rsp_list = ['가위','바위','보']

        self.dic_rsp_result = {
            '가위': ('바위',"승"), 
            '바위': ('보',"승"),
            '보': ('가위',"승"),
        }

        self.computer = None
        self.user = None

    def set_rsp(self):
        
        while True:
            try:
                self.user = input("가위 바위 보 중에 하나를 입력하세요.> ")
                if self.user in self.dic_rsp_result.keys():
                    break
                print("잘못된 입력입니다. 다시 입력하세요.")    
            except:
                print("잘못된 입력입니다. 다시 입력하세요.")
                continue
            
        self.computer = random.choice(self.rsp_list)


    def rsp_reslut(self):

        if self.computer == self.user:
            return "비겼습니다."
        elif self.dic_rsp_result[self.user][0] == self.computer:
            return "이겼습니다."
        else:
            return "졌습니다."
    
    def run(self):
        
        while True:
            self.set_rsp()
            print("사용자 : ",self.user)
            print("컴퓨터 : ",self.computer)
            print(self.rsp_reslut())
            
            continue_yn = input("계속 하시겠습니까? (y/n) : ")
           
            if continue_yn.upper() not in ['Y', 'YES'] :
                break
            
        print("프로그램 종료")


rsp_game = RspGame()
rsp_game.run()




