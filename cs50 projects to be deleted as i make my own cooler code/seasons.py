from datetime import date
from datetime import timedelta
from sys import exit
import re
import inflect
p = inflect.engine()


def main():
    time = date.today()-Date.get()
    #for some reason, it does not let a variable that is itself a tuple and needs it to be a tuple like this
    time = days_to_minutes(time)
    time = wordify(time)
    time = first_cap(time)
    print(time + " minutes")


class Date(date):
    def __init__(self, year, month, day):
        try:
            self.year = year
            self.month = month
            self.day = day
        except ValueError:
            exit("Invalid Date")

    @classmethod
    def get(cls):
        try:
            birth = (input("Date of Birth: "))
            m = re.match(r"\d{1,4}-\d?\d-\d?\d", birth)
            birth= m.group(0)
            birth = date.fromisoformat(birth)
            return birth
        except AttributeError  or ValueError:
            exit("Invalid date")


def days_to_minutes(days):
    days = timedelta.total_seconds(days)
    days = round(days * (1/60))
    return days

def wordify(number):
    word = p.number_to_words(number)
    word = re.sub(r" and ", " ", word)
    return word

def first_cap(string):
    string = string[0].upper() + string[1:]
    return string

if __name__ == "__main__":
    main()