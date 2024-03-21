def unique_day(day, possible_birthdays):
    counter=0
    for date in possible_birthdays:
        if day == date[1]:
            counter+=1
    return counter==1