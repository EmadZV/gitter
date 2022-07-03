def userinput1checker(string1) : # 1 این تابع برای چک کردن وجود کاربر در دیتابیس ماست
    # opening a text file
    file1 = open ("hamechi.txt")
    # setting flag and index to 0
    flag = 0
    index = 0
    # Loop through the file line by line
    for line in file1:  
        index += 1   
    # checking string is present in line or not
        if string1 in line:
            flag = 1
            break 
        # checking condition for string found or not
    if flag == 0: 
        print('String', string1 , 'Not Found') 
        print ("You should sign in first !")
        signin_want()
        #in ye loop dorost mikone ba 3 func
        return False
    else: 
        print('String', string1, 'Found In Line', index)
        print ("Welcome back" , string1)
        continuer()
        return True
    # closing text file 
    file1.close()   


def signer() : # در صورت تمایل کاربر با این تابع ثبت نام میکند 4
    file1 = open ("hamechi.txt" , "a")
    
    user = input("Enter your first name : last name : password ").split(":")
    for i in user :
        i = i.strip
        file1.write(i+" ")
        print ("congrats ! you signed up successfully ! ")
    file1.write("\n")
    continuer


def Truechecker (TRUEORFALSE) : # این تابع ورودی مثبت را میسنجد و آن را تبدیل به بولین میکند 3
    if TRUEORFALSE.upper() == "YES" or "Y" :
        return True
    else : 
        return False


def signin_want() : # این تابع از نتیجه منفی تابع 1* استفاده میکند و تمایل کاربر به ثبت نام را میسنجد 2
    choice = input ("Do you want to sign in now ? (YES/NO) " )
    if Truechecker(choice) == True :
        return signer()
        #age bekhad sign in kone be signer mire ke komakesh kone
        #sign in kone
    else : 
        close()
        # اگه نخواد ثبت نام کنه باید بسته بشه


def continuer( ) : 
    global quizlist
    quizlist = ["iqtest" , "etest"]
    print ("********************")
    for i in quizlist :
        print (i)
    choice = input ('good day to you sir/madame. which quiz do you want to attend in ?' )
    if choice.lower == "iqtest" :
        pass
    elif choice.lower == "etest" :
        pass


def iqquiz() :
    pass


def etest() : 
    pass


continuer()
