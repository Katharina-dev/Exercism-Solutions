from calendar import weekday
from datetime import date
# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message

weeks = {"first":[1,2,3,4,5,6,7],
        "second":[8,9,10,11,12,13,14],
        "third":[15,16,17,18,19,20,21],
        "fourth":[22,23,24,25,26,27,28],
        "fifth":[29,30,31],
        "teenth":[13,14,15,16,17,18,19]}

days = {"Monday":0, "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4, "Saturday":5, "Sunday":6}

def meetup(year, month, week, day_of_week):
    for day in range(1,33):
        try:
            if weekday(year, month, day) == days[day_of_week]:
                if week in weeks and day in weeks[week]:
                    return date(year,month,day)
                elif week == "last":
                    last_day = day
        except ValueError:
            if week != "last":
                raise MeetupDayException("That day does not exist.")
            return date(year,month,last_day)
