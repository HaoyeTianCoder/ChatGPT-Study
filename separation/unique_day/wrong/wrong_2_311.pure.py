def unique_day(day, possible_birthdays):
    counter=0
    for date in possible_birthdays:
        if date[1]==day:
            conter+=1
        else:
            counter=counter
    if counter==1:
        return True
    else:
        return False