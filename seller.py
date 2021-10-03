import file_handler as fh


a= fh.FileHandler("users.csv")
users =a.read_file()
b = fh.FileHandler("kalas.csv")
kalas = b.read_file()
def menu():
    print("""__________
1.Product registration
2.Inventory
3.Customers
4.Block a customer
5.Exit
___________""")


def check_customers():
    for i in users:
        if len(i) > 3  :
            print(f"{i[0]} is your customer ")
            if i[2] == False :
                print("this customer is Blocked")

def check_for_kala(number_of_seller):
        for i in range(len(kalas)):
            if kalas[0] == number_of_seller and kalas[3]< 5 :
                print(f"pls know that you have under 5 from {kalas[2]}")
#todo
