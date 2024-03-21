def contains_unique_day(month, possible_birthdays):
    for ele in possible_birthdays:
        birthmonth = ele[0]
        if birthmonth == month:
            if unique_day(ele[1], possible_birthdays) == True:
                return True
    return False