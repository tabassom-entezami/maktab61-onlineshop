import file_handler as fh

a = fh.FileHandler("users.csv")
kalas = fh.FileHandler("kalas.csv")


class Customer:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        a.add_to_file({"username": username, "password": password, "check": True})


class Boss:
    def __init__(self, username, password, store_name, time_open, time_close):
        self.username = username
        self.password = password
        self.store_name = store_name
        self.time_open = time_open
        self.time_close = time_close
        a.add_to_file({"username": username, "password": password, "check": True, "store_name": store_name,
                       "time_open": time_open,
                       "time_close": time_close})


class Kala:
    def __init__(self, name_of_seller, name_of_shop, name, number, *args):
        kalas.add_to_file(
            {"name_of_seller": name_of_seller, "name_of_shop": name_of_shop, "name": name, "number": number,
             "other_things": args})

    # def __call__(self):
    #     for i in range(len(self.keys)):
    #         print(f"""{self.keys[i]} is {self.values[i]}""")


