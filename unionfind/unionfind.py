#!/usr/bin/python

class UnionFind:
	'''
	A Union Find class that stores a mapping between 
	a set of user-defined objects and a set of integers.
	'''

	def __init__(self):
		self.__mapping = dict()		# maps a hashable object X to a node i
		self.__parent = []			# parent[i] represents the parent of node i, unless node i is a root, then parent[i] is the negative rank of node i


	def add(self, *items):
		'''
		Add item(s) for the UnionFind object to track

		param *items: a list of hashable user-defined objects to add
		'''
		for item in items:
			ID = len(self.__parent)
			self.__mapping[item] = ID
			self.__parent.append(-1)


	def find(self, item):
		'''
		Returns a unique identifier for the subset containing the item.

		param item: the item in question
		'''
		return self._find(self.__mapping[item])


	def together(self, a, b):
		'''
		Returns True if items a and b are in the same subset

		param a: item a
		param b: item b
		'''
		return self.find(a) == self.find(b)


	def _find(self, ID):
		'''
		Finds the root of a node

		param ID: the ID of the node looking for its root
		'''
		if self.__parent[ID] < 0:
			return ID
		self.__parent[ID] = self._find(self.__parent[ID])
		return self.__parent[ID]


	def union(self, a, b):
		'''
		Unions the subsets containing items a and b

		param a: item a
		param b: item b
		'''
		root1 = self.find(a)
		root2 = self.find(b)
		if root1 == root2:
			return

		rank1 = self.__parent[root1]
		rank2 = self.__parent[root2]
		if rank1 < rank2:
			self.__parent[root2] = root1
		elif rank1 > rank2:
			self.__parent[root1] = root2
		else:
			self.__parent[root1] = root2
			self.__parent[root2] -= 1



if __name__ == '__main__':
	uf = UnionFind()
	uf.add((1,5))
	uf.add((3,0))
	uf.add((7,6))
	uf.add((1,-1))
	uf.add((1000,3921))
	print(str(uf.together((1,5), (1,-1))))
	uf.union((1,5), (1,-1))
	print(str(uf.together((1,5), (1,-1))))








