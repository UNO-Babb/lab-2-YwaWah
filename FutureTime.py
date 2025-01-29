#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6) % 24
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later
  hours = input("Enter hours: ") 
  minutes = input ("Enter minutes: ")
  hours = int(hours)
  minutes= int(minutes)
  futureHour = (currentHour + hours) % 24
  futureMinute = (currentMinute + minutes) % 60
  extraHour = (currentMinute + minutes) // 60
  strHour = str(futureHour + extraHour)
  strMin = str(futureMinute)
  if futureMinute < 10:
    strMin = "0" + strMin
  print(strHour + ":" + strMin)

  #TODO:
  #Ask user for hours
  #Ask user for minutes

  #Calculate the time after the user-supplied time has passed.

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
