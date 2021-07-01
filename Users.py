class Users:
    
    def __init__(self, name, user_id, password, bill, rental_details):
        self.name = name
        self.user_id = user_id
        self.password = password
        self.bill = bill
        self.rental_details = rental_details

    def getPassword(self):
        return self.password

    def getUserID(self):
        return self.user_id

    def getBill(self):
        return self.bill

    def setBill(self, total_price):
        self.bill += total_price

    def setRentalDetails(self, bill_details):
        self.rental_details += bill_details

    def getRentalDetails(self):
        return self.rental_details 
    
    def __str__(self):
        return f'''==============================
                 \nName: {self.name} 
                 \nUser ID: {self.user_id}
                 \nBill: $ {self.bill}
                 \nRental Details: {self.rental_details}
                 '''
     
    
