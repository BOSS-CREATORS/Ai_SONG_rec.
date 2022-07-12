
####################################################
#               SONG RECOMMENDATIONS               #
####################################################

from userinformation import UserInformation
from DataBase import Database
from bot import AI

####################################################
#               CREATING DATABASE                  #
####################################################

Var = UserInformation().Create()    
result = Database().Create()

####################################################
#              RUNNING THE SYSTEM                  #
####################################################
AI().Run()

####################################################

