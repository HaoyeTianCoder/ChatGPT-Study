def unique_month(month, possible_birthdays):
    count = 0
    for item in possible_birthdays:
        if motnh == item[0]:
            count +=1
        else:
            continue
    if count >=2:
        return False
    else:
        return True