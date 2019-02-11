# run 할 때 Run -> Edit Configuration -> Parameters 설정하기
import sys
usernames = sys.argv[1:]
def greet_users(usernames):
     for username in usernames:
          print("Hello, ", end=' ')
          str_usernames=str(username)
          print(str_usernames[0].upper()+str_usernames[1:], end='')
          print("!")

greet_users(usernames)