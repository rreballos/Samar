print "Ex13   introducing argv and import  LPTHW"

from sys import argv
## the following statement only tells argv how many
## arguments to expect.
#script, first, second, third  = argv
script, a,b,third =argv
## arguments MUST be placed on the commandline only
print " The script is called:",  script
print  "your first variable is: ", a
print " Your second variable is called: ", b
print "your third variable is: ", third
### variables listed on argv line must be reflected in variables used in output (here).
