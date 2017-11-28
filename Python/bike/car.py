# declare Car class
class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if self.price > 10000:
			self.tax = .15
		else:
			self.tax = .12
	# This method displays all instance variables
	def display_all(self):
		print "Price: " + str(self.price) + "."
		print "Speed: " + str(self.speed) + "."
		print "Fuel: " + str(self.fuel) + "."
		print "Mileage: " + str(self.mileage) + "."
		print "Tax: " + str(self.tax) + "."
#now create an instance of the class
car1 = Car(20000, '100mph','Half Full', '18mpg')
car2 = Car(25000, '90mph','Full', '25mpg')
car3 = Car(10000, '20mph','Empty', '16mpg')
car4 = Car(11000, '80mph','Quarter Full', '19mpg')
car5 = Car(34000, '110mph','Three Quarters Full', '45mpg')
car6 = Car(40000, '200mph','Full', '12mpg')

car1.display_all()
car1.display_all()
car1.display_all()
car1.display_all()
car1.display_all()
car1.display_all()