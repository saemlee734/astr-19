'''
Write a Python program that declares a class describing your 
favorite animal. Have the data members of the class represent
the following physical parameters of the animal: length of the 
arms (float), length of the legs (float), number of eyes (int),
does it have a tail? (bool), is it furry? (bool). Write an
initialization function that sets the values of the data 
members when an instance of the class is created. Write 
a member function of the class to print out and describe 
the data members representing the physical characteristics
of the animal.
'''

#my favorite animal is the snow leopard 

#create a class for snow leopard
class SnowLeopard:

    #define the parts of the snow leopard
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
       
        #length of arms (assuming that the front two legs count as the arms) as a float
        self.arm_length = float(arm_length)

        #length of legs as float 
        self.leg_length = float(leg_length)

        #number of eyes as an integer
        self.num_eyes = int(num_eyes)

        #it has a tail so a boolean
        self.has_tail = bool(has_tail)

        #it is furry so boolean
        self.is_furry = bool(is_furry)

    #def statment that will describe snow leopard
    def describe_physical_characteristics(self):

        #print characteristics
        print("Snow Leopard Physical Characteristics:")

        #print arm (assuming that the front two legs count as the arms) length
        print(f"Average Arm Length: {self.arm_length} inches")

        #print leg length
        print(f"Average Leg Length: {self.leg_length} inches")

        #print number of eyes
        print(f"Number of Eyes: {self.num_eyes}")

        #print that it has a tail
        print(f"Does it have a Tail?: {'Yes' if self.has_tail else 'No'}")

        #print that is it furry
        print(f"Is it Furry?: {'Yes' if self.is_furry else 'No'}")


#input of snow leopard characteristics based on google average snow leopard
snow_leopard_instance = SnowLeopard(26, 26, 2, True, True)

#run the print prompt with the information together
snow_leopard_instance.describe_physical_characteristics()
