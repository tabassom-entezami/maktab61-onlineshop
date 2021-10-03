import time
import file_handler as fh
import users
import hashlib
import seller

a = fh.FileHandler("users.csv")
a = fh.FileHandler.read_file(a)
kala = fh.FileHandler("kalas.csv")
kala = fh.FileHandler.read_file(kala)


def menu():
    print("""__________
1. sign in
2. sing up
3. exit
__________""")


def menu2():
    print("""___________
1.customer
2.Boss!
3.Back
__________""")


def validation_phone_number(number):
    if len(number) == 11 and number.isdigit():
        return True
    else:
        print("number is not correct")
        return False


while True:
    try:
        menu()
        choose = int(input(" > "))
        if choose == 1:
            act = False
            shop = False
            user_name = input("pls enter your username(number) : ")
            for i in a:
                if i["username"] == user_name and i["store_name"] != None:
                    user_pass = input("pls enter your password : ")
                    store = i["store_name"]
                    if i["password"] == hashlib.sha256(user_pass.encode()).hexdigest():
                        act = True
                        break
                    else:
                        print("your pass was wrong try to sing in again")
                        break
                elif i["username"] == user_name:
                    user_pass = input("pls enter your password : ")
                    if i["password"] == hashlib.sha256(user_pass.encode()).hexdigest():
                        shop = True
                        break
                    else:
                        print("your pass was wrong try to sing in again")
                        break
            else:
                print("we could not find your username pls try again")

            if act:
                seller.check_for_kala(user_name)
                while True:
                    t = 0
                    seller.menu()
                    ans = input(" > ")
                    if ans == "1":
                        name = input("name of product")
                        number = input("number of that")
                        print(
                            "pls enter object keys (like color) and then object values (like Red) and when you are done enter end ")
                        obj = {}

                        while True:
                            key = input(" key ")
                            if key == "end":
                                break
                            val = input(" value ")
                            obj.update({key: val})
                        print(user_name, store, obj)
                        users.Kala(user_name, store, name, number, obj)
                    elif ans == "2":
                        for i in kala:
                            if i["name_of_seller"] == user_name:
                                print(i)
                                break
                        else:
                            print("you don not have anything")
                    elif ans == "3":
                        seller.check_customers()
                    elif ans == "4":
                        blocked = input("number of bad person : ")
                        a.block_an_user(blocked)
                    elif ans == "5":
                        break
                    else:
                        print("pls enter a correct number")






        elif choose == 2:
            while True:
                menu2()
                kind = int(input(" > "))
                if kind == 1:
                    while True:
                        t = 0
                        print("enter your username(phone_number) : ", end=" ")
                        user_in = input()
                        if validation_phone_number(user_in):
                            for i in a:
                                if i["username"] == user_in:
                                    print("we already have this number")
                                    break
                            else:
                                while True:
                                    print("enter a password : ", end=" ")
                                    pass1 = input()
                                    print("confirm your password : ", end=" ")
                                    pass2 = input()
                                    if pass2 == pass1:
                                        users.Customer(user_in, hashlib.sha256(pass1.encode()).hexdigest())
                                        print("we added you")
                                        time.sleep(3)
                                        t = 1
                                        break
                                    else:
                                        print("did not mach")
                            if t:
                                break
                        else:
                            print("number is not ok!")
                            break

                elif kind == 2:
                    while True:
                        t = 0
                        print("enter your username(phone_number) : ", end=" ")
                        user_in = input()
                        if validation_phone_number(user_in):
                            for i in a:
                                if i["username"] == user_in:
                                    print("we already have this number")
                                    break
                            else:
                                while True:
                                    t1 = 0
                                    print("enter a password : ", end=" ")
                                    pass1 = input()
                                    print("confirm your password : ", end=" ")
                                    pass2 = input()
                                    if pass2 == pass1:
                                        store = input("your store name : ")
                                        while True:
                                            t2 = 0
                                            time_to_open = input("what is your open time? : (9:00) ")
                                            time_to_close = input("what is your close time? : (18:00)")
                                            h1 = [int(x) for x in time_to_close.split(':')]
                                            h = [int(x) for x in time_to_open.split(':')]
                                            if h[0] < h1[0]:
                                                users.Boss(user_in, hashlib.sha256(pass2.encode()).hexdigest(),
                                                           store, time_to_open, time_to_close)
                                                print("you are added")
                                                time.sleep(3)
                                                t1, t2, t = 1, 1, 1
                                                break
                                            else:
                                                print("the time is not correct")
                                        if t2:
                                            break
                                    else:
                                        print("did not mach")
                                        time.sleep(3)
                                        break

                                if t1:
                                    break
                            if t:
                                break
                        else:
                            print("number is not ok!")


                elif kind == 3:
                    break
                else:
                    print("pls enter a correct number")
                    time.sleep(3)
        elif choose == 3:
            print("bye bye !!!")
            break
        else:
            print("pls enter a correct number")
            time.sleep(3)
    except ValueError:
        print("pls enter a correct number  ")
        time.sleep(3)
    # except Exception:
    #     print("pls look at the menu and choose a correct number ")
    #     time.sleep(3)
    except KeyboardInterrupt:
        print("you finish the program")
