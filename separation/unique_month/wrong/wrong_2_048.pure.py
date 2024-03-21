def unique_month(month, possible_birthdays):
    counter = 0
    result = 0
    while counter < len(possible_birthdays):
        chosen_month = possible_birthdays[counter][0]
        if chosen_month == month:
            result = result + 1
        counter = counter + 1
    if result > 1:
        return False
    return True