class box:

    def __init__(self , color , version , name):
        self.color = color
        self.version = version
        self.name = name
        print("instanse created" , color , version , name)


    def sayhello(self): 
        print("Hello. version: " , self.version , self.name)

box_obj = box("black",3.2 , "mahdi")
box_obj.sayhello()



