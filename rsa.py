# print(ord('a'))

dict1 = {}
for x in range(32, 127):
    dict1[x] = chr(x)
   
# print(dict1) # ascii to char dict

# encryption method
def encrypt(m, e, n):
    # return int(pow(m, e)) % n
    return pow(m, e, n)


e = 607
n = 10808266644599383431228066603118530286747579294631072262965743487302034557407489744597440855362897054631211560525564682859889523542951271420472004294519221032120599826411725894327550270616997117621872990046395494778414867302457851418456328648139860447751197512109828733651330932492561461451264473078493706131030473866887552027023516715201823657577368724869985578428783296444252522879015753440438218664399026748656010954904677340480332984766152980916469012312230314447203126325474657207271001965455237767203581774783824209208788744741023347939670371402957527812472396125575084257446436322781795533871084612144547584731
encrypt_dict = {}
for x in range(32, 127):
    encrypt_dict[x] = encrypt(x, e, n)
    
# print(encrypt_dict)

f = open('cipher_initial.txt', 'r')
lines = f.readlines()
list = []
for element in lines:
    list.append(int(element.replace("\n", "")))

# print(list)


# converting to chars
msg = ""
file = open("dales_RSA_decrypted.txt", "w")
for element in list:
    for key in encrypt_dict:
        if element == encrypt_dict[key]:
            file.write(dict1[key])
            msg += dict1[key]
       
file.close()           
        
print("\n" + msg + "\n")

    
 
 
 
 
    
# gcd method for later projects
def gcd(a, b):
    if a < b:
        a, b = b, a     # swap a and b so a is larger
    while b != 0:       # loop until b is 0, then we have found gcd
        a, b = b, a % b     # a is now b and b is now a % b
    return a   

