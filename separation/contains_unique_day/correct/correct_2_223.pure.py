def contains_unique_day(month, possible_birthdays):
    a=0
    for b in possible_birthdays:
        if b[0]==month:
            s=b[1]
            if unique_day(s,possible_birthdays):
                a=a+1
                break
            else:
                continue
        else:
            continue
    if a==1:
        return True
    else:
        return False