def unique_month(month, possible_birthdays):
    months = sum(map(lambda x: x[0]==month,possible_birthdays))
    return months == 1