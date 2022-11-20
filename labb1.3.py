n = int(input("  Enter max value : "))
f = input("  Enter O/E/B (Odd or Even or Both) : ")
o = input("  Enter Y/N (onlyprime?) : ")

def prime_number(onlyprime,formats,number):
    
  if onlyprime == "Y":
      
    if formats == "B" and number != 0:
        value = number % 6
        if value == 1 or value == 5:
          print(f"   {number} is prime number")
        elif number == 2 or number == 3:
          print(f"   {number} is prime number")
        return prime_number(onlyprime,formats,number-1)
        
    if formats == "O" and number != 0:
        value = number % 2
        if value != 0:
          print("  Please enter Odd number")
          return
        if number == 2 :
          print(f"   {number} is prime number")
          return
        return prime_number(onlyprime,formats,number-2)
        
    if formats == "E" and number >= 0:
          value = number % 6
          if number % 2 == 0:
            print("  Please enter Even number")
            return
          if value == 1 or value == 5:
            print(f"   {number} is prime number")
          elif number == 3:
            print(f"   {number} is prime number")
          return prime_number(onlyprime,formats,number-2)
    else:
      return
  
  else:
      
    if formats == "B" and number != 0:
      value = number % 6
      if value == 1 or value == 5:
        print(f"   {number} is prime number")
      elif number == 2 or number == 3:
        print(f"   {number} is prime number")
      else:
        print(f"   {number} is not prime number")
      return prime_number(onlyprime,formats,number-1)
      
    if formats == "O" and number != 0:
      value = number % 2
      if value != 0:
        print("  Please enter Odd number")
        return
      if number == 2 :
        print(f"   {number} is prime number")
        return
      else:
        print(f"   {number} is not prime number")
      return prime_number(onlyprime,formats,number-2)
      
    if formats == "E" and number >= 0:
        value = number % 6
        if number % 2 == 0:
          print("  Please enter Even number")
          return
        if value == 1 or value == 5:
          print(f"   {number} is prime number")
        elif number == 3:
          print(f"   {number} is prime number")
        else:
          print(f"   {number} is not prime number")
        return prime_number(onlyprime,formats,number-2)
    else:
        return
        
prime_number(o,f,n)


