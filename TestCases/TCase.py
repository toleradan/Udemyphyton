# #import statement
# import Library.CommonModule
#
# objA= Library.CommonModule.A()
# objA.startBrowsingA()
#
#
# objB= Library.CommonModule.B()
# objB.startBrowsingB()

# #from statement
# from Library.CommonModule import A
# objA=A()
# objA.startBrowsingA()

# #importing the file path
# import Pages.Login.ABC
# objC = Pages.Login.ABC.C()
# objC.mytesting()

#from statement with file path
from Pages.Login.ABC import C
obj = C()
obj.mytesting()