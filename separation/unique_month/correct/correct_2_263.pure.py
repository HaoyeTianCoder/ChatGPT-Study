def unique_month(month, possible_birthdays):
    count = 0
    allmonths = ()
    for i in possible_birthdays:
        allmonths += (i[0],)
    for i in allmonths:
        if month == i:
            count += 1
    if count == 1:
        return True
    else:
        return False