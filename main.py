from cinema import Cinema

row = int(input('Enter the number of rows:\n'))
seats = int(input("Enter the number of seats in each row:\n"))
if __name__ == "__main__":
	choice = 1
	while choice != 7:
		print('\n=========WELCOME TO BOOK YOUR MOVIE==========')
		print('-----------------------------------------')
		print('1. Show the seats')
		print('2. Buy a Ticket')
		print('3. Stastics')
		print('4. Show Booked Bickets user Info')
		print('0. Exit')
		
		choice = int(input('ENTER YOUR CHOICE: '))
		if choice == 1:
			show_seats()
		elif choice == 2:
			buy_ticket()
		elif choice == 3:
			show_statistics()
		elif choice == 4:
			show_booked_ticket()
		elif choice == 0:
			Exit()
		else:
			print('WRONG INPUT. ENTER THE CHOICE AGAIN')


