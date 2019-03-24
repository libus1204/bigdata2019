# import random
#
# def calculation_bmi(height, weight):
#     bmi_for_test = weight / (height/100) ** 2
#     if bmi_for_test < 18.5 : return "thin"
#     if bmi_for_test < 25: return "normal"
#     return "fat"
#
# file_print = open("bmi.csv", "w", encoding="utf-8")
# file_print.write("height,weight,label\r\n")
#
# random_data = {"thin":0,"normal":0,"fat":0}
# for i in range(30000):
#     height = random.randint(120, 200)
#     weight = random.randint(35, 80)
#     label = calculation_bmi(height, weight)
#     random_data[label] += 1
#     file_print.write("{0},{1},{2}\r\n".format(height, weight, label))
# file_print.close()
# print("ok", random_data)
# import random
# def calculation_bmi(height, weight):
#     bmi_for_test = weight / (height/100) ** 2
#     if bmi_for_test < 18.5 : return "thin"
#     if bmi_for_test < 25 : return "normal"
#     return "fat"
# file_print = open("bmi.csv", "w", encoding="utf-8")
# file_print.write("height,weight,label\r\n")
# random_data = {"thin":0,"normal":0,"fat":0}
# for data in range(30000):
#     height = random.randint(120, 200)
#     weight = random.randint(35, 80)
#     label = calculation_bmi(height, weight)
#     random_data[label] += 1
#     file_print.write("{0},{1},{2}\r\n".format(height, weight, label))
# file_print.close()
# print("ok", random_data)
# import random
# def calculation_bmi(height, weight):
#     bmi_test = weight / (height / 100) ** 2
#     if bmi_test < 18.5: return "thin"
#     if bmi_test < 25: return "normal"
#     return "fat"
# file_print = open("bmi.csv", "w", encoding="utf-8")
# file_print.write("height,weight,label\r\n")
# random_data = {"thin":0, "normal":0, "fat":0}
# for data in range(30000):
#     height = random.randint(120, 200)
#     weight = random.randint(35, 80)
#     label = calculation_bmi(height, weight)
#     random_data[label] += 1
#     file_print.write("{0},{1},{2}\r\n".format(height, weight, label))
# file_print.close()
# print("ok", random_data)
# import random
# def cal(height, weight):
#     bmi = weight / (height/100) ** 2
#     if bmi < 18.5: return "thin"
#     if bmi< 25: return "normal"
#     return "fat"
# fp = open("bmi.csv", "w", encoding="utf-8")
# fp.write("height,weight,label\r\n")
# random_data = {"thin":0, "normal":0, "fat":0}
# for data in range(30000):
#     height = random.randint(120, 200)
#     weight = random.randint(35, 80)
#     label = cal(height, weight)
#     random_data[label] += 1
#     fp.write("{0},{1},{2}\r\n".format(height, weight, label))
# fp.close()
# print("ok", random_data)
# import random
# def cal(height, weight):
#     bmi = weight / (height/100) ** 2
#     if bmi < 18.5: return "thin"
#     if bmi < 25: return "normal"
#     return "fat"
# fp = open("bmi.csv", "w", encoding="utf-8")
# fp.write("height,weight,label\r\n")
# random_data = {"thin":0, "normal":0, "fat":0}
# for data in range(30000):
#     height = random.randint(120, 200)
#     weight = random.randint(35, 85)
#     label = cal(height, weight)
#     random_data[label] += 1
#     fp.write("{0},{1},{2}\r\n".format(height, weight, label))
# fp.close()
# print("ok", random_data)
# import random
# def cal(h, w):
#     bmi = w / (h/100) ** 2
#     if bmi < 18.5: return "thin"
#     if bmi < 25: return "normal"
#     return "fat"
# fp = open("bmi.csv", "w", encoding="utf-8")
# fp.write("height,weight,label\r\n")
# random_data = {"thin":0, "normal":0, "fat":0}
# for data in range(30000):
#     h = random.randint(120, 200)
#     w = random.randint(35, 85)
#     l = cal(h, w)
#     random_data[l] += 1
#     fp.write("{0},{1},{2}\r\n".format(h,w,l))
# fp.close()
# print("ok", random_data)
# import random
# def cal(h,w):
#     b = w / (h/100) ** 2
#     if b < 18.5: return "thin"
#     if b < 25: return "normal"
#     return "fat"
# fp = open("bmi.csv", "w", encoding="utf-8")
# fp.write("height,weight,label\r\n")
# random_data = {"thin":0, "normal":0, "fat":0}
# for data in range(30000):
#     h = random.randint(120, 200)
#     w = random.randint(35, 85)
#     l = cal(h,w)
#     random_data[l] += 1
#     fp.write("{0},{1},{2}\r\n".format(h,w,l))
# fp.close()
# print("ok", random_data)
# import random
# def cal(h,w):
#     b = w / (h/100) ** 2
#     if b < 18.5: return "thin"
#     if b < 25: return "normal"
#     return "fat"
# fp = open("bmi.csv", "w", encoding="utf-8")
# fp.write("height,weight,label\r\n")
# random_data = {"thin":0, "normal":0, "fat":0}
# for data in range(30000):
#     h = random.randint(120, 200)
#     w = random.randint(35, 85)
#     l = cal(h, w)
#     random_data[l] += 1
#     fp.write("{0},{1},{2}\r\n".format(h,w,l))
# fp.close()
# print("ok", random_data)
# import random
# def cal(h,w):
#     b = w / (h/100) ** 2
#     if b < 18.5: return "thin"
#     if b < 25: return "normal"
#     return "fat"
# fp=open('bmi.csv', 'w', encoding='utf-8')
# fp.write('height,weight,label\r\n')
# random_data = {"thin":0, "normal":0, "fat":0}
# for data in range(30000):
#     h = random.randint(120, 200)
#     w = random.randint(35, 85)
#     l = cal(h, w)
#     random_data[l] += 1
#     fp.write("{0},{1},{2}\r\n".format(h, w, l))
# fp.close()
# print("ok", random_data)
import random
def cal(h, w):
    b = w / (h/100) ** 2
    if b < 18.5: return "thin"
    if b < 25: return "normal"
    return "fat"
fp = open('bmi.csv', 'w', encoding='utf-8')
fp.write('height,weight,label\r\n')
random_data = {"thin":0, "normal":0, "fat":0}
for data in range(30000):
    h = random.randint(120, 200)
    w = random.randint(35, 85)
    l = cal(h, w)
    random_data[l] += 1
    fp.write("{0},{1},{2}\r\n".format(h, w, l))
fp.close()
print("ok", random_data)