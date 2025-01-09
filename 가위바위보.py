import math
from circle import *  # circle.py 모듈의 모든 함수와 상수를 가져옴

#import 선언 없이 그냥 언제든 호출 가능한 함수
print("Hello World")

print(math.pi) # math 모듈의 pi 상수 호출
print(math.sin(5)) # 삼각함수 호출
print(PI) # circle.py 모듈의 PI 상수 호출

dic_rsp_result = {
    '가위': ('바위',"승"), 
    '바위': ('보',"승"),
    '보': ('가위',"승"),
}

def rsp(mine,yours):

    if mine == yours:
        return "비겼습니다."
    elif dic_rsp_result[mine][0] == yours:
        return "이겼습니다."
    else:
        return "졌습니다."

print(rsp("가위","바위"))
print(rsp("바위","바위"))
print(rsp("가위","바위"))

