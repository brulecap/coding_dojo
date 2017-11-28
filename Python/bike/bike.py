# declare Bike class
class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	# This method displays all instance variables
	def displayInfo(self):
		print "This bike's price is " + str(self.price) + "."
		print "This bike's maximum speed is " + str(self.max_speed) + "."
		print "This bikes has been ridden " + str(self.miles) + " miles."
		return self
# This method adds 10 miles
	def ride(self):
		print "Riding"
		self.miles += 10
		return self
#this method subtracts 5 but allows the minimum miles to be not less than 0
	def reverse(self):
		print "Reversing"
		if self.miles > 5:
			self.miles -= 5
		else:
			self.miles = 0
		return self
#now create an instance of the class
bike1 = Bike(1000, 60)
bike2 = Bike(500, 50)
bike3 = Bike(200, 30)

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()