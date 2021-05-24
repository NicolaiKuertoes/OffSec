class LCG:
	a = 25214903917
	c = 11
	m = 2**48-1
	state = 0

	def __init__(self, seed):
		self.state = self.init_scamble(seed)

	def init_scamble(self, seed):
		return (seed ^ 25214903917) & 281474976710655

	def next(self, bits):
		self.state = (self.a * self.state + self.c ) & self.m
		return (self.state >> 48 - bits) & ((1<<31) - 1)

	def nextInt(self):
		return self.next(31)


