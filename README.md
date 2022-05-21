# natas15-walkthrough
My process of solving the hacking challenge natas15 -> natas16.

This level's password: `AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J`

For this level, we're dealing with an SQL database that allows us to search for a user by name, and the only output we get is

1. "This user exists."
2. "This user doesn't exist."
3. "Error in query."

The query string's PHP appears as such: `"SELECT * from users where username=\"".$_REQUEST["username"]."\"";`, meaning we have full control after the username. For instance, `" OR 1=1;#` gives output #1.

For my solution, I realised that the password was likely stored as plaintext in the database, so we could brute-force it letter by letter by using SQL's substring() function; SELECT substring(password, n, 1) = character; solves our problem for that. And seems to work. However, it is not case-sensitive, which I struggled with for a while. Fortunately, converting characters to binary and comparing those fixed the issue. Here's the curl for an individual character:

`curl -u natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J -X POST --data-urlencode "username=natas16\" AND (SELECT cast(substring(password, 1, 1) as binary) = cast('W' as binary));#" http://natas15.natas.labs.overthewire.org/`

Of course, you wouldn't do this by hand, so I wrote a handy little python program to do this for me, which worked out nicely. One of the biggest difficulties was dealing with excessive escape characters that would get escaped first in python and then again after posting through curl.


![](https://i.imgur.com/1p7kE73.png))
