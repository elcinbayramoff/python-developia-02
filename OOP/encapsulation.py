# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
    

# bank1 = BankAccount(100)
# print(bank1.balance)
# bank1.balance = 10
# print(bank1.balance)

#1. Public - Hər kəsə açıq
#2. Protected - Qorunmuş
#3. Private - Gizli

# class Person:
#     def __init__(self, name, age, fin_code):
#         self.name = name # public
#         self._age = age # protected
#         self.__fin_code = fin_code # private

# person1 = Person('Ali',20,1234567)

# print(person1.name)
# print(person1._age)
# print(person1.__fin_code) Olmaz
#name-mangling
# print(person1._Person__fin_code) # Mümkündür


# class Person:
#     def __init__(self, name, age, fin_code):
#         self.name = name # public
#         self._age = age # protected
#         self.__fin_code = fin_code # private
    
#     def change_fin(self, new_fin):
#         self.__fin_code = new_fin 
#         """
#         Class daxilində private atributlara keçid edərkən o compile olanda avtomatik olaraq
#         _ClassName__atributName -ə çevrilir və buna görə də işləyə bilir.
#         """

# person1 = Person('Ali',20,1234567)
# person1.change_fin(11111111)

# print(person1._Person__fin_code)


#getter, setter

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance

#     #getter
#     def get_balance(self):
#         return self.__balance
    
#     #setter
#     def set_balance(self, amount):
#         if amount < 0:
#             raise ValueError('Amount should be >= 0')
#         self.__balance = amount

# acc1 = BankAccount(100)
# # print(acc1.__balance) #olmaz
# print(acc1.get_balance())

# acc1.set_balance(-5)
# print(acc1.get_balance())

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance

#     @property
#     def balance(self):
#         return self.__balance
    
#     @balance.setter
#     def balance(self, amount):
#         if amount < 0:
#             raise ValueError('Amount should be >= 0')
#         self.__balance = amount


# acc1 = BankAccount(100)
# print(acc1.balance)
# acc1.balance = 1000
# print(acc1.balance)


# class Stage:

#     @property
#     def candidate_count(self):
#         return 100
    
# stage1 = Stage()

# print(stage1.candidate_count) 