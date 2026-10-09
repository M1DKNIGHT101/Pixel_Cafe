import pandas as pd

df =pd.read_csv('pixel_cafe_sales.csv')
# print(df) # will print table of data to terminal




#1. Inspect: display the shape and column headings.
#print(df.shape)      # (number of rows, number of columns)
# print(df. columns)



#2. Select: display Product and Quantity together.
# print(df[["Product", "Quantity"]])



#3. Filter: display Food rows.
# food = df[df['Category'] == 'Food']
# print(food)

# Then display all rows with quantities greater than 30.
# busy = df[df["Quantity"] > 30]
# print(busy)

# only food items over 30
# both = df[(df["Quantity"] > 30) & (df["Category"] == "Food")]
# print(both)



# 4. Sort: display the three rows with the largest quantities
# ranked = df.sort_values("Quantity", ascending=False)
# print(ranked.head(3))



# 5. Calculate: add Revenue = Price * Quantity.
df["Revenue"] = df["Price"] * df["Quantity"]
print(df[["Product", "Price", "Quantity", "Revenue"]])



# 6. Summarise: display the total revenue in pounds.
# total_revenue = df["Revenue"].sum()
# print(f"Total revenue: £{total_revenue:.2f}")


# A. Display all Friday rows.
# friday = df[df["Day"] == ["Friday"]
# print(friday)


# B. Find Friday's total revenue.
# friday_revenue = friday["Revenue"].sum()
# print(f"Friday's total revenue: £{friday_revenue:.2f}")

# C. Display the five rows with the highest revenue.
# highest_revenue = df.sort_values("Revenue", ascending=False)
# print(highest_revenue.head(5))

# D. Find total Food revenue for the week.
# food = df[df["Category"] == "Food"]
# food_revenue = food["Revenue"].sum()
# print(f"Weekly Food revenue: £{food_revenue:.2f}")

# E. Write a recommendation using two figures.
# Students should write their own recommendation.
# print(
#     f"I recommend checking food stock before Friday. "
#     f"Friday generated £{friday_revenue:.2f} across all categories, "
#     f"and Food generated £{food_revenue:.2f} over the week. "
#     f"We should check Friday's food sales before deciding "
#     f"how much extra stock to order."
#)