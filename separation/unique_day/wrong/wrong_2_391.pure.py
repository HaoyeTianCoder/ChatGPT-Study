def unique_day(day, possible_birthdays):
    count = 0
    for item in possible_birthdays:
        if day == item[1]:
            count +=1
        else:
            continue
    if count >=2:
        return False
    else:
        return True