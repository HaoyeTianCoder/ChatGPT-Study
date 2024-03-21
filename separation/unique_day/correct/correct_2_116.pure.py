def unique_day(day, possible_birthdays):
    occurence = 0
    for date in possible_birthdays:
        if day == date[1]:
            occurence +=1
    if occurence == 0 or occurence > 1:
        return False
    return True