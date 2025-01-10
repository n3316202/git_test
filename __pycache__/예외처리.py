def main():
	bread = 10     # 열 개의 빵
	try:
		people = int(input("몇 명? "))
		print("1인당 빵의 수: ", bread / people)
		print("맛있게 드세요.")
	except ValueError as msg:
		print("입력이 잘못되었습니다.")
		print(ValueError, msg) # 오류메세지 출력

	except ZeroDivisionError as msg:
		print("0으로는 나눌 수 없습니다.")
		print(ZeroDivisionError, msg) # 오류메세지 출력

    finally:
        print("어쨌든 프로그램은 종료되었습니다.")

main()
