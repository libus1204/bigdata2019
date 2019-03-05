from collections import OrderedDict
import json

print("가상데이터로 기기들의 제어를 시작합니다.")
sim_baseDate = input("날짜를 입력하세요(YYYYMMDD) : ")
sim_baseTime = input("측정시간을 입력하세요(hhMM) : ")
sim_category_T1H = input("온도를 입력하세요 : ")
sim_category_RN1 = input("강수량을 입력하세요 : ")
sim_category_REH = input("습도를 입력하세요 : ")
sim_fcstTime = input("예측시간을 입력하세요 : ")
sim_nx = input("위도를 입력하세요 : ")
sim_ny = input("경도를 입력하세요 : ")
sim_khaiGrade = input("통합대기환경지수를 입력하세요 : ")
sim_stationName = input("동네 이름을 입력하세요 : ")
total_air_simul = []
total_dust_simul = []
value=[]
value.append(sim_category_T1H)
value.append(sim_category_RN1)
value.append(sim_category_REH)
category_list = ["T1H", "RN1", "REH"]
simulation1 = OrderedDict()
simulation2 = OrderedDict()
simulation3 = OrderedDict()
simulation1["baseDate"] = int(sim_baseDate)
simulation1["baseTime"] = int(sim_baseTime)
simulation1["category"] = str(category_list[0])
simulation1["fcstTime"] = int(sim_fcstTime)
simulation1["fcstValue"] = int(sim_category_T1H)
simulation1["sim_nx"] = int(sim_nx)
simulation1["sim_ny"] = int(sim_ny)
simulation2["baseDate"] = int(sim_baseDate)
simulation2["baseTime"] = int(sim_baseTime)
simulation2["category"] = str(category_list[1])
simulation2["fcstTime"] = int(sim_fcstTime)
simulation2["fcstValue"] = int(sim_category_RN1)
simulation2["sim_nx"] = int(sim_nx)
simulation2["sim_ny"] = int(sim_ny)
simulation3["baseDate"] = int(sim_baseDate)
simulation3["baseTime"] = int(sim_baseTime)
simulation3["category"] = str(category_list[2])
simulation3["fcstTime"] = int(sim_fcstTime)
simulation3["fcstValue"] = int(sim_category_REH)
simulation3["nx"] = int(sim_nx)
simulation3["ny"] = int(sim_ny)
total_air_simul.append(simulation1)
total_air_simul.append(simulation2)
total_air_simul.append(simulation3)

with open('air_simul', 'w', encoding='utf-8') as outfile:
    retJson = json.dumps(total_air_simul, indent=4, sort_keys=True, ensure_ascii=False)
    outfile.write(retJson)

simulation4 = OrderedDict()
simulation4["dateTime"] = sim_baseDate+sim_baseTime
simulation4["khaiGrade"] = sim_khaiGrade
simulation4["stationName"] = sim_stationName
total_dust_simul.append(simulation4)

with open('dust_simul', 'w', encoding='utf-8') as outfile:
    retJson = json.dumps(total_dust_simul, indent=4, sort_keys=True, ensure_ascii=False)
    outfile.write(retJson)


simulation_air_csv = ["baseDate, baseTime, category, fcstTime, fcstValue, sim_nx, sim_ny"]
for count in range(len(category_list)):
    simulation_air_csv.append(sim_baseDate+','+sim_baseTime+','+category_list[count]+','+sim_fcstTime+','+value[count]+','+sim_nx+','+sim_ny)

f= open('simul_air_csv.csv', 'w')
f.write('\n'.join(simulation_air_csv))
f.close()
