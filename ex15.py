print "ex15.py  Reading Files LPTHW"
from sys import argv
script, filename = argv
  ## gets the filename to be opened from the command line via argv
  ## and stores it in variable 'txt'
txt = open(filename)
  ## tells python to read the file specified above 
  ## filename handle.command  ( what to do with the filehandle)
print "   Here's your file %r:" %filename
print txt.read()
print txt.close()
## the following lines do about same as above but from within
## the program rather than getting the filename from
## commandline/argv and into a different file handle
print "   Type the filename again:"
file_again = raw_input(">")
txt_again = open(file_again)
print txt_again.read()
print txt_again.close()