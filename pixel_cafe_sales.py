import pandas as pd

df = pd.read_csv('pixel_cafe_sales.csv')
print(df) # will print table of data to terminal 





#1. Inspect: display the shape and column headings.
#print(df.shape)      # (number of rows, number of columns)
print(df. columns)



#2. Select: display Product and Quantity together.
print(df[["Product", "Quantity"]])



#3. Filter: display Food rows.
food = df[df['Category'] == 'Food']
print(food)

# Then display all rows with quantities greater than 30.
busy = df[df["Quantity"] > 30]
print(busy)

# only food items over 30
both = df[(df["Quantity"] > 30) & (df["Category"] == "Food")]
print(both)
