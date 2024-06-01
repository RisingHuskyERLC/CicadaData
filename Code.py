# Code (python)
import datetime

today = datetime.date.today()
year = today.year
x=0
uncool = True

while uncool == True:
  x+=1
  if x % 13 == 0 and x % 17 == 0:
    print("every ", x, " years, there will be 13&17 year cicadas")
    uncool = False

nextYearWithCicadas = year + x
if nextYearWithCicadas % 13 != 0 or nextYearWithCicadas % 17 != 0:
  thireteenRemainder = nextYearWithCicadas % 13
  sec
print("there will be year 13&17 cicadas in the year ", nextYearWithCicadas)
