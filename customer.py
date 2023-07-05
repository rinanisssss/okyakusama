class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return self.first_name + " " + self.family_name  # memorizing the names

    def entry_fee(self):
        if self.age < 20:
            return print(1000)
        elif 20 <= self.age < 65:
            return print(1500)
        else:
            return print(1200)


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.entry_fee()
tom = Customer(first_name="Tom", family_name="Ford", age=57)
tom.entry_fee()
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.entry_fee()


# # ken = Customer(first_name="Ken", family_name="Tanaka")
# print(ken.full_name())  # "Ken Tanaka" という値を返す
# tom = Customer(first_name="Tom", family_name="Ford")
# print(tom.full_name())  # "Tom Ford" という値を返す


# ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
# print(ken.age)  # 15 という値を返す

# tom = Customer(first_name="Tom", family_name="Ford", age=57)
# print(tom.age)  # 57 という値を返す

# ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
# print(ieyasu.age)  # 73 という値を返す


# ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
# ken.entry_fee()  # 1000 という値を返す

# tom = Customer(first_name="Tom", family_name="Ford", age= 57)
# tom.entry_fee() # 1500 という値を返す

# ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
# ieyasu.entry_fee() # 1200 という値を返す
