def unique_month(month, possible_birthdays):
    counter = 0
    for elem in possible_birthdays:
        birthmonth = elem[0]
        if birthmonth == month:
            counter += 1
    if counter == 1:
        return True
    else:
        return False