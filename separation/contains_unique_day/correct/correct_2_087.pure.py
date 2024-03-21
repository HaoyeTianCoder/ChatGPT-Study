def contains_unique_day(month, possible_birthdays):
    singlemonthbirthday = ()
    for birthmonth in possible_birthdays:
        if month == birthmonth[0]:
            singlemonthbirthday += (birthmonth,)
    for birthday in singlemonthbirthday:
        if unique_day(birthday[1], possible_birthdays) == True:
            return True
    return False