def unique_month(month, possible_birthdays):
    checker = []
    for bday in possible_birthdays:
        if month == bday[0] and month not in checker:
            checker.append(month)
        elif month == bday[0] and month in checker:
            return False
    return True