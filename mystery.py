import os

MystFile = open('mystery.txt','w')
MystFile.write('''69. It's not just a number. IT'S THE GREATEST NUMBER!

Sincerely,
The coolest teen who has ever lived''')
MystFile.close()

print('''_________________________________________________

Check your Python or root directory (ex. C:\) for "mystery.txt".


Debug/QA Notes:
1. Let me know if it doesn't show up in either spot.
   ***This code was only tested on Linux and runs just fine on there.***

2. Apologies in advance if it overwrites any other 
   "mystery.txt" files in previously mentioned directories.
_________________________________________________''')