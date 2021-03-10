# Youtibe link: https://www.youtube.com/watch?v=t8pPdKYpowI&t=30s&ab_channel=TechWorldwithNana
import datetime

user_input = input("Enter the goal deadline with date, separated by colon: \n")
# input format :   learn python:20.03.2021
# here, 'learn python' is the goal & '20.03.2021' is the deadline. Both are separated by :
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]
# print(input_list)

# print(datetime.datetime.strptime(deadline, "%d.%m.%Y"))
# print(type(datetime.datetime.strptime(deadline, "%d.%m.%Y")))

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
# print(today_date)

days_remaining = deadline_date-today_date
# print("Time remaining for My Goal", goal, "is", days_remaining)
print("Dear User, \nTime remaining for My Goal",
      goal, "is", days_remaining.days, "days")

print("Dear User, \nTime remaining for My Goal",
      goal, "is", int((days_remaining.total_seconds())/3600), "hours")
