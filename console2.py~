#!/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class Prac(cmd.Cmd):

    prompt = "(hbnh) "
    classes = [
            "BaseModel", "User", "City", "State", "Amenity", "Place", "Review"
            ]

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new = eval(arg)()
            storage.save()
            print(new.id)

    def do_show(self, arg):
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
        else:
            strn = f"{arg[0]}.{arg[1]}"
            try:
                inst = storage.all()[strn]
                print(inst)
            except Exception:
                print("** no instance found **")

    def do_destroy(self, arg):
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
        else:
            strn = "{}.{}".format(arg[0], arg[1])
            try:
                del storage.all()[strn]
                storage.save()
            except Exception:
                print("** no instance found **")

    def do_all(self, arg):
        inst = storage.all()
        arg = arg.split()
        lis = []

        if len(arg) == 0:
            for instance in inst.values():
                lis.append(instance.__str__())
        else:
            if arg[0] not in self.classes:
                print("** class doesn't exist **")
                return
            else:
                for instance in inst.values():
                    if instance.__class__.__name__ == arg[0]:
                        lis.append(instance.__str__())
        print(lis)

    def do_update(self, arg):
        arg = arg.split()
        objects = storage.all()

        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif len(arg) > 1:
            try:
                instance = objects["{}.{}".format(arg[0], arg[1])]
            except Exception:
                print("** no instance found **")
                return
            if len(arg) == 2:
                print("** attribute name missing **")
            elif len(arg) == 3:
                print("** value missing **")
            else:
                attr = arg[2]
                value = str(arg[3])
                strings = ["\"", "\'"]
                if value[0] in strings:
                    value = value.strip("'\"")
                else:
                    dot = False
                    letter = False
                    for c in value:
                        if c.isalpha():
                            letter = True
                        if c == ".":
                            dot = True
                    if letter is True:
                        value = str(value)
                    elif dot is True:
                        value = float(value)
                    else:
                        value = int(value)
                setattr(instance, attr, value)

                storage.save()


if __name__ == "__main__":
    Prac().cmdloop()
