def unique_day(day, possible_birthdays):
    count=0
    for birthday in possible_birthdays:
        if day in birthday[1]:
            count+=1
    if count==1:
        return True
    else:
        return False    