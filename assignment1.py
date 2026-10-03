from abc import ABC , abstractmethod
class paymentmethod(ABC):
        @abstractmethod
        def get_details(self) -> str:
            pass

        @abstractmethod
        def pay(self, amount:float) -> bool:
            pass  


class RazorpayCardPayment(paymentmethod):
    def __init__(self, card_number):
        self.card_number = card_number
    def get_details(self):
        return f"Razor card: {self.card_number}"
    def pay(self, amount):
        print(f"Razorpay card payment : {amount}$")
        return 1


class StripeCardPayment(paymentmethod):
    def __init__(self, card_number):
        self.card_number = card_number
    def get_details(self):
        return f"Stripe card: {self.card_number}"
    def pay(self, amount):
        print(f"Stripe card payment : {amount}$")
        return 1

class RazorpayUPIPayement(paymentmethod):
    def __init__(self, upi):
        self.upi = upi
    def get_details(self):
        return f"upi id : {self.upi}"
    def pay(self,amount):
        print(f"razorpay upi payment : {amount}$")
        return 1

class StripeUPIPayement(paymentmethod):
    def __init__(self, upi):
        self.upi = upi
    def get_details(self):
        return f"upi id : {self.upi}"
    def pay(self,amount):
        print(f"stripe upi payment : {amount}$")
        return 1



class FactoryPaymentMethod():
    factory{}
    @classmethod 
    def get_payment_object(cls, method_type: str, **kwargs) -> paymentmethod:

        class RazorpayFactory(FactoryPaymentMethod):
            factory = {
                "card": RazorpayCardPayment,
                "upi": RazorpayUPIPayment
            }
        class StripeFactory(FactoryPaymentMethod):
            factory = {
                "card": StripeCardPayment,
                "upi": StripeUPIPayment
            }


class Aggregator(ABC):
    @abstractmethod
    def  call_get_payment_object(self, method_type: str, amount: float, **kwargs) -> bool:
        pass

class RazorpayAggregator(Aggregator):
    processing = 2/100
    def  call_get_payment_object(self, method_type: str, amount: float, **kwargs):
        payment = RazorpayFactory.get_payement_object(
            method_type, **kwargs
        )
        final = amount + amount*processing
        return payment.pay()

class StripeAggregator(Aggregator):
    processing = 2.9
    def  call_get_payment_object(self, method_type: str, amount: float, **kwargs):
        payment = StripeFactory.get_payement_object(
            method_type, **kwargs
        )
        final = amount + amount*processing
        return payment.pay()

class AggregatorFactory:
    factory = {
        "stripe" : StripeAggregator
        "razorpay" : RazorpayAggregator
    }
    @classmethod
    def get_aggregator_object(cls, aggregator_name: str):
        
