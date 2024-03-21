def unique_month(month, possible_birthdays):
    months = [possible_birthdays[i][0] for i in range(len(possible_birthdays))]
    if months.count(month) > 1:
        return False
    return True