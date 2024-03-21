def unique_month(month, possible_birthdays):
    months = 0
    for j in range(len(possible_birthdays)):  
        if possible_birthdays[j][0] == month:
            months = months + 1
    if months == 1: 
        return True
    else:
        return False