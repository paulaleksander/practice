class Greeter:

	def __init__(self):
		self.f_name = ''
		self.l_name = ''

	def get_formatted_name(self):
		full_name = f"{self.f_name} {self.l_name}"
		return full_name.title()

	def get_name_from_user(self):
		self.f_name = input("First name: ")	
		self.l_name = input("Last name: ")			
		formatted_name = self.get_formatted_name()
		return formatted_name
	
