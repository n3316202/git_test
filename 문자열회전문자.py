def rotate_string(s):
    n = len(s)
    for i in range(n):
        # 한 글자씩 회전
        rotated = s[i:] + s[:i]
        print(rotated)

# 입력 받기
input_string = input("문자열을 입력하세요: ")
rotate_string(input_string)