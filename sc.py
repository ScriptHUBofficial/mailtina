import email
import random
import string
import time
import os
output = []
randomLeghnt = 5




def get_random_string(length):
    
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def prefixgen(exportAmount, Email):
    for i in range(exportAmount):
        ranID = get_random_string(5)
        Emailcore = Email.replace("@gmail.com", "")
        final = "{}+{}@gmail.com".format(Emailcore, ranID)
        output.append(final)
    print(output)
    input("Devam etmek için Enter'a basın...")
    mainmenu()

def exportprefix(exportdir):
    try:
        Directory = r'{}\blog.scriptbullet.txt'.format(exportdir)
        print("file location: " + Directory)
        with open(Directory, 'w') as fp:
            for item in output:
                fp.write("%s\n" % item)
            
            print('\033[32m' + "sonek seçilen dizine aktarılır" + '\033[0m')
            input("Devam etmek için Enter'a basın...")
            mainmenu()
    except:
        print('\033[31m' + "Dizin bulunamadı veya oluşturulmuş bir sonek bulunamadı" + '\033[0m')
        input("Devam etmek için Enter'a basın...")
        mainmenu()




def mainmenu():
    os.system('cls')
    print('\033[35m' + """  



███╗   ██╗██╗ ██████╗ ██████╗ ████████╗██╗███╗   ██╗ █████╗ 
████╗  ██║██║██╔════╝██╔═══██╗╚══██╔══╝██║████╗  ██║██╔══██╗
██╔██╗ ██║██║██║     ██║   ██║   ██║   ██║██╔██╗ ██║███████║
██║╚██╗██║██║██║     ██║   ██║   ██║   ██║██║╚██╗██║██╔══██║
██║ ╚████║██║╚██████╗╚██████╔╝   ██║   ██║██║ ╚████║██║  ██║

                                                                                                                     

https://blog.scriptbullet.com.tr                                                                                   

""" + '\033[0m')
    print('\033[35m' + """ 

                           
     
    [1] son ek oluştur   [2] ihracat son eki
    [3] programı kapat                                                                                                 

""" + '\033[0m')
    answer = input()
    if answer == "1" :
        email
        genAmount = int(input("Kaç tane son ek oluşturmak istiyorsunuz?         "))
        emailinput = input("kullanmak istediğin gmail hesabını ver                        ")
        prefixgen(genAmount, emailinput)
        

    elif answer == "2":
        exportpath = input("Dosyayı nereye kaydetmek istiyorsunuz? ")
        exportprefix(exportpath)


    elif answer == "3":
        print("")
    else:
        print('\033[31m' + "Bu geçerli bir cevap değil" + '\033[0m')

mainmenu()



            

