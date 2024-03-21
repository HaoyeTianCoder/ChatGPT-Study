def unique_day(day, possible_birthdays):
    a=''
    for date in possible_birthdays:
        if a== date[1]:
            return False
        elif day ==date[1]:
            a=day
    return True