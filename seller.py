import file_handler as fh


a= fh.FileHandler("users.csv")
users =a.read_file()
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

