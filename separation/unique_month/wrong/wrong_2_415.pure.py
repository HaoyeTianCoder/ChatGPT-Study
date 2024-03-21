def unique_month(month, possible_birthdays):
    count=0
    for i in possible_birthdays:
        if month==i[0]:
            count+=1
    if count>1:
        return False
    else:
        return True