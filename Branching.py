#example for branching

work_time = int(input("Enyter your work time in hour: "))
sleep_time = int(input("Enter your sleep time in hour: "))
if (work_time + sleep_time) > 24:
    print("Impossible")
elif (work_time + sleep_time) >= 24:
    print("Full schedule")
else:
    leftover = abs(24 - work_time - sleep_time)
    print(leftover , "h of free time")
print("End of the day")