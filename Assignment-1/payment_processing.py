# Assignment 1 - Multi Gateway Payment Processing System

from abc import ABC, abstractmethod


# Parent class for all payment methods
class PaymentMethod(ABC):

    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass


# Razorpay payment methods
class RazorpayCardPayment(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def get_details(self):
        return "Razorpay Card ending with " + self.card_number[-4:]

    def pay(self, amount):
        print("Paying Rs.", amount, "using Razorpay Card")
        return True


class RazorpayUPIPayment(PaymentMethod):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def get_details(self):
        return "Razorpay UPI - " + self.upi_id

    def pay(self, amount):
        print("Paying Rs.", amount, "using Razorpay UPI")
        return True


# Stripe payment methods
class StripeCardPayment(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def get_details(self):
        return "Stripe Card ending with " + self.card_number[-4:]

    def pay(self, amount):
        print("Paying Rs.", amount, "using Stripe Card")
        return True


class StripeUPIPayment(PaymentMethod):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def get_details(self):
        return "Stripe UPI - " + self.upi_id

    def pay(self, amount):
        print("Paying Rs.", amount, "using Stripe UPI")
        return True


# Factory for creating payment objects
class FactoryPaymentMethod:
    factory = {}

    @classmethod
    def get_payment_object(cls, method_type, **kwargs):
        if method_type not in cls.factory:
            raise ValueError("Invalid payment method")
        return cls.factory[method_type](**kwargs)


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


# Common aggregator class
class Aggregator(ABC):
    def __init__(self, name, processing_fee, payment_factory):
        self.name = name
        self.processing_fee = processing_fee
        self.payment_factory = payment_factory

    def call_get_payment_object(self, method_type, amount, **kwargs):
        payment = self.payment_factory.get_payment_object(method_type, **kwargs)

        fee = amount * self.processing_fee / 100
        total_amount = amount + fee

        print("\nGateway:", self.name)
        print("Processing fee:", self.processing_fee, "%")
        print("Fee amount: Rs.", round(fee, 2))
        print("Payment details:", payment.get_details())

        return payment.pay(round(total_amount, 2))


class RazorpayAggregator(Aggregator):
    def __init__(self):
        super().__init__("Razorpay", 2.0, RazorpayFactory)


class StripeAggregator(Aggregator):
    def __init__(self):
        super().__init__("Stripe", 2.9, StripeFactory)


# Factory for selecting the payment gateway
class AggregatorFactory:
    factory = {
        "razorpay": RazorpayAggregator,
        "stripe": StripeAggregator
    }

    @classmethod
    def get_aggregator_object(cls, name):
        if name not in cls.factory:
            raise ValueError("Invalid aggregator")
        return cls.factory[name]()


def main():
    print("----- Payment Processing System -----")
    print("1. Razorpay")
    print("2. Stripe")
    gateway_choice = input("Select payment gateway: ").lower().strip()

    if gateway_choice == "1":
        gateway_name = "razorpay"
    elif gateway_choice == "2":
        gateway_name = "stripe"
    else:
        gateway_name = gateway_choice

    print("\n1. Card")
    print("2. UPI")
    method_choice = input("Select payment method: ").lower().strip()

    if method_choice == "1":
        method = "card"
        details = {"card_number": input("Enter card number: ")}
    elif method_choice == "2":
        method = "upi"
        details = {"upi_id": input("Enter UPI ID: ")}
    else:
        print("Invalid payment method")
        return

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount should be greater than zero")
            return

        aggregator = AggregatorFactory.get_aggregator_object(gateway_name)
        result = aggregator.call_get_payment_object(method, amount, **details)

        if result:
            print("Payment successful")
        else:
            print("Payment failed")

    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
