def same(iterable):
	iterator = iter(iterable)
	try:
		first = iterator.next()
	except StopIteration:
		return True
	return all(x == first for x in iterator)