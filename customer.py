import file_handler as fh

a= fh.FileHandler("users.csv")
users =a.read_file()
b = fh.FileHandler("kalas.csv")
kalas = b.read_file()
c= fh.FileHandler("block.csv")
blocked = c.read_file()
d= fh.FileHandler("list.csv")
list_shop=d.read_file()
def customer_menu():
        print("""__________
1.List of all kala
2.List of all shopping malls
3.Search for a mall
4.Select a mall
5.last shops
6.exit""")



