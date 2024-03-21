def unique_day(day, possible_birthdays):
    counter=0
    for i in possible_birthdays:
        if i[1]==day:
            counter+=1
    return counter==1