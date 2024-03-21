def unique_month(month, possible_birthdays):
    counter=0
    for date in possible_birthdays:
        if month == date[0]:
            counter+=1
    return counter==1