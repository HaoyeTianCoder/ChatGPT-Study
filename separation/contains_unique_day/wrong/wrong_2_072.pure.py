def contains_unique_day(month, possible_birthdays):
    tup = ()
    for birthday in possible_birthdays:
        if month == birthday[0]:
            tup += (birthday,)
    for each in tup:
        if each[1] == '18' or each[1] == '19':
            return True
    return False 