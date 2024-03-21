def unique_day(day, possible_birthdays):
    count=0
    for i in possible_birthdays:
        if day == i[1]:
            count+=1
        else:
            continue
    if count<=1:
        return True
    else:
        return False