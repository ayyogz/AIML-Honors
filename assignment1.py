
from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    @abstractmethod
    def get_details(self) -> str:
        pass

    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass


class RazorpayCardPayment(PaymentMethod):

    def __init__(self, card_number):
        self.card_number = card_number

    def get_details(self):
        return f"Razor card: {self.card_number}"

    def pay(self, amount):
        print(f"Razorpay card payment: {amount}$")
        return True


class StripeCardPayment(PaymentMethod):

    def __init__(self, card_number):
        self.card_number = card_number

    def get_details(self):
        return f"Stripe card: {self.card_number}"

    def pay(self, amount):
        print(f"Stripe card payment: {amount}$")
        return True


class RazorpayUPIPayment(PaymentMethod):

    def __init__(self, upi):
        self.upi = upi

    def get_details(self):
        return f"UPI ID: {self.upi}"

    def pay(self, amount):
        print(f"Razorpay UPI payment: {amount}$")
        return True


class StripeUPIPayment(PaymentMethod):

    def __init__(self, upi):
        self.upi = upi

    def get_details(self):
        return f"UPI ID: {self.upi}"

    def pay(self, amount):
        print(f"Stripe UPI payment: {amount}$")
        return True


class FactoryPaymentMethod:

    @classmethod
    def get_payment_object(cls, method_type, aggregator_name, **kwargs):

        factories = {
            "razorpay": {
                "card": RazorpayCardPayment,
                "upi": RazorpayUPIPayment
            },
            "stripe": {
                "card": StripeCardPayment,
                "upi": StripeUPIPayment
            }
        }

        if aggregator_name not in factories:
            raise ValueError("Invalid aggregator")

        payment_class = factories[aggregator_name].get(method_type)

        if payment_class is None:
            raise ValueError("Invalid payment method")

        return payment_class(**kwargs)


class Aggregator(ABC):

    @abstractmethod
    def call_get_payment_object(self, method_type, amount, **kwargs) -> bool:
        pass


class RazorpayAggregator(Aggregator):

    processing = 2 / 100

    def call_get_payment_object(self, method_type, amount, **kwargs):

        payment = FactoryPaymentMethod.get_payment_object(
            method_type, "razorpay", **kwargs
        )

        final_amount = amount + (amount * self.processing)

        return payment.pay(final_amount)


class StripeAggregator(Aggregator):

    processing = 2.9 / 100

    def call_get_payment_object(self, method_type, amount, **kwargs):

        payment = FactoryPaymentMethod.get_payment_object(
            method_type, "stripe", **kwargs
        )

        final_amount = amount + (amount * self.processing)

        return payment.pay(final_amount)


class AggregatorFactory:

    factory = {
        "stripe": StripeAggregator,
        "razorpay": RazorpayAggregator
    }

    @classmethod
    def get_aggregator_object(cls, aggregator_name):

        if aggregator_name not in cls.factory:
            raise ValueError("Invalid aggregator name")

        return cls.factory[aggregator_name]()


def main():

    try:
        aggregator_name = input(
            "Enter aggregator name (razorpay or stripe): "
        ).lower()

        method_type = input(
            "Enter payment method (card/upi): "
        ).lower()

        amount = float(input("Enter amount: "))

        aggregator = AggregatorFactory.get_aggregator_object(
            aggregator_name
        )

        if method_type == "card":

            card_number = input("Enter card number: ")

            payment = aggregator.call_get_payment_object(
                method_type, amount, card_number=card_number
            )

        elif method_type == "upi":

            upi_id = input("Enter UPI ID: ")

            payment = aggregator.call_get_payment_object(
                method_type, amount, upi=upi_id
            )

        else:
            print("Invalid payment option")
            return

        if payment:
            print("Payment successful")
        else:
            print("Try again")

    except ValueError as e:
        print("Error in user values:", e)

    except Exception as e:
        print("Server error:", e)


if __name__ == "__main__":
    main()
