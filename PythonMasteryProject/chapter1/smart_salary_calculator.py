"""
Docstring for chapter1.smart_salary_calculator!
Write a program for the accounting department of a startup company. This program should:

Take as input: employee name, base salary (in Tomans), and number of overtime hours.

Calculate:

The rate for each overtime hour is 1.5 times the regular hourly rate (assuming 160 hours of work per month).

If the total salary (base + overtime) was below 12 million Tomans, the tax is 0%.

If it was between 12 and 20 million, the tax is 10% on the amount in excess of 12 million.

If it was above 20 million, the tax is 20% on the amount in excess of 20 million (plus the previous tax bracket).

Output: Pay slip including name, gross salary, tax amount, and net salary received.
"""
employee_name = input("Enter your name: ")
try:
    income = int(input("Enter your salary (in Tomans): "))
    overtime_work = int(input("Enter your overtime work (hours): "))
    
    # Calculation Logic
    hourly_rate = income / 160
    overtime_rate = hourly_rate * 1.5
    total_overtime_pay = overtime_work * overtime_rate
    gross_salary = income + total_overtime_pay

    # Tax Logic
    tax = 0
    if gross_salary > 20000000:
        tax = 800000 + (gross_salary - 20000000) * 0.20
    elif gross_salary > 12000000:
        tax = (gross_salary - 12000000) * 0.10

    net_salary = gross_salary - tax

    # Final Output
    print("-" * 30)
    print(f"Employee: {employee_name}")
    print(f"Gross Salary: {gross_salary:,.0f} Toman")
    print(f"Tax: {tax:,.0f} Toman")
    print(f"Net Salary: {net_salary:,.0f} Toman")
    print("-" * 30)

except ValueError:
    print("Error: Please enter numbers only for salary and hours.")