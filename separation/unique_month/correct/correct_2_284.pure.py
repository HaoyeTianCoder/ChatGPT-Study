def unique_month(month, possible_birthdays):
    counter=0
    for birthday in possible_birthdays:
        if month==birthday[0]:
            counter+=1
        else:
            continue
    if counter==1:
        return True
    else:
        return False