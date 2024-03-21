def unique_day(day, possible_birthdays):
    days = sum(map(lambda x: x[1]==day,possible_birthdays))
    return days == 1