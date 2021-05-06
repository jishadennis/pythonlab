def addprefix(s):
    if len(s)<3:
        return s
    else:
        if s[-3:]!='ing':
            return s+'ing'
        else:
            return s+'ly'
s=input("Enter a string:")
s1=addprefix(s)
print("After adding suitable prefix:",s1)
