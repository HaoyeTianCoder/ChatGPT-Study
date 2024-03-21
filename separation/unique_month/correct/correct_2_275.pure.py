def unique_month(month, possible_birthdays):
    months = [birthday[0] for birthday in possible_birthdays]
    return months.count(month) == 1