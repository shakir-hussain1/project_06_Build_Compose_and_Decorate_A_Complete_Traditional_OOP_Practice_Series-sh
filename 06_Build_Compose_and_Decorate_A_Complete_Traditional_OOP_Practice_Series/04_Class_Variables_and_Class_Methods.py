class Bank:
    bank_name = "Habib Bank"  # Class variable

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Bank Name: {Bank.bank_name}")

# Create instances
acc1 = Bank("Shakir")
acc2 = Bank("Naveed")

# Display initial bank name
acc1.display()
acc2.display()

print("\nChanging bank name...\n")
Bank.change_bank_name("National Bank")

# Display after changing bank name
acc1.display()
acc2.display()
