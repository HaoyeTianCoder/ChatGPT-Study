def contains_unique_day(month,possible_birthdays):
    tup=()
    for i in possible_birthdays:
        if unique_day(i[1],possible_birthdays):
            tup=tup+(i[0],)
        else:
            pass
    for k in range(0,len(tup)):
        if tup[k]==month:
            return True
        else:
            pass
    return False