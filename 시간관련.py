from datetime import datetime

# 현재 시간 가져오기
now = datetime.now()

# 현재 시간의 시간 부분
current_hour = now.hour

# 인사 출력
if 4 <= current_hour < 12:
    print("Good Morning")
elif 12 <= current_hour < 18:
    print("Good Afternoon")
elif 18 <= current_hour < 22:
    print("Good Evening")
else:
    print("Good Night")