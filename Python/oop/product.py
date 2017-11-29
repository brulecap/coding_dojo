# declare Product class
class Product(object):
	def __init__(self, price, name, weight, brand, status='for_sale'):
		self.price = price
		self.name= name
		self.weight = weight
		self.brand = brand
		self.status = status
	# This method displays all instance variables
	def display_all(self):
		print "Price: " + str(self.price)
		print "Name: " + self.name
		print "Weight: " + self.weight
		print "Brand: " + self.brand
		print "Status: " + self.status
		return self
	# Product was sold. Update status
	def sell(self):
		self.status = "sold"
		return self
	# Add tax to price and return price + tax
	def add_tax(self, tax):
		self.price *= (1+tax)
		return self.price
	# Handle returns per the following guidelines:
	# Defective, change status to "defective" and change price to 0.
	# Returned in the box, like new, mark it "for sale".
	# Box has been, opened, set the status to "used" and apply a 20% discount.
	def handle_return(self, reason):
		if reason == "defective":
			self.status = reason
			self.price = 0
		elif reason == "like new":
			self.status = "for sale"
		elif reason == "opened":
			self.status = "used"
			self.price *= .80
		else:
			print "Method: handle_return; error: unknown return reason - " + reason
		return self