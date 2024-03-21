def unique_day(day, possible_birthdays):
    count=0
    for i in possible_birthdays:
        count+=i.count(day)
    if count==1:
        return True
    return False