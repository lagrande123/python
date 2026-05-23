import datetime
import calender

current_date = datetime.datetime.now()

print("the time at greenwich meradin is :", current_time)

print("n/1. show whole year calender")
print("n/2 show whole month calender")   
choice = int(input("\nEnter your choice (1 or 2): "))

if choice == 1:
    year = int(input("Enter Year: "))
    
    # Print whole year calendar
    print("\n")
    print(calendar.calendar(year))

elif choice == 2:
    year = int(input("Enter Year: "))
    month = int(input("Enter Month (1-12): "))
    
choice = int(input("\nEnter your choice (1 or 2): "))

if choice == 1:
    year = int(input("Enter Year: "))
    
    # Print whole year calendar
    print("\n")
    print(calendar.calendar(year))

elif choice == 2:
    year = int(input("Enter Year: "))
    month = int(input("Enter Month (1-12): "))
    
