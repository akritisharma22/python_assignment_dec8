pw="PASSWORD"

def check(pw1):

    if pw==pw1 :
        print ("Password match")

    else:
        print("wrong password")


pw1 = input('enter password:')
check(pw1)