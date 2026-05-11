import numpy as np
sales = np.array([20000, 25000, 18000, 8000, 27000, 35000,
                  40000, 38000, 42000, 45000, 48000, 50000])

cost = np.array([10000]*12)

profit = sales - cost

print("Mothly Cost: ", cost)
print("Mothly sales: ", sales)
print("Monthly Profit:", profit)


best_month = np.argmax(sales)
best_sales = sales[best_month]

print("Best Month:", best_month + 1)
print("Highest Sales:", best_sales)

loss_months = np.where(profit < 0)

print("Loss Months:", loss_months[0] + 1)

total_sales = np.sum(sales)
print("Total Sales:", total_sales)

total_profit = np.sum(profit)
print("Total Profit:", total_profit)

high_sales = sales[sales > 30000]
print("High Sales:", high_sales)

average_sales = np.mean(sales)
print("Average Sales:", average_sales)

max_sales = np.max(sales)
print("Max Sales:", max_sales)

min_sales = np.min(sales)
print("Min Sales:", min_sales)

best_month_q1 = np.argmax(sales[:3])
best_month_q2 = np.argmax(sales[3:6])
best_month_q3 = np.argmax(sales[6:9])
best_month_q4 = np.argmax(sales[9:])
print("best month in quarter 1:", best_month_q1+1)
print("best month in quarter 2:", best_month_q2+1)
print("best month in quarter 3:", best_month_q3+1)
print("best month in quarter 4:", best_month_q4+1)


quarters = sales.reshape(4, 3)
quarterly_max = np.argmax(quarters,axis=1)



print(quarterly_max)
