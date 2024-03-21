def unique_month(month, possible_birthdays):
    occurence = 0
    for date in possible_birthdays:
        if month == date[0]:
            occurence +=1
    if occurence == 0 or occurence > 1:
        return False
    return True 