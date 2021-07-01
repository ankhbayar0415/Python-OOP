import csv
import os
import pandas as pd

from Bikes import Bikes
from MountainBikes import MountainBikes
from CityBikes import CityBikes
from ElectricBikes import ElectricBikes
from Users import Users

def cls():
	os.system('cls')

def main():

	login_page = "login.txt"
	users_file = "Users.csv"
	bikes_file = "Bikes.csv"
	rent_page = "rent.txt"
	
	user_list = []
	bike_list = []

	with open(bikes_file, mode='r') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		mountain_bike_count = 0
		electric_bike_count = 0
		city_bike_count = 0
		line_count = 0
		for row in csv_reader:
			if line_count == 0:
				line_count += 1
			else:
				if row[0] == "Mountain":
					bike_list.append(MountainBikes(row[0],row[1], row[2], int(row[3]), float(row[4]), float(row[5]), int(row[6])))
					mountain_bike_count += int(row[3])
				elif row[0] == "City":
					bike_list.append(CityBikes(row[0], row[1], row[2], int(row[3]), float(row[4]), float(row[5]), int(row[6])))
					city_bike_count += int(row[3])
				elif row[0] == "Electric":
					bike_list.append(ElectricBikes(row[0], row[1], row[2], int(row[3]), float(row[4]), float(row[7])))
					electric_bike_count += int(row[3])
				line_count += 1

	with open(users_file, mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		line_count = 0
		for row in csv_reader:
			if line_count == 0:
				line_count += 1
			user_list.append(Users(row["Full Name"], row["User ID"], row["Password"], float(row["Bill"]), row["Rental Details"]))
			line_count += 1

	while True:
		f = open(login_page, "r")
		print(f.read())
		f.close()
		
		userChoice = int(input("Enter your choice: "))
	
		try:
			userChoice = int(userChoice)
		except ValueError:
			print("That's not an int!")
			continue
	
		if userChoice == 1:
			cls()            
			while True:
				cls()
				user_id = input(" Please Enter your user name: ")
				password = input(" Please Enter your password: ")
				yes = False

				for user in user_list:
					if user.getUserID() == user_id and user.getPassword() == password:
						yes = True
					else:
						yes = False
				if yes == True:
					break
				else:
					print("\nWrong username or password.\n")
					continue

			
			while True:
				cls()
				f = open(rent_page, "r")
				print(f.read())
				f.close()
				userChoice = int(input("Enter your choice: "))

				try:
					userChoice = int(userChoice)
				except ValueError:
					print("That's not an int!")
					continue

				if userChoice == 1:
					cls()
					print ("\n==============================================================",
							"\n	We currently have {} mountain bikes available   ".format(mountain_bike_count),
							"\n==============================================================")
					i = 0
					for bike in bike_list:
						if bike.bike_type == "Mountain":
							i += 1
							print("++++++++++++++++++++++++++++++++++++")
							print("\t\tOPTION No. {}".format(i))
							print(bike.printIt())
							print("++++++++++++++++++++++++++++++++++++")
							print("\n")
							

					print(". . . . . . . . . . . . . . . . . . . . . . . . .")
					while True:
						userChoice = int(input("Enter the option number: "))

						try:
							userChoice = int(userChoice)
						except ValueError:
							print("That's not an int!")
							continue

						if userChoice > 0 and userChoice <= i:
							duration = int(input("How many hours do you want to rent?"))
							number_of_bikes = int(input("How many bikes?"))
							
							j = 0
							for bike in bike_list:
								if bike.bike_type == "Mountain":
									j += 1
									if j == userChoice:
										total_price = bike.getEffectivePrice(duration, number_of_bikes)
										break

							bill_details = bike.getName() + " for " + str(duration) + " hours."

							print(bill_details)
							print("Total Payment Value: ", total_price)
							print("Successfull. Your account bill is now updated.")

							user.setBill(total_price)
							user.setRentalDetails(bill_details)
						
							df = pd.read_csv("Users.csv")
							df.loc[df["User ID"]==user_id, "Bill"] = user.getBill()
							df.loc[df["User ID"]==user_id, "Rental Datails"] = user.getRentalDetails()
							df.to_csv("Users.csv", index=False)
					
							df = pd.read_csv("Bikes.csv")
							df.loc[df["Bike Name"] == bike.getName(), "Stock"] = bike.stock
							df.to_csv("Bikes.csv", index=False)

							break
						else:
							print("Please enter valid option number!")
							continue
					break
							
				elif userChoice == 2:
					cls()
					print ("\n==============================================================",
							"\n	We currently have {} electric bikes available   ".format(electric_bike_count),
							"\n==============================================================")
					i = 0
					for bike in bike_list:
						if bike.bike_type == "Electric":
							i += 1
							print("++++++++++++++++++++++++++++++++++++")
							print("\t\tOPTION No. {}".format(i))
							print(bike.printIt())
							print("++++++++++++++++++++++++++++++++++++")
							print("\n")
							

					print(". . . . . . . . . . . . . . . . . . . . . . . . .")
					while True:
						userChoice = int(input("Enter the option number: "))

						try:
							userChoice = int(userChoice)
						except ValueError:
							print("That's not an int!")
							continue

						if userChoice > 0 and userChoice <= i:
							duration = int(input("How many hours do you want to rent?"))
							number_of_bikes = int(input("How many bikes?"))
							
							j = 0
							for bike in bike_list:
								if bike.bike_type == "Electric":
									j += 1
									if j == userChoice:
										total_price = bike.getEffectivePrice(duration, number_of_bikes)
										break

							bill_details = bike.getName() + " for " + str(duration) + " hours."

							print(bill_details)
							print("Total Payment Value: ", total_price)
							print("Successfull. Your account bill is now updated.")

							user.setBill(total_price)
							user.setRentalDetails(bill_details)
							
							df = pd.read_csv("Users.csv")
							df.loc[df["User ID"]==user_id, "Bill"] = user.getBill()
							df.loc[df["User ID"]==user_id, "Rent Datails"] = user.getRentalDetails()
					
							df = pd.read_csv("Bikes.csv")
							df.loc[df["Bike Name"] == bike.getName(), "Stock"] = bike.stock
							
							break
						else:
							print("Please enter valid option number!")
							continue
					break

				elif userChoice == 3:
					cls()
					print ("\n==============================================================",
							"\n	We currently have {} city bikes available   ".format(city_bike_count),
							"\n==============================================================")
					i = 0
					for bike in bike_list:
						if bike.bike_type == "City":
							i += 1
							print("++++++++++++++++++++++++++++++++++++")
							print("\t\tOPTION No. {}".format(i))
							print(bike.printIt())
							print("++++++++++++++++++++++++++++++++++++")
							print("\n")
							

					print(". . . . . . . . . . . . . . . . . . . . . . . . .")
					while True:
						userChoice = int(input("Enter the option number: "))

						try:
							userChoice = int(userChoice)
						except ValueError:
							print("That's not an int!")
							continue

						if userChoice > 0 and userChoice <= i:
							print("\n")
							duration = int(input("How many hours do you want to rent?"))
							print("\n")
							number_of_bikes = int(input("How many bikes?"))
							print("\n")
							j = 0
							for bike in bike_list:
								j += 1
								if bike.bike_type == "City":
									if j == userChoice:
										total_price = bike.getEffectivePrice(duration, number_of_bikes)
										break
									
							cls()			
							bill_details = bike.getName() + " for " + str(duration) + " hours."

							print(bill_details)
							print("Total Payment Value: ", total_price)
							print("Successfull. Your account bill is now updated.")

							user.setBill(total_price)
							user.setRentalDetails(bill_details)
							
							df = pd.read_csv("Users.csv")
							df.loc[df["User ID"]==user_id, "Bill"] = user.getBill()
							df.loc[df["User ID"]==user_id, "Rent Datails"] = user.getRentalDetails()
					
							df = pd.read_csv("Bikes.csv")
							df.loc[df["Bike Name"] == bike.getName(), "Stock"] = bike.stock
							
							break
						else:
							print("Please enter valid option number!")
							continue
					break

				elif userChoice == 4:
					cls()
					print(user.__str__())
					userChoice = input("Enter 'q' to go back: ")
					continue
					

				elif userChoice == 5:
					quit()
				else:
					print("Please enter valid option number!")
					continue

		elif userChoice == 2:
			cls()
			print("==== User Registration system ====")
			user_name = input("Enter your full name: ")

			while True:
				user_id = input("Enter your user name: ")
				matched = 0

				for user in user_list:
					if user.getUserID() == user_id:
						matched = 1
					else:
						matched = 0
				if matched == 0:
					break
				else:
					print("\nUser ID already taken!!! Choose another one")
					continue


			password = input("Enter your password: ")
		
			user_list.append(Users(user_name, user_id, password, 0, ""))

			mydict =[{'Full Name' : user_name, 'User ID': user_id, 'Password': password, 'Bill': '0', 'Rental Details': '.'}] 
			fields = ['Full Name', 'User ID', 'Password', 'Bill', 'Rental Details'] 
			
			with open(users_file, 'a') as csvfile:
				writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames = fields) 
				writer.writerows(mydict) 

			cls()
			print("Account succesfully created...")

			continue
		elif userChoice == 3:
			quit()
   
main()
