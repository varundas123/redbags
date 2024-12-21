from datetime import date, timedelta

# Welcome Message
print("\t\tWelcome to Home Loan EMI Calculator")

# Input for loan details
principal = float(input("Principal Amount: "))
rate = float(input("Rate of Interest: "))
tenure = int(input("Tenure (in months): "))

# EMI Calculation
monthlyrate = rate / (12 * 100)
print("\nYour loan details are being calculated...\n")

# Option to see EMI details
emi_schedule = input("Enter 1 to see EMI details: ")

if emi_schedule == "1":
    print("\nDate\t\Total Disbursed\tRemaining Tenure\t\t\tEMI")
    today = date.today()  # Get today's date
    remaining_tenure = tenure
    #disbursed_amount = 375000
    total_disbursed = 375000  # Total disbursed amount
    emi = 0.0  # Initialize EMI
    emi_total = 0.0
    for month in range(1, tenure + 1):  
        # Disbursement logic (every 3 months)
        if total_disbursed == 375000:
            disbursed_amount = min(principal * 30 / 100, principal - total_disbursed)
            total_disbursed += disbursed_amount  
            emi = round(float(total_disbursed * monthlyrate * (1 + monthlyrate) ** remaining_tenure) /
                        (((1 + monthlyrate) ** remaining_tenure) - 1))                  
        elif month % 3 == 1 and total_disbursed < principal:
            disbursed_amount = min(principal * 10 / 100, principal - total_disbursed)
            total_disbursed += disbursed_amount

            # Recalculate EMI based on total disbursed
            emi = round(float(total_disbursed * monthlyrate * (1 + monthlyrate) ** remaining_tenure) /
                        (((1 + monthlyrate) ** remaining_tenure) - 1))

        emi_date = today.strftime("%d/%m/%Y")  # Format the date
        emi_total += emi
        # Print the details for the current month
        print(f"{emi_date}\t{total_disbursed:.2f}\t\t\t{remaining_tenure}\t\t\t{emi}")

        # Update for the next month
        today += timedelta(days=30)  # Move to the next month
        remaining_tenure -= 1  # Reduce tenure by 1 month
        
print("Repayment Amount", emi_total)
