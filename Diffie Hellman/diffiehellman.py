# the computers with these dont know the other ones key
key1 = 688754328678529
key2 = 93375743874823942

#we agreed on these
base = 303781
mod = 650519


computer1key = pow(base, key1, mod)
computer2key = pow(base, key2, mod)

# pretend to send the new keys to other computer


# combine the received key with the owned key
computer1final = pow(computer2key, key1, mod)
computer2final = pow(computer1key, key2, mod)

# proof they are the same
print(computer1final)
print(computer2final)