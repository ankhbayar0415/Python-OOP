from Bikes import Bikes

class ElectricBikes(Bikes):
    
    def __init__(self, bike_type, bike_name, bike_description, stock, hourly_price, insurance_rate):
        self.insurance_rate = insurance_rate
        Bikes.__init__(self, bike_type, bike_name, bike_description, stock, hourly_price)

    def getInsurance(self):
        return self.insurance_rate
    
    
    def getEffectivePrice(self, duration, number_of_bikes):
        if number_of_bikes <= 0:
            print("Number of bikes should be positive!")
            return 0
        elif number_of_bikes > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return 0
        else:
            self.stock -= number_of_bikes     
            tot = (self.hourly_price * duration) * number_of_bikes       
            return  (tot + (self.insurance_rate * duration))
     
    def printIt(self):
        return super().printIt() + \
                 "\nInorder to rent an electric bike, you should get insurance provided by us" + \
                 "\nInsurance price per hour: {}".format(self.insurance_rate)


    
