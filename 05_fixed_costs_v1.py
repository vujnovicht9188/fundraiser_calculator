# import libraries
import pandas


# *** Functions go here ***

# checks that input is either float or integer that is more than zero.
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Ask user Yes/No question and make sure answer is valid
def yes_no(question):

    to_check = ['yes', 'no']

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("Please enter either yes or no...\n")

def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}.  \nPlease try again. \n".format(error))
            continue
    
        return response

# currency formatting function
def currency(x):
    return "${:.2f}".format(x)

# Gets expenses, returns list which has the data frame and sub total
def get_expenses(var_fixed):
   
    # Set up dictionaries and lists

    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list,
    }
    
    # loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":

        print()
        
        # get name, quantity and item
        item_name = not_blank("Item name: ", "The component name can't be blank.")
        if item_name.lower() == "xxx":
            break

        if var_fixed == "variable":
            
            quantity = num_check("Quantity: ", "The amount must be a whole number more than zero", int)
        
        else:
            quantity = 1

        price = num_check("How much for a single item? $", "The price must be a number <more than zero>", float)

          # add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    variable_frame = pandas.DataFrame(variable_dict)
    variable_frame = variable_frame.set_index('Item')

    # calculate cost of each component
    variable_frame['Cost'] = variable_frame['Quantity'] * variable_frame['Price']

    # Find sub total
    sub_total= variable_frame['Cost'].sum()

    # Currency fortmatting (uses currency function)
    add_dollars = ['Price' , 'Cost']
    for item in add_dollars:
        variable_frame[item] = variable_frame[item].apply(currency)

        return [variable_frame, sub_total]

     # *** Main Routine goes here ***

# Get product name
# product_name = not_blank("Company Name: ", "Error.. This message cannot be blank")

fixed_expenses = get_expenses("fixed")
fixed_frame = fixed_expenses[0]
fixed_sub = fixed_expenses[1]



# *** Printing Area ***

print()
print(fixed_frame)
print()

print("Variable Costs: ${:.2f}".format(fixed_sub))