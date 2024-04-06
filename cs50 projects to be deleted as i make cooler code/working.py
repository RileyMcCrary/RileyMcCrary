import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        times = re.match(r"(1[0-2]|\d)(:[0-5]\d)? (AM|PM) (to) (1[0-2]|\d)(:[0-5]\d)? (AM|PM)",s)
        times = times.group(0)
        pattern = re.compile(r" to ")
        first_time, second_time = pattern.split(times)
        first_time = twenty_four(first_time)
        second_time = twenty_four(second_time)
        return (first_time+" to "+second_time)
    except AttributeError:
        raise ValueError

def twenty_four(twelve_hour):
    match = re.match(r"(1[0-2]|\d)(:\d{2})? (AM|PM)", twelve_hour)
    #12 AM with minutes
    if match.group(1) == "12" and match.group(3) == "AM" and match.group(2) != None:
        return "00"+match.group(2)
    #12 AM without minutes
    elif match.group(1) == "12" and match.group(3) == "AM" and match.group(2) == None:
        return "00:00"
    #12 PM with minutes
    elif match.group(1) == "12" and match.group(3) == "PM" and match.group(2) != None:
        return match.group(1)+match.group(2)
    #12 PM without minutes
    elif match.group(1) == "12" and match.group(3) == "PM" and match.group(2) == None:
        return match.group(1)+":00"

#other numbers
    #leaves all other AMs alone
    elif match.group(3) == "AM" and match.group(2) != None and len(match.group(1)+match.group(2)) == 5:
        return match.group(1)+match.group(2)
    #leaves AM alone, and adds a leading zero to a single-digit hour
    elif match.group(3) == "AM" and match.group(2) != None and len(match.group(1)+match.group(2)) == 4:
        return "0"+match.group(1)+match.group(2)
    elif match.group(3) == "AM" and match.group(2) == None and len(match.group(1)) == 2:
        return match.group(1)+":00"
    elif match.group(3) == "AM" and match.group(2) == None and len(match.group(1)) == 1:
        return "0"+match.group(1)+":00"


#PMs
    #adds 12 to the hour and adds minutes
    elif match.group(3) == "PM" and match.group(2) != None:
        return (str(int(match.group(1))+12)+match.group(2))
    elif match.group(3) == "PM" and match.group(2) == None:
        return (str(int(match.group(1))+12)+":00")
















if __name__ == "__main__":
    main()