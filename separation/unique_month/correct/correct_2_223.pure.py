def unique_month(month, possible_birthdays):
    s=0
    for b in possible_birthdays:
        if b[0]==month:
            s=s+1
        else:
            continue
    return s==1