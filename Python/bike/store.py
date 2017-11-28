from product import Product
# declare Store class
class Store(object):
	def __init__(self, address, name):
		self.address = address
		self.owner_name= name
		self.products = []
	# This method displays all instance variables
	def display_all(self):
		print "Addres: " + self.address
		print "Owner Name: " + self.owner_name
		for product in self.products:
			product.display_all()
		return self
	# Add product to inventory
	def add_product(self, product):
		self.products.append(product)
		return self
	# Remove product from inventory
	def remove_product(self, name):
		for product in self.products:
			if product.name == name:
				product_index = self.products.index(product)
				print self.products.index(product)
				print product_index
				self.products.pop(product_index)
		return self

store = Store("123 Stone Street, Stone NH 11111", "me")
store.display_all()


product1 = Product(300, 'laptop','5lbs', 'Dell')
product2 = Product(500, 'tv','25lbs', 'Samsung')
product3 = Product(1200, 'drone','10lbs', 'GoPro','like_new')

store.add_product(product1)
store.add_product(product2)
store.add_product(product3)
store.display_all()
store.remove_product('tv')
store.display_all()