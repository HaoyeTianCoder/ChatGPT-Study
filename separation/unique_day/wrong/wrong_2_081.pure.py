def unique_day(date, possible_birthdays):
    result=()
    counter=0
    for i in possible_birthdays:
        if day==i[1]:
            result=result+(possible_birthdays[:counter]+possible_birthdays[counter+1:])
            break
        else:
            counter+=1
            continue
    for i in result:
        if day==i[1]:
            return False
    return True