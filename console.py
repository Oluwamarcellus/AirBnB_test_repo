#!/usr/bin/python3
""" Airbnb Clone """
from models.base_model import BaseModel
from models import storage
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.user import User
from models.city import City
import cmd

prompt = '(hbnb)'
classes = ['City', 'Place', 'State', 'User', 'Amenity', 'User', 'BaseModel', 'Review']
dotcmd  = ['.all()']

class HBNBCommand(cmd.Cmd):
    """Creates a new instance of a given class, saves it \
(to the JSON file) and prints the id."""
    def do_create(self, line):
        if line == "":
            print("** class name missing **")
        if line not in HBNBCommand.classes:
            print("** class doesn't exist ** ")
        else:
            if line == "BaseModel":
                obj = BaseModel()
            elif line == "User":
                obj = User()
            elif line == "State":
                obj = State()
            elif line == "Place":
                obj = Place()
            elif line == "Amenity":
                obj == Amenity()
            elif line == "Review":
                obj = Review()
            storage.save()
            print(obj.id)
            
    def do_show(self, line):
        arg = line.split()
        if line == "":
            print("** class name missing **")   
        if arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        if arg < 2:
            print("** instance id missing **")
        else:
            className = arg[0]
            objId = arg[1]
            key = className + "." + objId
        try:
            print(storage.all()[key])
        except KeyError:
            print("** no instance found **")
    def do_destroy(self, line):
        arg = line.split()
        if line == "":
            print('** class name missing **')
        if arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist ** ")
        else:
            className = arg[0]
            objId = arg[1]
            key = className + "." + objId
        try:
            del storage.all()[key]
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name. Ex: $ all BaseModel or $ all
        """
        args = line.split()
        result = []
        if len(args) != 0:
            if args[0] not in HBNBCommand.classes:
                print('** class doesn\'t exist **')
                return
            else:
                for key, value in storage.all().items():
                    if type(value).__name__ == args[0]:
                        result.append(value.__str__())
        else:
            for key, value in storage.all().items():
                result.append(value.__str__())
        print(result)  
            
    def do_update(self, line):
        arg = line.split()
        if line == "":
            print('** class name missing **')
        if arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist ** ")
        if arg < 2:
            print('** instance id missing **')
        if arg < 3:
            print("** attribute name missing **")
        if arg < 4:
            print("** value missing **")
        className = arg[0]
        objId = arg[1]
        attr = arg[2]
        value = arg[3]
        noUpdate = ['id', 'created_at', 'updated_at']
        
        for attr in noUpdate:
            print("** attribute can\'t be updated **")
            return
        """String validity test"""
        if value[0] != '"' and value[-1] != '"' or value[0]  != "'":
            if value[0] != "'":
                print("** A string argument must be between \
# double quotes **")
                return
            value = value[1:-1]
        else:
            try:
                for i in value:
                    if i == ".":
                        value = float(value)
                        break
                    else:
                        value = int(value)
            except ValueError:
                print("** A string argument must \
# be between double quote **")
        if (attr[0] == '"' and attr[-1] == '"')\
               or attr[0] == "'" or attr[-1] == "'":
                if attr[0] != '"' or attr[-1] == "'":
                    print("** A string argument must be between \
# double quotes **")
                    return
                attr = attr[1:-1]
                """String validity ends"""
        key = className + "." + objId
        
        try:
            instance = storage.all()[key]
            instance.__dict__[attr] = value
            instance.save()
            pass
        except KeyError:
            print("** no instance found **")

    def do_quit(self, line):
        """Quit command to exit from cmd"""
        return True

    def do_EOF(self, line):
        """Ctrl D - to kill the program or exit from cmd"""
        print()
        return True

    def emptyline(self):
        """Empty line + Enter shouldn't execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
