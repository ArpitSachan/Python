import time
import datetime

class BikeRental:

	def __init__(self, stock=0):
		self.stock=stock

	def displaystock(self):
		print("{} bikes are available for rent".format(self.stock))
		return self.stock

	def hourly(self, n):
		n=int(n)
		if(n<=0):
			print("Please enter a valid value.")
		elif n>int(self.stock):
			print("Sorry, Out of stock!")
		else:
			now=datetime.datetime.now()
			print("Rented {} bike(s) at {}".format(n, now.hour))
			print("Chrges are $5 hourly for each bike")

			self.stock-=n
			return now

	def daily(self, n):
		if(n<=0):
			print("Please enter a valid value.")
		elif n>self.stock:
			print("Sorry, Out of stock!")
		else:
			now=datetime.datetime.now()
			print("Rented {} bike(s) at {}".format(n, now.hour))
			print("Chrges are $20 hourly for each bike")

			self.stock-=n
			return now

	def weekly(self, n):
		if(n<=0):
			print("Please enter a valid value.")
		elif n>self.stock:
			print("Sorry, Out of stock!")
		else:
			now=datetime.datetime.now()
			print("Rented {} bike(s) at {}".format(n, now.hour))
			print("Chrges are $5 hourly for each bike")

			self.stock-=n
			return now

	def returnBike(self, reuqest):
		time, basis, bikes=reuqest
		bill=0
		print(time)
		if time and bikes:
			self.stock+=int(bikes)
			now=datetime.datetime.now()
			period=int(now)-int(time)

			if(basis==1):
				bill=round(period.seconds/360000)*5*bikes
			elif basis==2:
				bill=round(period.days)*20*bikes
			else:
				bill=round(period.days/7)*60*bikes

			if(bikes>=3):
				print("You get a discount of 70%")
				bill=bill*0.7
			print("Pay {} fast!".format(bill))
			return bill
		else:
			return 3

class Customer:
	def __init__(self):
		self.bikes=0
		self.basis=0
		self.time=0
		self.bill=0

	def requestBike(self):
		bikes= input("How many bike you would like to rent?: ")
		self.bikes=bikes
		return self.bikes

	def returnBike(self):
		if(self.basis and self.time and self.bikes):
			return self.basis, self.time, self.bikes
		else:
			return (0,0,0)


cust=Customer()
x=cust.requestBike()
cust.basis=input("Basis: ")
cust.bikes=input("bikes: ")
cust.time=datetime.datetime.now()
y=cust.returnBike()
rent=BikeRental(10)
rent.hourly(x)
time.sleep(3)

rent.returnBike(y)