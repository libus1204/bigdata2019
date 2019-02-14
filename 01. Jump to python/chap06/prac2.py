like_programming = []
your_name = []
while True:
    why_like_programming = input("프로그래밍이 왜 좋으세요? (종료 입력 시 프로그램 종료) : ")
    if why_like_programming == "종료":
        print("프로그램을 종료합니다.")
        f = open("./poll.txt", 'a')
        for num in range(len(like_programming)):
            write_name = your_name[num]
            write_reason = like_programming[num]
            f.write("[" + write_name + "]" + " ")
            f.write(write_reason+ "\n")
        f.close()
        exit()
    like_programming.append(why_like_programming)
    whats_your_name = input("이름을 입력해주세요. : ")
    your_name.append(whats_your_name)
    print("설문에 응답해 주셔서 감사합니다.")


