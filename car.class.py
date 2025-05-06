class car:
    def __init__(self, company,name,model,color):
        self.company = company
        self.name = name
        self.model =model
        self.color = color  
        print("car created")

    def get_info (self):
        print(self.company,self.name,self.model,self.color)

car_1 = car("toyota", "GTR R35", "2019", "white") 
car_1.get_info()

car_2 = car("bmw", "M5", "2022", "Black") 
car_2.get_info()    