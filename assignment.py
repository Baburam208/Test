
# class MaxSizeArr():

# 	def __init__(self,n):
# 		self.size = n
# 		self.innerarr =  []
	
# 	def push(self, obj):
# 		self.innerarr.append(obj)
# 		if len(self.innerarr) > self.size:
# 			self.innerarr.pop(0)

# 	def getarr(self):
# 		return self.innerarr

# class CreateArr(MaxSizeArr):
# 	def __init__(self,n):
# 		self.size = n
# 		self.innerarr=[]
# c=CreateArr(4)
# c.push('hey')
# c.push('there')
# c.push('asis')
# c.push('now')
# c.push('then')
# print(c.getarr())
	
# a = MaxSizeArr(3)
# b= MaxSizeArr(2)

# a.push('hey')
# a.push('hi')
# a.push('let go')
# a.push('go')

# b.push('what')
# b.push('you')
# b.push('doing')
# b.push('now')

# print(a.getarr())
# print(b.getarr())

class Person():
	def __init__(self, first, last):
		self.firstname = first
		self.lastname = last

	def name(self):
		return self.firstname + ' ' + self.lastname

class Emp(Person):
	count=0
	def __init__(self,first,last,no):
		Person.__init__(self,first, last)
		self.empno = no
	def show(self):
		return self.name() + self.empno

	@classmethod
	def sum(cls):
		return (cls.count+2)


a = Emp('asis','rij', '100')
print(a.name())
print(a.show())
# print(Emp.mro())

print(a.sum())

