def add(num1,num2):
   # print("Result of addition : ",num1+num2+5)
   return num1+num2+5
def prntstr(str):
    return str+" This is in file1"

if __name__=='__main__':
    print(prntstr("This is me"))
    a=add(3,5)
    print("in file 1",a)
