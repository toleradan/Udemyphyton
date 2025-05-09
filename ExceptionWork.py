# try:
#     user_input1= input("Please enter your first number:" )
#     user_input2= input("Please enter your second number:" )
#
#     c = int(user_input1) + int(user_input2)
#     print(c)
# except:
#     print("Your input is incorrect, please enter correct data")
#
# finally:
#     print("This is finally")

from configparser import ConfigParser
#Created object of Configparser class
config = ConfigParser()

#To read data from config file
config.read("C:/Users/BSI-Corelate_Adan/PycharmProjects/TestAutomation/Config.cfg") #change the \ to /
config.read("./InputFiles/Config1.cfg") #change the \ to /

print(config.get("Section1","username"))
print(config.get("Section2","username"))

