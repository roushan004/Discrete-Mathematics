#!/usr/bin/env python3
def FME(b, k, m):
  #O(log2(e))
  c = b % m
  for i in range(k):
    c = c*c % m
    
  return c
def FastModularExponentiation(b, e, m):
  
  c = 1
  #e = e % (m-1)  #implication of Fermat's Little Theorem Applicable only when m is prime 
  binary = str(bin(e))
  binary = binary[2::][::-1]
  for i in range(len(binary)):
    if int(binary[i]) == 1:
      c = (c*FME(b=b, k=i, m=m)) % m
  return c
#print(FastModularExponentiation(b=48, e=19, m=13))#Passed
#print(FastModularExponentiation(b=53, e=121455469879878796541651874168741684168614516874164516416174645156156416451546145187489778978789898945512325567898746212334789984541121233235648459859787559451541419845498498411141414141222616546541268782118732113813178671867371177117178313171317474514212152544514145154454678658747894789498748944789498489489489846545874, m=19))#Passed

if __name__ == '__main__':
    b = int(input("b:"))
    e = int(input("e:"))
    m = int(input("m:"))
    print(FastModularExponentiation(b, e, m))


