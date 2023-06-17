#
# Example file for working with Calendars
# LinkedIn Learning Python course by Joe Marini
#
# TODO: import the calendar module
import calendar

# TODO: create a plain text calendar
# c = calendar.TextCalendar(calendar.SUNDAY)
# c = calendar.TextCalendar(calendar.MONDAY)
# str = c.formatmonth(2023, 6, 3, 0)
# print(str)


# TODO: create an HTML formatted calendar
# hc = calendar.HTMLCalendar(calendar.MONDAY)
# str = hc.formatmonth(2023, 6)
# print(str)

# TODO: loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
# for i in c.itermonthdays(2023, 1):
#     print(i)

# TODO: The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for month in calendar.month_name:
    print(month)

for days in calendar.day_name:
    print(days)

# TODO: Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("The team meeting will be on:")
for m in range(1, 13):
    cal = calendar.monthcalendar(2023, m)
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print("%10s %2d" % (calendar.month_name[m], meetday))
