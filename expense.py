
from datetime import datetime


class Expense:
    def __init__(self, amount, category, date, description):
        self.__amount = amount
        self.__category = category
        self.__date = date
        self.__description = description

    @property
    def amount(self):
        return self.__amount

    @property
    def category(self):
        return self.__category

    @property
    def date(self):
        return self.__date

    @property
    def description(self):
        return self.__description

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["amount"],
            data["category"],
            data["date"],
            data["description"]
        )

    def display(self):
        print(f"Amount: Rs. {self.amount:.2f}")
        print(f"Category: {self.category}")
        print(f"Date: {self.date}")
        print(f"Description: {self.description}")
