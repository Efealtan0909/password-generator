import random , json

CL = [
    'a','b','c','d','e','f','g','h','i','I','j','k','l','m','n','o','p','r','s','t','u','v','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','Y','Z',
    '+','-',',',':','<','>','{','}','[',']','*','_','?','#','$'
]

NL = [
    '0','1','2','3','4','5','6','7','8','9'
]

charsI = input('How much Characters you Want ?\n\nCharacters>')
numberPassI = input('\nHow much Passwords you Want ?\n\nPasswords>')
DisplayI = input('\n(1) Save in File\n(2) Print in Terminal\nSelect How you Want to display the Passwords\n\nSelection>')

CODE = ""
if DisplayI == '1':
    FileName = input('\nEnter Name of File you Want to Save on\n\nFileName>')
    CODE = ""
    for f in range(int(numberPassI)):
        while(True):
            newPassword=""
            for i in range(int(charsI)):
                isNumber = random.randrange(0,2)
                if isNumber == 1:
                    newPassword = newPassword + random.choice(NL)
                else:
                    newPassword = newPassword + random.choice(CL)
            if newPassword not in CODE:
                CODE = CODE + "\n" + newPassword
                break
    passwordsfile = open(FileName,'a')
    passwordsfile.write(CODE + "\n")
else:
    if DisplayI == '2':
        CODE = ""
        for f in range(int(numberPassI)):
            while(True):
                newPassword=""
                for i in range(int(charsI)):
                    isNumber = random.randrange(0,2)
                    if isNumber == 1:
                        newPassword = newPassword + random.choice(NL)
                    else:
                        newPassword = newPassword + random.choice(CL)
                if newPassword not in CODE:
                    CODE = CODE + "\n" + newPassword
                    break
        print(CODE)
    else:
        print('Error')
    



