import random , json

CL = [
    'a','b','c','d','e','f','g','h','i','I','j','k','l','m','n','o','p','r','s','t','u','v','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','Y','Z',
    '+','-',',',':','<','>','{','}','[',']','*','_','?','#','$'
]

NL = [
    '0','1','2','3','4','5','6','7','8','9'
]
CODE = ""
for f in range(300000):
    while(True):
        newPassword=""
        for i in range(16):
            isNumber = random.randrange(0,2)
            if isNumber == 1:
                newPassword = newPassword + random.choice(NL)
            else:
                newPassword = newPassword + random.choice(CL)
        if newPassword not in CODE:
            CODE = CODE + "\n" + newPassword
            break;

        #with open('list.json') as f:
    #    List = json.load(f)
    #    for password in List['used']:
    #        if CODE != List['used']:
    #         print(CODE)
    #    
    #    
    #with open('list.json' , 'a') as f:
    #    json.dump(List,f,indent=4)
passwordsfile = open('password.txt','a')
passwordsfile.write(CODE + "\n")
