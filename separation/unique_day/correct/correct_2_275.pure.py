def unique_day(date, possible_birthdays):
    days = [birthday[1] for birthday in possible_birthdays]
    return days.count(date) == 1