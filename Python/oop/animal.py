class Animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health
	# This method displays all instance variables
	def display_health(self):
		print "Name: " + self.name
		print "Health: " + str(self.health)
		return self
	# Walk
	def walk(self):
		self.health -= 1
		return self
	# Walk
	def run(self):
		self.health -= 5
		return self

class Dog(Animal):
	def __init__(self, name, health=150):
		super(Dog, self).__init__(name, health)    # use super to call the Animal __init__ method
	# Pet
	def pet(self):
		self.health += 5
		return self

class Dragon(Animal):
	def __init__(self, name, health=170):
		super(Dragon, self).__init__(name, health)    # use super to call the Animal __init__ method
	# Fly
	def fly(self):
		self.health -= 10
		return self
	# This method prints a message and then calls parent display_health method.
	def display_health(self):
		print "I am a dragon."
		super(Dragon, self).display_health()
		return self

class Dolphin(Animal):
	def __init__(self, name, health=140):
		super(Dolphin, self).__init__(name, health)    # use super to call the Animal __init__ method
	# Swim
	def swim(self):
		self.health -= 5
		return self
	# Walk
	def walk(self):
		print "I can't walk silly!"
		return self
	# Walk
	def run(self):
		print "If I can't walk silly how do you expect me to run?"
		return self

# Have the animal walk() three times, run() twice, and display_health().
animal = Animal("Animal", 100)
animal.walk().walk().walk().run().run().display_health()

#Have the Dog walk() three times, run() twice, pet() once, and display_health().
dog = Dog("Dog")
dog.walk().walk().walk().run().run().pet()
dog.display_health()

#Have the Dragon walk() three times, run() twice, fly() twice, and display_health().
dragon = Dragon("Dragon")
dragon.walk().walk().walk().run().run().fly().fly()
dragon.display_health()

# Now try creating a new Animal and confirm that it can not call the pet() and fly() methods, and its
# display_health() is not saying 'this is a dragon!'. Also confirm that your Dog class can not fly().
dolphin = Dolphin("dolphin")
dolphin.walk().walk().walk().run().run().swim().swim()
dolphin.display_health()

try:
	dog.fly()
except Exception as e:
	print(e)