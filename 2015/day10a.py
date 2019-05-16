def lookandsay(number):
	temp = list()
	for i in str(number):
		if len(temp) > 0 and i == int(temp[-1][1]):
			temp[-1][0] += 1
		else:
			temp.append([1,i])
	return ''.join([''.join(map(str,i)) for i in temp])

num = 311332213
