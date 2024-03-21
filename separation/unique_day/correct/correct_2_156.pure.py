def unique_day(day, possible_birthdays):
    counter =0
    for elements in possible_birthdays:
        if day == elements[1]:
            counter +=1
    return counter == 1