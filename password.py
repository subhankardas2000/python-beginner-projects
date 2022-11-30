import random

pas=['a','b','c','d','e','f','g',
    'h','i', 'j','k', 'l','m','n',
    'o','p', 'q','r','s','t','u',
    'v','w', 'x', 'y','z','A','B',
    'C','D','E','F','G','H','I',
    'J','K','L','M','N','0','P',
    'Q','R','S','T','U','V','W',
    'X','Y', 'Z', '1','2','3', '4',
    '5','6','7','8','9','0','&',
    '!','@','#','$','%','_']

password=""
for i in range(8):
    password=password+random.choices(pas)[0]
    
print("Your password : ",password)