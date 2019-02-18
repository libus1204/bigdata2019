import re

p = re.compile("Crow|Servo")
m = p.match('Nothing')    # Not match
print(m)
m = p.match('Crow')       # 'Crow'
print(m)
m = p.match('Servo')      # 'Servo'
print(m)
m = p.match('CrowServo')  # 'Crow'
print(m)
