"""One expense. Something you spent money on."""
from datetime import date


class Expense:
    """Keeps the four things we know about an expense."""

    def __init__(self, expense_date: date, category: str,
                 description: str, amount: float) -> None:
        """Save the four values on this expense."""
        self.expense_date = expense_date
        self.category = category
        self.description = description
        self.amount = amount

    def __str__(self) -> str:
        """Make one line of text to print."""
        return (f'{self.expense_date}  {self.category:12}  '
                f'{self.description:25}  ${self.amount:9.2f}')