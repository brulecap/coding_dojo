# PART I
# Create a Python class called MathDojo that has the methods add and subtract.
# Have these 2 functions take at least 1 parameter.
#
# Then create a new instance called md. It should be able to do the following task:
#
# md.add(2).add(2,5).subtract(3,2).result
# which should perform 0+2+(2+5)-(3+2) and return 4.
#
# PART II
# Modify MathDojo to take at least one integer(s) and/or list(s) as a parameter with any
# number of values passed into the list. It should now be able to perform the following tasks:
#
# md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result
# should do 0+1+3+4+(3+5+7+8)+(2+4.3+1.25)-2-(2+3)-(1.1+2.3) and return its result.
#
# PART III
# Make any needed changes in MathDojo in order to support tuples of values in addition to
# lists and singletons.
#
# Note: I took it one step beyond and the add and subtract methods can handle any number
# of parameters, not just 2.
class MathDojo(object):
	def __init__(self):
		self.temp = 0
	# Result
	def result(self):
		print "%0.2f" % self.temp
		self.temp = 0
		return self
	# The add and subtract function I came up with have the same code
	# for the most part. Created one function with an add or subtract 
	# parameter to be called from add or subtract.
	def add_subtract(self, operation, *args):
		for item in args:
			if isinstance(item, list) or isinstance(item, tuple):
				for number in item:
					if isinstance(number, int) or isinstance(number, float):
						if operation == "add":
							self.temp += number
						elif operation == "subtract":
							self.temp -= number
						else:
							print "add_subtract: unknown operation: " + operation
					else:
						print "Unknown value while adding: " + number
			elif isinstance(item, int) or isinstance(item, float):
				if operation == "add":
					self.temp += item
				elif operation == "subtract":
					self.temp -= item
				else:
					print "add_subtract: unknown operation: " + operation
			else:
				print "Unknown value while adding: " + item
		return self

	# Add
	def add(self, *args):
		self.add_subtract("add", *args)
		return self

	# Subtract
	def subtract(self, *args):
		self.add_subtract("subtract", *args)
		return self

md = MathDojo()
try:
	md.add(2).add(2,5).subtract(3,2).result()
	md.add([3,5,7,8], [2,4.3,1.25]).subtract((3,5,7,8), [2,4.3,1.25]).result()
	md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()
	# All the above using the more than 2 parameter functionality
	md.add([1], 3,4, [3,5,7,8], [2,4.3,1.25], 2, 2, 5).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3],(3,5,7,8), [2,4.3,1.25], 3, 2).result()
except Exception as e:
	print(e)