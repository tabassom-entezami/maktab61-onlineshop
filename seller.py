import file_handler as fh


a= fh.FileHandler("users.csv")
users =a.read_file()
b = fh.FileHandler("kalas.csv")
kalas = b.read_file()
c= fh.FileHandler("block.csv")
blocked = c.read_file()
def menu():
    print("""__________
1.Product registration
2.Inventory
3.Customers
4.Block a customer
5.Exit
___________""")




def check_customers(seller):
    for i in users:
        if len(i) > 3  :
            print(f"{i[0]} is your customer ")
            for j in blocked:
                if j["seler"] == seller and j["blocked"] == i[0]:
                    print("this user is blocked!")

def check_for_kala(number_of_seller):
        for i in kalas:
            if i["name_of_seller"] == number_of_seller and int(i["number"] )< 5:
                print(f"""pls know that you have less than 5 of {i["name"]}""")



