daysmap = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday"
}
curday = int(input("Enter what day it is: "))
diff = int(input("Enter number of days: "))
day = daysmap[(curday + diff) % 7]
print("It will be", day)
