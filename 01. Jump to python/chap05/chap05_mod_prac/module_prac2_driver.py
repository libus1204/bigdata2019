import module_prac2 # 같은 폴더 안에 module_prac1 에 있는 함수 호출

print(module_prac2.safe_sum('a',1)) # 더할수 있는 것이 아닙니다. None 출력
print(module_prac2.safe_sum(1,4)) # 5 출력
print(module_prac2.sum(10,10.4)) # 20.4 출력

# 아까는 위에 주석처럼 결과가 출력 되었으나
# module_prac2_driver.py 출력은
# 더할수 있는 것이 아닙니다.
# None
# 5
# 20.4
# 더할수 있는 것이 아닙니다
# None
# 5
# 20.4
# import module_prac2 을 수행하는 순간 module_prac2 가 실행이 되어 결과값을 출력
# ---> if __name__ == "__main__": 사용
# module_prac2_2 에서 계속
