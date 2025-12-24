# modules and global variables
from abc import ABC,abstractmethod
import string
import random


# create password generator abstract class
class PasswordGeneratorAbstract(ABC):
    @abstractmethod
    def generate_password(self,length=8):
        pass
        
    

# create numeric password generators
class NumericPasswordGenerator(PasswordGeneratorAbstract):
    letters = string.digits
    
    def generate_password(self,length=8):
        
       
        return "".join (str(random.choice(self.letters)) 
                        for _ in  range(length))      

# create letter password generators
class LettersPasswordGenerator(PasswordGeneratorAbstract):
    letters = string.ascii_letters
    
    def generate_password(self, length=8):
        return "".join (str(random.choice(self.letters)) 
            for _ in  range(length))   

# create mixed password generator
class MixedPasswordGenerator(PasswordGeneratorAbstract):
    letters = string.ascii_letters + string.digits
    def generate_password(self, length=8):
        return "".join (str(random.choice(self.letters)) 
            for _ in  range(length))   



# run the application
generator = MixedPasswordGenerator()

print(generator.generate_password())







