PI = 3.14

def ar_circle(r):
    return PI * r * r # 원넓이 계산

def ci_circle(r):
    return 2 * PI * r # 원둘계 계산


a = 1000
b = 1000 + 0
#print(a == b) #True
print(id(a),id(b))
#print(a is b)

a = 3
b = 3
#print(a == b)
print(id(a),id(b))
#print(a is b)
import platform

# Python 인터프리터 구현체 확인 (예: CPython, PyPy 등)
print(platform.python_implementation())