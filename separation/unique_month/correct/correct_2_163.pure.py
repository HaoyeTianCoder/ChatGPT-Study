def unique_month(month, possible_birthdays):
    c=0
    for birthday in possible_birthdays:
        if month==birthday[0]:
            c+=1
    return c==1