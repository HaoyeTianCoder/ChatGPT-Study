def unique_day(date, possible_birthdays):
    count = 0
    for i in possible_birthdays:
        if date == i[1]:
            result += 1
        return result
        if result == 1:
            return True
        else:
            return False