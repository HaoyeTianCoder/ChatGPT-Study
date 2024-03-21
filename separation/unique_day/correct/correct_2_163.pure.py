def unique_day(day, possible_birthdays):
    c=0
    for birthday in possible_birthdays:
        if day==birthday[1]:
            c+=1
    return c==1