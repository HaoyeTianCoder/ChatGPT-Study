def unique_day(day, possible_birthdays):
    num=0
    for i in possible_birthdays:
        if day==i[1]:
            num+=1
    return num==1