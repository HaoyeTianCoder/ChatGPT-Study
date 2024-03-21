def unique_month(month, possible_birthdays):
    data = ()
    for birthday in possible_birthdays:
        if month == birthday[0]:
            data += (birthday,)
    if len(data)==1:
        return True
    else:
        return False