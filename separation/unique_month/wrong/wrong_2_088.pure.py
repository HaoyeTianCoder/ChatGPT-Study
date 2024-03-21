def unique_month(month, possible_birthdays):
    day = month
    counted = ()
    for birthdays in possible_birthdays:
        if birthdays[0] == day:
            if day not in counted:
                counted += (day,)
            else:
                return False
    return True