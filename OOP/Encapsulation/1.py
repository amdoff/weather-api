class User:
    def __init__(self, name: str, card: str, amount: float, currency: str):
        self.__name = name
        self.__card = card
        self.__amount = amount
        self.__currency = currency

    def get_name(self) -> str:
        return self.__name

    def get_currency(self) -> str:
        return self.__currency

    def add_money(self, amount: float):
        self.__amount += amount

    def get_money(self, amount: float) -> bool:
        if self.__amount >= amount:
            self.__amount -= amount
            return True
        return False

    def __str__(self) -> str:
        return f"""CARD INFO:
HOLDER: {self.__name}
CARD: {self.__card}
AMOUNT: {self.__amount} {self.__currency}"""
from datetime import datetime

class Transaction:
    def __init__(self):
        self.usd_to_uzs = 0
        self.rub_to_uzs = 0
        self.status = "FAILED"
        self.timestamp = None
        self.sender = None
        self.receiver = None
        self.amount = 0
        self.currency = "UZS"

    def set_transfer_rates(self, usd_to_uzs: float, rub_to_uzs: float):
        self.usd_to_uzs = usd_to_uzs
        self.rub_to_uzs = rub_to_uzs

    def make_transaction(self, sender: User, receiver: User, amount: float):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = datetime.now()

        sender_currency = sender.get_currency()
        receiver_currency = receiver.get_currency()

        if sender_currency == "USD":
            amount_in_sender_currency = amount / self.usd_to_uzs
        elif sender_currency == "RUB":
            amount_in_sender_currency = amount / self.rub_to_uzs
        elif sender_currency == "UZS":
            amount_in_sender_currency = amount
        else:
            self.status = "FAILED"
            return

        if sender.get_money(amount_in_sender_currency):
            if receiver_currency == "USD":
                amount_in_receiver_currency = amount / self.usd_to_uzs
            elif receiver_currency == "RUB":
                amount_in_receiver_currency = amount / self.rub_to_uzs
            elif receiver_currency == "UZS":
                amount_in_receiver_currency = amount
            else:
                self.status = "FAILED"
                return

            receiver.add_money(amount_in_receiver_currency)
            self.status = "SUCCESS"
        else:
            self.status = "FAILED"

    def __str__(self) -> str:
        return f"""TRANSACTION
SENDER: {self.sender.get_name()} ({self.sender.get_currency()})
RECEIVER: {self.receiver.get_name()} ({self.receiver.get_currency()})
AMOUNT: {self.amount} {self.currency}. TRANSFER TIMESTAMP: {self.timestamp}
STATUS: {self.status}"""
