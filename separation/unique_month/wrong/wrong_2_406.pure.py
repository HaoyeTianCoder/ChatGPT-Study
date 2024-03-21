def unique_month(month, possible_birthdays):
    tupleofmonths = ()
    for i in possible_birthdays:
        tupleofmonths += (i[0],)
    count = 0
    for i in tupleofmonths:
        if month == i:
            count += 1
    return count ==1