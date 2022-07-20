import re
import ipaddress
# Make a regular expression for validating an Ip-address
regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
# Define a function for validating an Ip address
def check(Ip):
  list=[]
  # pass the regular expression and the string in search() method
  #if it is a valid Ip address then convert it into other formats and save them in a list
  if(re.search(regex, Ip)):
    Ip=Ip.split('.')
    iphex=' '.join((hex(int(i))[2:] for i in Ip))
    ipbin='{:0>8}'.format(str(bin(i))[2:])
    ipoct='.'.join(format(int(x), '04o') for x in Ip.split('.'))
    list.append(Ip)
    list.append(ipbin)
    list.append(iphex)
    list.append(ipoct)
  else:
    pass
output=[]
numberdictionary = {1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth", 6: "sixth",
                    7: "seventh", 8: "eighth", 9: "ninth", 10: "tenth"}
a = []
for element in range(1, 11):
  a.append(input())      
#Saving convert IP Adresses in a new file
for ip in a:
  check(ip)
with open("conversions.txt", "w") as f:
  for s in list:
    f.write(str(s) +"\t")
#Reading converted IP Adresses from the file and printing them
fread = open("conversion.txt", "r")
for p in range(0, 10):
  if clist[p] == 1:
    print(f"The {numberdictionary[p+1]} IP address in Decimal, Binary,"f" Octal and hexadecimal format is {fread.readline()}")
  else:
   print(f"The {numberdictionary[p+1]} IP address is invalid IPv4 address\n")
fread.readline()
fread.close()
    
