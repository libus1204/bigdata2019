dic = {'A':'.- ', 'B':'-...', 'C':'-.-.', 'D':' -..', 'E':' .  ', 'F':'..-.', 'G':' --.', 'H':'....', 'I':' .. ',
       'J':'.---', 'K':' -.-', 'L':'.-..', 'M':' -- ', 'N':' -. ', 'O':'--- ', 'P':'.--.', 'Q':'--.-', 'R':' .-.',
       'S':' ...', 'T':'  - ', 'U':' ..-', 'V':'...-', 'W':' .--', 'X':'-..-', 'Y':'-.--', 'Z':'--..'}

user_input = list(input("문자열을 입력하세요 : "))
for string in range(len(user_input)):
    if not dic.get(user_input[string]):
        print(" ",end=" ")
    else: print(dic.get(user_input[string]), end=" ")


