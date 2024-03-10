#!/usr/bin/python3
import cmd
import math as m

class Myconsole(cmd.Cmd):
    intro = "Welcome to your calculator Charity :-)"
    prompt = "(charity): "


    def do_add(self, arg):
        """adds two numbers"""
        num1, num2 = map(float, arg.split())
        result = num1 + num2
        print (f"Result: {result}") 

    def do_sub(self, arg):
        """subtracts a number from the initial"""
        num1, num2 = map(float, arg.split())
        result = num1 - num2
        print (f"Result: {result}")

    def do_div(self, arg):
        """divides two numbers"""
        num1, num2 = map(float, arg.split())
        result = num1 / num2
        print (f"Result: {result}")

    def do_mult(self, arg):
        """multiplies two numbers"""
        num1, num2 = map(float, arg.split())
        result = num1 * num2
        print (f"Result: {result}")
    
    def do_exit(self, _):
        """exits the command-line interface"""
        return True
    
    def do_sin(self, arg):
        """returns the sin of a number"""
        result = m.sin(float(arg))
        print (f"Result: {result}")
    
    def do_cos(self, arg):
        """returns the cos of a number"""
        result = m.cos(float(arg))
        print (f"Result: {result}")

    def do_tan(self, arg):
        """returns the tan of a number"""
        result = m.tan(float(arg))
        print (f"Result: {result}")
    
    def do_log(self, arg):
        """returns the log_10 of a number"""
        result = m.log10(float(arg))
        print (f"Result: {result}")

    def do_squareroot(self, arg):
        """returns the squareroot of a number"""
        result = m.sqrt(float(arg))
        print (f"Result: {result}")
    
#how to implement sin, log, cos and tan
    
if __name__ == "__main__":
    Myconsole().cmdloop()
