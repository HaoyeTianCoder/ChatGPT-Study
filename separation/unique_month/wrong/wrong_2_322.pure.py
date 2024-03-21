def unique_month(month, possible_birthdays):
    counter=0
    for dates in possible_birthdays:
        if month==dates[0]:
            counter=counter+1
        else:
            continue
    if counter>1:
        return False
    else:
        return True 