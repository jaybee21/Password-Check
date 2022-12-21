# PasswordChecker
If the security of your account is truly important to you, you should find out if your password has ever been compromised, and if you want to do this You're probably going to use one of the websites or apps, and I should warn you that doing so puts you at risk of being hacked in some way, because the password you entered on this website was actually taken and stored in a sizable database somewhere in the world, and you have no idea what will happen to it from there.

+ To address this issue I'll create a program that examines the password and determines whether it has ever been compromised and how many times, By retrieving some information from a database that is specifically designed to keep track of these instances and completing the entire process on your device without your password leaving your computer, In this instance, you can be certain that it has never been hacked and that you are totally secure. <br> No platform or person in the world is aware of your password.

## Program logic is as follows:
=> create a function that sends a request to the destination website and returns data. <br>
=> Convert our password to sha1 using hashlib library. <br>
=> Search for all compromised passwords that began with the same five characters or numbers as ours hash started with {k-anonymity}. <br>
=> We now compare the remaining hash of our password with the hash that we obtained after having a list of all the passwords that were converted to sha1 and began with the same beginning as ours. <br>
=> It will now display our password in sha1 hash format along with the number of hacks that it has experienced. <br>

## Installation
-> Download the files <br>
-> Run the Python file from the terminal by typing its name first, then the passwords you want to check (you can enter as many passwords as you want and the program will check for them all at once).
![image](https://user-images.githubusercontent.com/76536316/208256922-5369cf34-8a72-42a5-9636-630e6ecbe4ed.png)

## Employed libraries
<ul> 
  <li>requests</li>
  <li>sys</li>
  <li>hashlib</li>
</ul>
## JSolutions
