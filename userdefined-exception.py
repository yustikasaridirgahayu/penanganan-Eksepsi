import math

class abstractError(RuntimeError):
	def __init__(self, s):
		self.s = s

class DuaDimensi(object):
	def __init__(self):
		raise abstractError("ERROR: '" + "DuaDimensi" + "' adalah kelas abstrak")
	def luas(self):
		raise NotImplementedError
	def keliling(self):
		raise NotImplementedError

class Lingkaran(DuaDimensi):
	def __init__(self, r):
		self.r = r
	def luas(self):
		return math.pi * self.r * self.r
	def keliling(self):
		return 2 * math.pi * self.r

def main():

	obj1 = Lingkaran(3)

	print("LINGKARAN")
	print("luas\t\t:", obj1.luas())
	print("Keliling\t:", obj1.keliling())

	try:
		print("\nMembuat objek " + "dari kelas DuaDimensi...")
		obj2 = DuaDimensi()
	except abstractError as error:
		print(error.s)
	else:
		print("DUADIMENSI")
		print("Luas\t\t:", obj2.luas())
		print("Keliling\t:", obj2.keliling())

if __name__ == "__main__":
	main()
