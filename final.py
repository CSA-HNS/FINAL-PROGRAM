#Hanzala Siddiqui
#Computer Programming I
#04/21/2017
import time
import os
class Cars(object):
    
    def __init__(self, brand, model, left, year, price):
        self.brand=brand
        self.model=model
        self.year=year
        self.left=left
        price=float(price)
        price=price*1000000
        self.price=price
    def add_car(self, car):
        carslist.append(car)
    def is_brand(self, ebrand):
        for car in carslist:
            if(car.brand==ebrand):
                if(car.price<=w):
                    return True
        return False
    def all_brand(self):
        cl=[]
        for car in carslist:
            if(car.price<=w):
                if(car.brand not in cl):
                    cl.append(car.brand)
        for i in cl:
            print(i)
    def is_model(self, emodel, ebrand):
        for car in carslist:
            if(car.brand==ebrand):
                if(car.model==emodel):
                    if(car.price<=w):
                        return True
        return False
    def all_model(self, ebrand):
        for car in carslist:
            if(car.brand==ebrand):
                if(car.price<=w):
                    print(car.model)
    def is_left(self, ebrand, emodel):
        for car in carslist:
            if(car.brand==ebrand):
                if(car.model==emodel):
                    if(int(car.left)>=1):
                        return True
                    else:
                        return False
    def pprice(self,ebrand,emodel):
        for car in carslist:
            if(car.brand==ebrand):
                if(car.model==emodel):
                    p=car.price
                    return p
    def buying(self, ebrand, emodel):
        for car in carslist:
            if(car.brand==ebrand):
                if(car.model==emodel):
                    x=car.year
                    return x
    def bought(self, ebrand, emodel):
        for car in carslist:
            if(car.brand==ebrand):
                if(car.model==emodel):
                    l=car.left
                    l=int(l)
                    l-=1
                    car.left=str(l)
        outfile = open("inventory.txt", "w")
        for car in carslist:
            p=int(car.price)
            p=p/1000000
            outfile.write(car.brand+" "+car.model+" "+car.left+" "+car.year+" "+str(p)+"\n")
        
        


def buy(brand, model, ccolor,wallet):
    x=carslist[0]
    year=x.buying(brand, model)
    price=x.pprice(brand, model)
    print("The car that you would like to buy is a "+ccolor+" "+str(year) +" "+ brand +" "+ model+ " priced at " +str(price))
    o=int(input("Enter 1 to buy the car. Enter 2 if you do not want to buy the car. "))
    if(o==1):
        wallet-=price
        x.bought(brand, model)
        print("You have bought a "+ccolor+" "+str(year) +" "+ brand +" "+ model+ " priced at " +str(price))
        print("Enjoy your Luxurious, Exclusive and Elite car from World Class Cars. ")
        time.sleep(5)
        quit()
    else:
        os.system('cls')
        menu()
def color():
    while True:
        ccolor=input("We will custom paint your car for you. What color would you like? ")
        return ccolor
        

def remaining(brand, model,wallet):
    x=carslist[0]
    if(x.is_left(brand, model)):
        ccolor=color()
        buy(brand, model,ccolor,wallet)
    else:
        print("Sorry, That car is not currently available in our inventory. ")
        return
    
def model(brand, wallet):
    while True:
        x=carslist[0]
        print("Here are your options: ")
        x.all_model(brand)
        model=input("Please enter a specific model of "+brand+" that you would like to buy a car of? ")
        model=model.lower()
        model=model.title()
        if(x.is_model(model, brand)):
            os.system('cls')
            remaining(brand, model,wallet)
        else:
            print("That is not an available model for the brand you want. ")
            time.sleep(3)
            os.system('cls')





def brand(wallet):
    while True:
        x=carslist[0]
        print("Here are your options: ")
        x.all_brand()
        
        brand=input("Hi "+ name+", please enter a specific brand that you would like to buy a car of? ")
        brand=brand.lower()
        brand=brand.title()
        x=carslist[0]
        if(x.is_brand(brand)):
            os.system('cls')
            model(brand,wallet)
        else:
            print("That is not an option! ")
            time.sleep(3)
            os.system('cls')

        
    
    
def buy_menu():
    
    global carlist
    carlist=[]
    global carslist
    carslist=[]
    fileref=open('inventory.txt', 'r')
    for line in fileref:
        carlist.append(line.split())
    fileref.close()
    for l in carlist:
        x=int(l[2])
        x+=1
        car=Cars(l[0], l[1], str(x), l[3], l[4])
        car.add_car(car)
    while True:
        try:
            wallet=int(input("What is your budget? (If you would like to trade in a car please add theat value to your budget and enter that sum.) "))
            global w
            w=wallet
            break
        except:
            print("Please enter your budget!")
    min=100000
    if(wallet<min):
        print("Sorry, but we do not have any cars in your budget! ")
        time.sleep(2)
        os.system('cls')
        menu()
    brand(wallet)

    
    
def menu():
    global name
    print("Welcome to World Class Cars. The most Luxurious, Exclusive and Elite cars in the world! ")
    name=input("What is your name? ")
    while True:
        try:
            option=int(input("""Would you like to:
1 - Buy a car
2 - Quit
Enter the number corresponding to what you would like to do.
"""))
            if(option==1):
                os.system('cls')
                buy_menu()
            elif(option==2):
                quit()
            else:
                print("Number entered was too large or small!")
        except:
            print("That is not an option! ")
    
    
        
menu()
