class Greeter:

	def __init__(self):
		self.f_name = ''
		self.l_name = ''

	def get_formatted_name(self):
		full_name = f"{self.f_name} {self.l_name}"
		return full_name.title()

	def get_name_from_user(self, first_name = input("First name: "), last_name = input("Last name: ")):
		while True:
			self.f_name = first_name
			if self.f_name == 'q':
				break
			self.l_name = last_name
			if self.l_name == 'q':
				break		
			formatted_name = self.get_formatted_name()
			return formatted_name
		
	