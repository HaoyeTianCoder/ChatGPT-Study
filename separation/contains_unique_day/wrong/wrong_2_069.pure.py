def contains_unique_day(month, possible_birthdays):
    result=()
    for i in possible_birthdays:
        if i[0]==month:
            result+=(i,) 
    for i in result:
        if unique_day(i[1],possible_birthdays)==True:
            return True
    return False