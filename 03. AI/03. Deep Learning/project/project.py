import random
# BMI를 계산해서 레이블을 리턴하는 함수
def calc_bmi(h, d):
    if h < 120 and h >90 and d < 80 and d > 60: return "normal"
    elif h < 90 and d < 60: return "low"
    elif h >= 120 and d >= 80: return "high"
    else: return "None"
# 출력 파일 준비하기
fp = open("blood_pressure.csv","w",encoding="utf-8")
fp.write("systole,atonly,blood_pressure\n")
# 무작위로 데이터 생성하기
for i in range(20000):
    h = random.randint(60, 160)
    d = random.randint(40, 130)
    label = calc_bmi(h, d)
    if label == 'None': continue
    fp.write("{0},{1},{2}\n".format(h, d, label))
fp.close()
print("ok,")