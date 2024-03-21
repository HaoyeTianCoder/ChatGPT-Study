def unique_month(month, possible_birthdays):
    a=''
    for date in possible_birthdays:
        if a== date[0]:
            return False
        elif month ==date[0]:
            a=month
    return True