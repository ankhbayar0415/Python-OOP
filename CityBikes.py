from Bikes import Bikes

class CityBikes(Bikes):
    
    def __init__(self, bike_type, bike_name, bike_description, stock, hourly_price, discount, valid_hour):
        self.discount = discount
        self.valid_hour = valid_hour
        Bikes.__init__(self, bike_type, bike_name, bike_description, stock, hourly_price)

    def getDiscount(self):
        return self.discount

    def getHour(self):
        return self.valid_hour
    
    def getEffectivePrice(self, duration, number_of_bikes):
        if number_of_bikes <= 0:
            print("Number of bikes should be positive!")
            return 0
        elif number_of_bikes > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return 0
        else:
            self.stock -= number_of_bikes
            if duration >= self.valid_hour:     
                tot = (self.hourly_price * duration) * (1 - (self.discount * 0.01)) * number_of_bikes                
            else:
                tot = (self.hourly_price * duration)* number_of_bikes                
            return tot - 5
     
    def printIt(self):
        return super().printIt() + \
                 "\nDiscount: {} %".format(self.discount) + \
                 "\nNote: Discount only available for those who are renting more than {}".format(self.valid_hour) + \
                 "\nBonus Discount: Summer is coming!!! Everyone will get $5 discount on your checkout!!!"


       

    
