# 1. Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # Check if discount is 20% or higher
        discount_amount = price * (discount_percent / 100)  # Calculate discount
        return price - discount_amount  # Return discounted price
    else:
        return price  # Return original price if discount is less than 20%




# 2. Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.

price = 1000
discount_percent = 25

# 3. Call the function AND PRINT THE RESULT
final_price = calculate_discount(price, discount_percent)
print(f"Final price after discount: {final_price}")

price = 1000
discount_percent = 10

# 3. Call the function AND PRINT THE RESULT
final_price = calculate_discount(price, discount_percent)
print(f"Final price after discount: {final_price}")