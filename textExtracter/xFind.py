def xFind (text, first, last):
	list = []
	x = 0
	y = 0
	size = text.count (first)
	for i in range(size):
		x = text.find(first ,y)+ len (first)
		y = text.find(last, x)
		list.append(text[x:y])
	return list


