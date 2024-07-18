#Balance Check Task

def balance_check(balance: float, withdrawal_amount: float) -> tuple:
  if balance >= withdrawal_amount:
      balance -= withdrawal_amount
      return balance, 'Withdrawal successful!'
  else:
      return balance, 'Insufficient funds.'

def main():
  try:
      balance = float(input("Enter your account balance: "))
      withdrawal_amount = float(input("Enter the amount you want to withdraw: "))

      result = balance_check(balance, withdrawal_amount)
      print(result)

  except ValueError:
      print("Invalid input. Please enter numeric values for balance and withdrawal amount.")

if __name__ == "__main__":
  main()

#Interest Calculation Task

def calculate_interest(principal: float, rate: float, time: float) -> float:
    return (principal * rate * time) / 100

# This line of code Prompt the user for the inputs
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (as a percentage): "))
time = float(input("Enter the time period in years: "))

# This code Calculate the interest
interest = calculate_interest(principal, rate, time)

# This will Print the result
print(f"The calculated interest is: {interest}")


#Loan Eligibility Task

def check_loan_eligibility(age: int, income: float, credit_score: int) -> str:
    if 21 <= age <= 65 and income >= 30000 and credit_score >= 700:
        return "Eligible for a loan."
    else:
        return "Not eligible for a loan."

def main():
    try:
        age = int(input("Enter your age: "))
        income = float(input("Enter your annual income: "))
        credit_score = int(input("Enter your credit score: "))

        result = check_loan_eligibility(age, income, credit_score)
        print(result)
    except ValueError:
        print("Invalid input. Please enter numeric values for age, income, and credit score.")

if __name__ == "__main__":
    main()


#Transaction History Filter Task

def filter_transactions(transactions: list, threshold: float) -> list:
    """
    Filters transactions above the given threshold.

    Parameters:
        transactions (list): A list of transaction amounts.
        threshold (float): The threshold amount.

    Returns:
        list: A list of transactions that are above the threshold amount.
    """
    return [transaction for transaction in transactions if transaction > threshold]

def main():
    transactions = [250.0, 500.0, 75.0, 1000.0, 150.0]  # Sample transactions
    threshold = float(input("Enter the threshold amount: "))

    filtered_transactions = filter_transactions(transactions, threshold)
    print(f"Transactions above the threshold of {threshold}: {filtered_transactions}")

if __name__ == "__main__":
    main()

# Calculate Total Expense Task

def calculate_total_expense(rent: float, groceries: float, utilities: float, entertainment: float) -> float:
    return rent + groceries + utilities + entertainment

def main():
    try:
        rent = float(input("Enter the monthly rent expense: "))
        groceries = float(input("Enter the monthly groceries expense: "))
        utilities = float(input("Enter the monthly utilities expense: "))
        entertainment = float(input("Enter the monthly entertainment expense: "))

        total_expense = calculate_total_expense(rent, groceries, utilities, entertainment)
        print(f"The total monthly expense is: {total_expense:.2f}")
    except ValueError:
        print("Please enter a valid number for each expense.")

if __name__ == "__main__":
    main()
