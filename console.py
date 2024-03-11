#!/usr/bin/python3
""" Defines console class the entry point of hbnb Project
"""


from cmd import Cmd
from models import storage
from models.engine.errors import *
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = storage.models


class HBNBCommand(Cmd):
    """ Make some HBNB commands """
    prompt = "(hbnb) "

    # Commands Allowed
    def do_EOF(self, args):
        """Exit program in non interactive mode"""
        return True

    def do_quit(self, args):
        """Exit commands that close program"""
        return True

    def emptyline(self):
        """Empty line do nothing"""
        pass

    def do_create(self, args):
        """creates new instance of base model
        Print error if name is missing
        """
        args, n = parse(args)

        if not n:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif n == 1:
            temp = eval(args[0])()
            print(temp.id)
            temp.save()
        else:
            print("** Too many argument for create **")
            pass

    def do_show(self, arg):
        """Show an Instance of base Model on sent ModelName and id
        Print error message if either Model or instance_id is missing
        Print an Error message for wrong Model or instance_id"""
        args, n = parse(arg)

        if not n:
            print("** class name missing **")
        elif n == 1:
            print("** instance id missing **")
        elif n == 2:
            try:
                inst = storage.find_by_id(*args)
                print(inst)
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")
        else:
            print("** Too many argument for show **")
            pass

    def do_all(self, args):
        """Display string representations of all instances of a given class.
        If no class is specified, display all initiated objects."""
        args, n = parse(args)

        if n < 2:
            try:
                print(storage.find_all(*args))
            except ModelNotFoundError:
                print("** class doesn't exist **")
        else:
            print("** Too many argument for all **")
            pass

    def do_destroy(self, arg):
        """Delete an Instance of Model base on sent ModelName and id."""
        args, n = parse(arg)

        if not n:
            print("** class name missing **")
        elif n == 1:
            print("** instance id missing **")
        elif n == 2:
            try:
                storage.delete_by_id(*args)
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")
        else:
            print("** Too many argument for destroy **")
            pass

    def do_update(self, arg):
        """Updates an instance base on its id
        Throws error for missing arguments"""
        args, n = parse(arg)
        if not n:
            print("** class name missing **")
        elif n == 1:
            print("** instance id missing **")
        elif n == 2:
            print("** attribute name missing **")
        elif n == 3:
            print("** value missing **")
        else:
            try:
                storage.update_one(*args[0:4])
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")

    def default(self, arg):
        """Override default method to handle class methods"""
        if '.' in arg and arg[-1] == ')':
            if arg.split('.')[0] not in classes:
                print("** class does not exist **")
                return
            return self.handle_class_methods(arg)
        return Cmd.default(self, arg)

    def do_models(self, arg):
        """Prints all registered Models to stdout"""
        print(*classes)

    def handle_class_methods(self, arg):
        """Handle Class Methods to std
        """

        printable = ("all(", "show(", "count(", "create(")
        try:
            val = eval(arg)
            for x in printable:
                if x in arg:
                    print(val)
                    break
            return
        except AttributeError:
            print("** invalid method **")
        except InstanceNotFoundError:
            print("** no instance found **")
        except TypeError as te:
            field = te.args[0].split()[-1].replace("_", " ")
            field = field.strip("'")
            print(f"** {field} missing **")
        except Exception as e:
            print("** invalid syntax **")
            pass


def parse(line: str):
    """Split lines by spaces a"""
    args = shlex.split(line)
    return args, len(args)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
