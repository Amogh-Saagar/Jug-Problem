from copy import deepcopy
import time
class Jug:
	def __init__(self, l):
		self.cap = l
		self.l = 0
	
	def fill(self):
		self.l = self.cap
	
	def empty(self):
		self.l = 0
	

	def vol(self):
		return self.l
	def capa(self):
		return self.cap
	def set(self, l):
		self.l = l
	def __repr__(self):
		return str(self.l)

def move(j1, j2): #move from j1 to j2
	j1 = deepcopy(j1)
	j2 = deepcopy(j2)
	newl = min(j2.vol()+j1.vol(), j2.capa()) # new volume in j2
	j1.set(j2.vol()-newl+j1.vol())
	j2.set(newl)
	return (j1,j2)
m = int(input())
n = int(input())
k = int(input())
j = {("", (Jug(m), Jug(n)))}
d = True
while d:
	jn = set()
	for i in j:
		#print(i[1][0].vol() == k)
		if i[1][0].vol() == k or i[1][1].vol() == k:
			print(i[0], "done")
			d = False
			break
		c = deepcopy(i[1])
		if c[1].vol() != 0:
			c1 = deepcopy(c)
			c1[1].empty()
			jn.add((i[0]+" empty2", deepcopy(c1)))
			if c[0].vol() != c[0].capa():
				c2 = deepcopy(c)
				jn.add((i[0]+" 2move1", move(c2[1], c2[0])[::-1]))
		if c[0].vol() != 0:
			c3 = deepcopy(c)
			c3[0].empty()
			jn.add((i[0]+" empty1", deepcopy(c3)))
			if c[1].vol() != c[1].capa():
				c4 = deepcopy(c)
				jn.add((i[0]+" 1move2", move(c4[0], c4[1])))
		if c[1].vol() != c[1].capa():
			c5 = deepcopy(c)
			c5[1].fill()
			jn.add((i[0]+" fill2", deepcopy(c5)))
		if c[0].vol() != c[0].capa():
			c5 = deepcopy(c)
			c5[0].fill()
			jn.add((i[0]+" fill1", deepcopy(c5)))
	j = deepcopy(jn)
	#print("\n".join(map(str, j)))
	#print()
	#time.sleep(1)
		
		
