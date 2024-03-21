def unique_day(day, possible_birthdays):
    s=0
    for b in possible_birthdays:
        if b[1]==day:
            s=s+1
        else:
            continue
    return s==1