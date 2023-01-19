# BIP-39-Simple-Words-Generator
This software is useful to create mnemonic words that follow the BIP-39 standard.
The code is as short as possible. Using as few libraries as possible. 
To make sure the user does not have to trust anyone that the words produced are really private. 
The only library it uses is the SHA256 function inside the haslib library.
At the moment there are 2 codes. One, called lets_roll_another.py to create the words starting from some 8 sided dice. 
And another, famous_last_words.py, will tell you the last word, if you have the others. 
This is important as you cannot just create 12 or 24 random words. As the last one is a checksum of the first ones.

The usual warnings apply.
-Run it while you are not connected to the internet.
-Run an antivirus before running this software.
-And with your computer operating system up to date.
-Don't store the words on the computer (or worse on the cloud, or tablet, or anything else that can be hacked).
-Store them instead on a physical device.

The best would be to simply use the dices and no computer,
but unfortunately because the last word is a checksum of the first ones this is not a viable solution
