### Template for Code Reading Exercise

1. Where did you find the code and why did you choose it? (Provide the link)

https://github.com/CholoCantos/Food-Ordering-System

I found the code in the Git Hub when I was looking for codes for ordering systems.
I thought about creating a food-ordering system for our own project and wanted to see what other programmers have for ideas in this direction. 
It's not a super complex code to analyze, but I thought it was good that the code is so well structured and contains a lot of things that we have already learned and applied ourselves. I was able to recapitulate and practise what I had already learned.


1. What does the program do? What's the general structure of the program? 

The project is a food ordering system, which main items on the menu are pansit and lomi. The program provides different payment methods (Card payment, Cash payment, credit card payment or debit card payment). You can choose different options of food and drink from a menu and at the end enter the order adress and wether you want a receipt. 
The developers of the program have created an individual Python file for each function and also imported the required libraries there.
At the end they summarize everything in the main function. 

1. Function analysis: pick one function and analyze it in detail:

- What does this function do?
- What are the inputs and outputs?
- How does it work (step by step)?

# Import the base class for all payment methods
from ModeOfPayment import mode_of_payment 

# Defines a subclass of mode_of_payment specifically for handling cash transactions 
# -> It inherits characteristics shared payment behaviour from mode_of_payment-class like customer_name, amount and timeStamp
class cash_payment (mode_of_payment): 
  amount_given = 0.0                    # class-level variable to store the amount of cash received
  change = 0.0                          # class-level variable to store calculated change # the value of 0.0 will get overridden by instance values via methods in the constructor

# Sets the amount of cash the customer handed over 
# Inputs: a: the amount given by the customer (expected as float or int) 
# Outputs: Sets the instance variable self.amount.given
  def set_amount_given (self, a):
      self.amount_given = a

# Calculates the change to be returned to the customer; takes the cash received (amount_given), subtracts the due amount (amount), stores the result in self.change
# Inputs: Uses self.amount_given and self.amount (from parent class)
# Outputs: stores the result in self.change
  def calc_change (self):
      self.change = self.amount_given - self.amount

# Constructor: __init__
# Initializes a cash payment object with customer name, total amount due, and amount given
# Inputs: cust_name (string) - the name of the customer; amount (float or string): total amount due; given (int or float) amount of cash customer provided
# Outputs: None (initializes object state)
  def __init__(self, cust_name, amount, given):
        self.set_customer_name(cust_name)       # Sets customer name using inherited method from base class 
        self.set_amount_due(float(amount))      # Sets total amount to pay using inherited method from base class
        self.set_amount_given(int(given))       # Sets cash given by the customer using inherited method from base class
        self.calc_change()                      # Calculates the change to return

# Prints a formatted receipt for a cash transaction: Displays a header for cash receipts, prints key transaction details: Customer name (self.customer_name), total amount (self.amount), timestamp of payment (self.timeStamp), calculated change (self.change)
# Inputs: None (it uses internal instance values)
# Outputs: A printed receipt on the console including customer name, Total amount due, time of transaction, change returned
  def print_receipt(self):
    print("\n\n\t   Cash Receipt\n")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" Name: " + self.customer_name)
    print(" Total: ₱%.2f" %(self.amount))
    print(" Time: " + self.timeStamp)
    print(" Change: ₱%.2f" %(self.change))
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n")


1. Takeaways: are there anything you can learn from the code? (How to structure your code, a clean solution for some function you might also need...)

I generally find the structure very helpful for our own project. I find it very clearly laid out, as it shows which functions the project contains and we as developers can develop our program step by step. It is also easier to debug functions if an error appears in a function.
I found the idea of the visual receipt particularly cool and would use it as an idea for our project.

1. What parts of the code were confusing or difficult at the beginning to understand?
- Were you able to understand what it is doing after your own research?

Overall, I found the code easy to understand because it was so clearly structured and we had already used many of the functions. 
I had to look up a few individual functions, such as timeStamp, to understand what this function does. I also looked up exactly what modules such as ModeofPayment provide.
