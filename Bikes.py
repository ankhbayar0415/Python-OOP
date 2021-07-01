class Bikes():
    
    def __init__(self, bike_type, bike_name, bike_description, stock, hourly_price):
        self.bike_type = bike_type
        self.bike_name = bike_name
        self.bike_description = bike_description
        self.stock = stock
        self.hourly_price = hourly_price
    
    def getType(self):
        return self.bike_type

    def getName(self):
        return self.bike_name

    def getDesc(self):
        return self.bike_description

    def getPrice(self):
        return self.hourly_price

    def printIt(self):
        return "\nBike name: {}".format(self.bike_name) + \
               "\nDescription: {}".format(self.bike_description) + \
               "\nStock: {}".format(self.stock) + \
               "\nHourly price: {}".format(self.hourly_price)

    
