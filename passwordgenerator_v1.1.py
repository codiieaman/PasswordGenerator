"""Password geenrator program wri6ten in python 
    Project Initiated by: Anon
   Updated By: Aman Bhandari
   Email: vandari956@gmail.com"""


import random 

capital_letters = 'ABCDEFGHIKLMNOPQRSTVXYZ'
lower_letters = 'AbCDEFGHIKLMNOPQRSTVYZ'.lower()
special_characters = '@#$^&*()|?><<"?|/[]{\}'
numbers = '0123456789'


def weak_password():

	"""Generate password mix with upper letters,
	   lower letters and numbers  """

	password = ""
	group_of_selected_characters = []#list to group randomly selected characters
	
	for n in range(3):
		"""Select 3 characters from each of the 3 categories """
		selected_capital_letters = random.choice(capital_letters)
		selected_numbers = random.choice(numbers)
		selected_lower_letters = random.choice(lower_letters)

		#add each character to the list group_of_selected_characters
		group_of_selected_characters.append(selected_capital_letters)
		group_of_selected_characters.append(selected_numbers)
		group_of_selected_characters.append(selected_lower_letters)
	for character in group_of_selected_characters:#loops through each character in the list and add it to password
		password += character
	return password


def strong_password():

	"""Generate password mix with upper,
	   lower,numbers and special characters """

	password = ""
	group_of_selected_characters = [] #list to group randomly selected characters
	for n in range(6):
		"""Select 6 characters from each of the 4 categories """
		selected_capital_letters = random.choice(capital_letters)
		selected_numbers = random.choice(numbers)
		selected_lower_letters = random.choice(lower_letters)
		selected_special_characters = random.choice(special_characters)
        #add each character to the list group_of_selected_characters
		group_of_selected_characters.append(selected_capital_letters)
		group_of_selected_characters.append(selected_numbers)
		group_of_selected_characters.append(selected_lower_letters)
		group_of_selected_characters.append(selected_special_characters)
	for character in group_of_selected_characters: #loops through each character in the list and add it to password
		password += character
	return password

def main():
	"""calls weak and strong password generator functions"""


	print("""
    	Welcome to password generator 
    	You have two choices to choose
    	from.You can either choose to have 
    	a strong or weak password generated 
    	you.Have fun generating your password
    	     """)

	password_choice = int(input('''Enter [2] for strong password and [3] for weak password'''))#Users choice of password

	if password_choice == 2:
		password = strong_password()
		print('This is your password as requested >>>>  {} '.format(password))
	elif password_choice == 3:
		password = weak_password()
		print('This is your password as requested>>>   {} '.format(password))
	else:
		print('Invalid choice')

if __name__ == '__main__':
	main()
