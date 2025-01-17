# 파일 커넥션을 open한다.
handle = open("text.txt", "w");

# handle에 write 함수를 사용해서 hello world라는 문구를 입력하였다.
handle.write("hello world");# 파일은 리소스 타입이기 때문에 사용 후에는 반드시 커넥션을 닫아야 한다.

# 커넥션을 닫지 않으면 다른 곳에서 해당 파일을 사용할 수 없다.
handle.close();


# 파일 커넥션을 open한다. 옵션을 r로 설정했다.
handle = open("text.txt", "r");
# read함수는 파일 전체를 한번에 읽어드린다.
data =handle.read();
# 커넥션을 닫는다.
handle.close();
print(data);


with open("text.txt", "r") as handle:
  # 한 줄씩 읽기 위해 while 루프를 사용했다.
  while True:
    # 한 줄씩 읽어온다.
    line = handle.readline();
    # line에 값이 없다면 루프는 멈춘다.
    if not line:
      break;
    # 화면 출력
    print(line);


