def unique_month(month, possible_birthdays):
    counter =0
    for elements in possible_birthdays:
        if month == elements[0]:
            counter +=1
    return counter == 1