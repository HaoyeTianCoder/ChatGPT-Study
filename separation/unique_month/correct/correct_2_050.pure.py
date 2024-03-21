def unique_month(month, possible_birthdays):
    freq=0
    for birthday in possible_birthdays:
        if birthday[0]==month:
            freq=freq+1
        else:
            continue
    if freq==1:
        return True
    else:
        return False