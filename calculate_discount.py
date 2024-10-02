

# # Calculating the Dicounted Prices

# In[1]:


def calculate_discount(price, discount_percent):
    #discount 
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# In[2]:


# Prompt the user to enter the original price and discount percentage
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(price, discount_percent)

    # Display the final price or original price
    if discount_percent >= 20:
        print(f"Final price after {discount_percent}% discount: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${price:.2f}")
except ValueError:
    print("Please enter valid numerical values for price and discount percentage.")


# In[ ]:





# In[ ]:




