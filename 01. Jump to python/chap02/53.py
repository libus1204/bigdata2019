input_data="201901300915-0175440.002"
year = input_data[0:4]
month = input_data[4:6]
day = input_data[6:8]
time = input_data[8:10]
minute = input_data[10:12]
temp = input_data[12:15]
dust = input_data[15:17]
u_dust = input_data[17:19]
ozone = input_data[19:24]

print("year = "+year+"\nmonth = "+month+"\nday = "+day+"\ntime = "+time+"\nminute = "+minute+"\ntemp = "+temp+"\ndust = "+dust+"\nu_dust = "+u_dust+"\nozone = "+ozone)
