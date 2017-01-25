

print " ex4.py LPTHW"
cars= 100
space_in_a_car =4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passenger_per_car = passengers / cars_driven


print "Ex5.py"
my_name = 'Zed A. Shaw'
my_age = 35  # not a lie
my_height = 74 #inches
my_weight = 180 #lbs
my_eyes = 'BLUE'
my_teeth =  'White'
my_hair = 'Brown'
#
print "Lets talk about %s." %my_name
print "He's %d inches tall" % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print  "He's got %s eyes and %s hair." % (my_eyes, my_hair )
print "His teeth are usually %s depending on the coffee" % my_teeth
print "if I add %d, %d, and %d I get %d" % (
      my_age, my_height, my_weight, my_age + my_height +my_weight )
# demonstrate line continuation  using indentation
print "--------------"
print "Ex6.py  kinds of people"
#
x = "There are %d kinds of people." %10
binary = "binary"
do_not = "dont"
y = "Those who know %s and those who %s" %(binary,do_not)
#
print x
print y
#
print "I Said: %r." %x
print "I also said: %s." %y
#
hilarious = False
joke_evaluation = "Isnt that joke so funny?! %r"
print joke_evaluation % hilarious
#
w = "This is the left side of..."
e = "a string with a right side."
print  w + e
print "--------------"

print "Exercise 7 More Printing"
print "Mary had a little lamb."
print "Its fleece was white as %s" % 'snow'
print "And everywhere that Mary Went."
print "." * 10    # what did that do?  printed 10 periods.
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
#
print "with comma at end"
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
print "without comma at end"
print end1 + end2 + end3 + end4 + end5 + end6
print end7 + end8 +end9 + end10 + end11 + end12

print "_" * 20
##
print "Ex8 Printing, Printing   using a print formatter"

formatter = "%r %r %r %r"
## using  %s for strings removes the single quote in  the output
print formatter %( 1, 2, 3, 4)
print formatter % ("one","two","three","four")
print formatter %( "true", "false", "false", "true")
print formatter %( formatter,formatter,formatter,formatter)
print formatter % (
    "I had this thing",
    "That you could type up right.",
    "But it didnt sing",
    "So  I said Goodnight"
)
#
print "_" * 20
    
##
print "Ex9 Printing, Printing, Printing     New formatting stuff"
print "Heres some new strange stuff, be sure to type it exactly"
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print "here are the days: ",days
print "Here are the Months: ", months
print """
There's something going on  here.
With three double-quotes.
Well be able to type as much as we like.
Even 4 lines if we want,  or 5 or 6.
"""
print "_" * 20

print "Ex10 What Was That    Using backslash  quotes and double-quotes"
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat =  "Im \\ a \\cat."
 
fat_cat = """
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass   
"""

funny_cat = '''
 funny_cat: this uses
\* only single quotes
\*on several 
lines of text and shows backslashes
'''
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print funny_cat
 
print "_ " * 20

print "\t Ex11 Asking Question 		Getting raw input from console"

print "How old are you?",
age = raw_input()
print "How Tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So you're %s years old, %s tall, and %s Heavy." %(age, height, weight)


print "_" * 20,"\n"
print
print "ex12 Prompting People		combining prompt into input "
age = raw_input("what's your age")
height = raw_input("How High")
weight = raw_input( "how heavy?")
print "So you're %s years old, %s tall, and %s Heavy." %(age, height, weight)


print "_" * 20,"\n"

print "End of Ex4 to 12    from LPTHW.pdf "
