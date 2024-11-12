# Define the function to calculate the discounted price
def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Subtract the discount amount from the original price
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if discount is less than 20%
        return price

# Prompt the user for the original price and discount percentage
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Call the calculate_discount function
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the result
    if final_price < original_price:
        print(f"The final price after applying the discount is: {final_price}")
    else:
        print(f"No discount applied. The original price is: {original_price}")

except ValueError:
    print("Please enter valid numeric values for price and discount percentage.")
