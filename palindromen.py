def main():
 q=int(input(""))
 temp=q
 rev=0
 while(q>0):
    dig=q%10
    rev=rev*10+dig
    q=q//10
 if(temp==rev):
    print("yes")
 else:
    print("no")

if __name__ == '__main__':
    main()
