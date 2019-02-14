three_min = 0
total_sec = 0
for min in range(0,61):
    min_str = str(min)
    count_three = min_str.count('3') # 분에 3이 있는 숫자 카운트
    if count_three > 0: # 3이 1개라도 있을 때
        three_min += 60  # 분에 60초를 더함

for hour in range(0,24):
    hour_str = str(hour)
    count_three_hour = hour_str.count('3')  # 시간에 3이 있는 숫자 카운트
    if count_three_hour == 0 : # 3이 없을 때
        total_sec += three_min  # 위에서 구한 값 더함
    else: total_sec += 60*60  # 3이 있을 때에는 60분 * 60초 더함

print(total_sec)
