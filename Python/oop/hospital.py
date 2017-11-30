#Assignment: Hospital
#You're going to build a hospital with patients in it! Create a hospital class.
#Before looking at the requirements below, think about the potential characteristics of each patient and hospital.
#How would you design each?
# Patient:
#	Attributes:
#		Id: an id number
#		Name
#		Allergies
#		Bed number: should be none by default
# Hospital
#	Attributes:
#		Patients: an empty array
#		Name: hospital name
#		Capacity: an integer indicating the maximum number of patients the hospital can hold.
#	Methods:
#		Admit:
#			Add a patient to the list of patients. Assign the patient a bed number. If the
#			length of the list is >= the capacity do not admit the patient. Return a message either
#			confirming that admission is complete or saying the hospital is full.
#		Discharge:
#			Look up and remove a patient from the list of patients. Change bed number for that patient back to none.
# This is a challenging assignment. Ask yourself what input each method requires and what output you will need.
class Patient(object):
	def __init__(self, name, allergies, bed_number=None):
		self.name = name
		self.bed_number = bed_number
		# Allergies should be an array of strings. i.e. ['penicillin', 'nuts', 'shellfish']
		self.allergies = allergies
		# I don't think this ID is not unique run to run.
		# It would need to be changed if a database was connected and use the unique db auto increment id perhaps. 
		self.id =id(self)
	# This method displays all instance variables
	def display(self):
		print "Name: " + self.name
		print "Bed number: " + str(self.bed_number)
		print "ID: " + str(self.id)
		for allergy in self.allergies:
			print "Allergy: " + allergy
		return self

class Hospital(object):
	def __init__(self, name, capacity):
		self.name = name
		self.capacity = capacity
		self.patients = []
	# This method displays all instance variables
	def display(self):
		print "Name: " + self.name
		print "Capacity: " + str(self.capacity)
		for patient in self.patients:
			patient.display()
		return self
	# Admit a patient
	def admit(self, name, allergies, bed_number=None):
		if len(self.patients) >= self.capacity:
			return "No room"
		else:
			patient = Patient(name, allergies, bed_number)
			self.patients.append(patient)
			return "Admitted"

	def discharge(self, name):
		return_text = ""
		for patient in self.patients:
			if patient.name == name:
				patient.bed_number = None
				patient_index = self.patients.index(patient)
				self.patients.pop(patient_index)
				return_text = name + " discharged."
			else:
				return_text = name + " was not found."
		return return_text

hospital = Hospital("Bad Samaritan", 3)
print hospital.admit("Bruce", [], "1A")
print hospital.admit("John", ['nuts', 'shellfish'], "2A")
print hospital.admit("Frank", ['penicillin'])
print hospital.admit("Tom", ['penicillin', 'nuts', 'shellfish'], "3A")
hospital.display()
print hospital.discharge("John")
print hospital.admit("Tom", ['penicillin', 'nuts', 'shellfish'], "3A")
hospital.display()