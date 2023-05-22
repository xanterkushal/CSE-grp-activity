def calculate_daily_wage(hours_worked, hourly_rate):
    if hours_worked <= 8:
        daily_wage = hours_worked * hourly_rate
    else:
        overtime_hours = hours_worked - 8
        overtime_pay = overtime_hours * (hourly_rate * 1.5)
        daily_wage = (8 * hourly_rate) + overtime_pay
    return daily_wage

# Example usage
hours_worked = float(input("Enter the number of hours worked: "))
hourly_rate = float(input("Enter the hourly rate: "))

daily_wage = calculate_daily_wage(hours_worked, hourly_rate)
print("Daily Wage: $", daily_wage)
