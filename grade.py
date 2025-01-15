from calendar import c


import datetime

now = datetime.datetime.now()

print(now)

# class Grade:
#     def __init__(self,kor,eng,math):
#         self.kor = kor
#         self.eng = eng
#         self.math = math    

#     def set_eng(self,eng):
#         self.eng = eng

#     def get_total(self):
#         return self.kor + self.eng + self.math

#     def get_avg(self):
#         return self.get_total() / 3
    
#     def get_grade(self):
        
#         avg = self.get_avg()        
#         grade = "가"

#         if avg >= 90:
#             grade = '수'
#         elif avg >= 80:
#             grade = '우'
#         elif avg >= 70:
#             grade = '미'
#         elif avg >= 60:
#             grade = '양'
#         else:
#             grade ='가'

#         return grade

# # 
# def main():

#     while True:
#         kor = int(input("국어 점수 입력 : "))
#         eng = int(input("영어 점수 입력 : "))
#         math = int(input("수학 점수 입력 : "))

#         grade = Grade(kor,eng,math)        
        
#         print("국어 : ",grade.kor)

#         print("총점 : ",grade.get_total())
#         print("평균 : ",grade.get_avg())
#         print("학점 : ",grade.get_grade())

#         continue_yn = input("계속 하시겠습니까? (y/n) : ")
#         #y,yes,Yes,Y,yes
#         if continue_yn.upper() != 'Y' and continue_yn.upper() != 'YES' :
#             break
    
#     print("프로그램 종료")

# main()

# import copy

# a = [[1,2],[3,4]]
# b = copy.copy(a)
# print(id(a),id(b))
# a[1].append(5)
# print(id(a),id(b))
# print(a)
# print(id(a[1]),id(b[1]))
