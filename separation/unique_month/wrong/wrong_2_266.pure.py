def unique_month(month, possible_birthdays):
    counter=0
    for i in possible_birthdays:
        if month==i[0]:
            counter=counter+1
        else:
            pass
    return counter<=1