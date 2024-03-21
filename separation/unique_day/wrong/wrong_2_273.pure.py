def unique_day(day, possible_birthdays):
    num=0
    for i in possible_birthdays:
        if i[1]==day: num+=1
    return num==1