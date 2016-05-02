
class Dictionary(object):
	"""docstring for ClassName"""
	
	def __init__(self, node_id):
		self.dict = {}
		self.node_id = node_id


	def input_in_dict(self, timestamp, content):
		dict[(timestamp, self.node_id)] = content

	#Tuples are by default sorted by their first element (and if those are the same, then by the second, and so on), so no special key function is required
	
	def toString(self):
		for key in sorted(self.dict):
			print "%s: %s" % (key, self.dict[key])



