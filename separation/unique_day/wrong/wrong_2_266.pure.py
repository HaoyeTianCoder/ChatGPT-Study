def unique_day(day, possible_birthdays):
    counter=0
    for i in possible_birthdays:
        if day==i[1]:
            counter=counter+1
        else:
            pass
    return counter<=1