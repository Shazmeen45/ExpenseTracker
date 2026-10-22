
import json
from pathlib import Path
from expense import Expense


DATA_DIR = Path(__file__).parent / "data"
DATA_FILE = DATA_DIR / "expenses.json"


def load_expenses():
    DATA_DIR.mkdir(exist_ok=True)

    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            records = json.load(file)

        if not isinstance(records, list):
            raise ValueError("Expense data must be a list.")

        return [Expense.from_dict(item) for item in records]

    except (json.JSONDecodeError, ValueError, KeyError, TypeError) as error:
        print(f"Could not load expense data: {error}")
        return []


def save_expenses(expenses):
    DATA_DIR.mkdir(exist_ok=True)

    records = [expense.to_dict() for expense in expenses]

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)
