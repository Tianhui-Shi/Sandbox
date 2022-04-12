"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    month_number = int(input("How many months? "))

    for month in range(1, month_number + 1):
        income = float(input("Enter income for month {} : ".format(month)))
        incomes.append(income)

    report(incomes)

# this function will print the report of income
def report(income):
    print("\nIncome Report\n-------------")

    total = float(sum(income))
    for month,income in enumerate (income):
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month+1, income, total))

main()
