#Payment System (Runtime Polymorphism)#
class Payment:
    def process_payment(self):
        print("Processing payment")

class CreditCard(Payment):
    def process_payment(self):
        print("Payment by Credit Card")

class UPI(Payment):
    def process_payment(self):
        print("Payment by UPI")

class NetBanking(Payment):
    def process_payment(self):
        print("Payment by NetBanking")

p1 = CreditCard()
p2 = UPI()
p3 = NetBanking()

p1.process_payment()
p2.process_payment()
p3.process_payment()