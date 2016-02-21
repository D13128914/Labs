#
# Break a .docx password using dictionary (D13128914)
# Program takes a dictionary and protected .docx file as inputs
#


import win32com.client as win32

# Takes file, iterates through possible passwords and returns either password or Not Found message
def breakIt(file):
   for guess in passwords:
      try:
         doc = word.Documents.Open(file, False, True, None, guess)
         doc.Close()
         return str(guess)
      except Exception as error:
         pass
   return "Not found this time. Try a different wordlist."

# User enters a dictionary for the attack, lines are read and whitespace removed
wordlist = input("Enter a wordlist file: ")
wordlistfile = open(wordlist, 'r')
passwords =[line.rstrip() for line in open(wordlist)]
wordlistfile.close()

# User enters name of file they wish to open, 
locked = input("Enter protected file to open: ")
word = win32.Dispatch("Word.Application")

# Call the breakIt function on the protected file
answer = breakIt(locked)

# Displays password or "Not found" message
print("The password is: ", answer)




