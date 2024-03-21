def unique_month(month, possible_birthdays):
    count=0
    for x in possible_birthdays:
        if x[0]==month:
            count=count+1
    if count == 1:
        return True
    else:
        return False