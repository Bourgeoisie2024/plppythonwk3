# 1. Create a function named calculate_discount(price, discount_percent)

def calculate_discount(price, discount_percent):
    """
    This function calculates the final price after applying a discount.
    
    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to be applied.
    
    Returns:
    float: The final price after applying the discount if the discount is 20% or higher,
           otherwise returns the original price.
    """
    # Check if the discount percentage is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate the final price after applying the discount
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price

# 2. Prompt the user to enter the original price and discount percentage

def main():
    """
    Main function to prompt the user for input and print the final price after applying the discount.
    """
    # Prompt the user to enter the original price
    price = float(input("Enter the original price of the item: "))
    
    # Prompt the user to enter the discount percentage
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate the final price using the calculate_discount function
    final_price = calculate_discount(price, discount_percent)
    
    # Print the final price
    if discount_percent >= 20:
        print(f"The final price after applying the discount is: {final_price}")
    else:
        print(f"No discount applied. The original price is: {price}")

# Call the main function
if __name__ == "__main__":
    main()

# Output:

#Enter the original price of the item: 50.0
#Enter the discount percentage: 25
#The final price after applying the discount is: 37.5

# Explanation:

# calculate_discount() Function:

# 1. Parameters: price and discount_percent.
# 2. Condition: Checks if the discount percentage is 20% or higher.
# 3. Calculation: If the condition is met, it calculates the discount amount and the final price. Otherwise, it returns the original price.
# 4. Return: The final price after applying the discount or the original price.

# main() Function:

# 1. User Input: Prompts the user to enter the original price and discount percentage.
# 2. Function Call: Calls calculate_discount() to get the final price.
# 3. Output: Prints the final price or the original price based on the discount percentage.