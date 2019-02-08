def main():
   
 nu = int(input())
 su = 0
 temp = nu
 while temp > 0:
   digit = temp % 10
   su += digit ** 3
   temp //= 10
 if nu == su:
   print("yes")
 else:
   print("no")

if __name__ == '__main__':
    main()
