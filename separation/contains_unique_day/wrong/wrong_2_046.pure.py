def contains_unique_day(month, possible_birthdays):
	result=()
 for i in possible_birthdays:
		if unique_day(i[1],possible_birthdays)==True:
			result=result+(i[0],)
 num=0
 for j in result:
		if month==j:
			num=num+1
 if num==1:
		return True
 else:
		return False