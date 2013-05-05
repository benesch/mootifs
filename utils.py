def same(iterable):
	"""Returns true if every element of `iterable` is equal"""
	iterator = iter(iterable)
	try:
		first = iterator.next()
	except StopIteration:
		return True
	return all(x == first for x in iterator)