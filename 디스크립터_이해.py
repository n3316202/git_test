import math

print(math.pi)

class CharacterInfo:
    def __init__(self, power, speed):
        self.power = power
        self.speed = speed

    def __get__(self, obj, objtype):
        print('(GET)정보 조회됨')
        #<__main__.CharacterInfo object at 0x000001BCB2AD7D30> 
        # <__main__.Guardian object at 0x000001BCB2AD7BB0> 
        # <class '__main__.Guardian'>
        print(self, obj, objtype)
        return ("공격력 : "+str(self.power) + " / 스피드 : " + self.speed)

    def __set__(self, obj, val):
        print('(UPDATE)정보 갱신 시작')
        self.power = val.power
        self.speed = val.speed

    def __delete__(self, obj):
        print("(DELETE)정보 삭제하기")
        self.power =""
        self.speed = ""

class Guardian:
    info = CharacterInfo(10, "50km/h")


g1 = Guardian()   # g1 이라는 수호천사 인스턴스 하나 생성
print(g1.info)   # 인스턴스 g1의 초기 정보 출력 
info_after_upgrade = CharacterInfo(15, "70km/h")   # 업그레이드 아이템 적용 후 캐릭터 정보
g1.info = info_after_upgrade   # 새 캐릭터 정보를 인스턴스 g1 에 설정
print(g1.info)   # 인스턴스 g1의 정보 출력
del g1.info   # 인스턴스 g1의 정보 삭제
print(g1.info)   # 인스턴스 g1의 정보 출력


#https://blog.naver.com/codeitofficial/221701646124