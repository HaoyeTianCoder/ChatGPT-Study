def unique_month(month, possible_birthdays):
    count_month = 0
    for birthday in possible_birthdays:
        if month == birthday[0]:
            if count_month == 0: count_month += 1
            else: return False
    return True