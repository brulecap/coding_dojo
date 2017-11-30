# Assignment: Call Center
#You're creating a program for a call center. Every time a call comes in you need a way to
# track that call. One of your program's requirements is to store calls in a queue while
# callers wait to speak with a call center employee.

#You will create two classes. One class should be Call, the other CallCenter.

#Call Class
#	Create your call class with an init method. Each instance of Call() should have:
# 	Attributes:
#		unique id
#		caller name
#		caller phone number
#		time of call
#		reason for call
# 	Methods:
#		display: that prints all Call attributes.
# CallCenter Class
#	Create your call center class with an init method. Each instance of CallCenter() should have the following attributes:
#	Attributes:
#		calls: should be a list of call objects
#		queue size: should be the length of the call list
#	Methods:
#		add: adds a new call to the end of the call list
#		remove: removes the call from the beginning of the list (index 0).
#		info: prints the name and phone number for each call in the queue as well as the length of the queue.
# You should be able to test your code to prove that it works. Remember to build one piece at a time and test as you go for easier debugging!
# Ninja Level: add a method to call center class that can find and remove a call from the queue according to the phone number of the caller.
# Hacker Level: If everything is working properly, your queue should be sorted by time, but what if your calls get out of order?
# Add a method to the call center class that sorts the calls in the queue according to time of call in ascending order.
import datetime
import time
class Call(object):
	def __init__(self, name, number, reason):
		self.name = name
		self.number = number
		self.time = datetime.datetime.now()
		self.reason = reason
		self.id =id(self)
	# This method displays all instance variables
	def display(self):
		print "Name: " + self.name
		print "Number: " + self.number
		print self.time
		print "Reason: " + self.reason
		print "ID: " + str(self.id)
		return self

class CallCenter(object):
	def __init__(self):
		self.calls = []
		self.queue_size = 0
	# This method displays all instance variables
	def display(self):
		print "Queue size: " + str(self.queue_size)
		for call in self.calls:
			call.display()
	# Add new call
	def add(self, name, number, reason):
		call = Call(name, number, reason)
		self.calls.append(call)
		self.queue_size += 1
		return self
	# Remove call from top of list
	def remove(self, number=None):
		if number == None:
			self.calls.pop(0)
			self.queue_size -= 1
		else:
			for call in self.calls:
				if call.number == number:
					call_index = self.calls.index(call)
					self.calls.pop(call_index)
		return self
	def sort(self):
		self.calls.sort(key=lambda call: call.time)
		return self

################ Test cases ################
#call1 = Call("Bruce", "571-225-3512", "Complaint")
#call1.display()
#call1 = Call("John", "307-555-5555", "Problem")
#call1.display()
call_center = CallCenter()
call_center.add("Bruce", "571-225-3512", "Complaint")
time.sleep(5)
call_center.add("John", "307-555-5555", "Problem")
time.sleep(5)
call_center.add("Frank", "555-555-5555", "Question")
################ Rearrange to test sort ################
temp = call_center.calls[0]
call_center.calls[0] = call_center.calls[2]
call_center.calls[2] = temp 
call_center.display()
#call_center.remove("307-555-5555")
#call_center.display()
#print "Remove again"
#call_center.remove()
#call_center.display()
call_center.sort()
call_center.display()