def unique_day(day, possible_birthdays):
    count=0
    for i in possible_birthdays:
        if i[1]==day:
            count+=1
    return count==1