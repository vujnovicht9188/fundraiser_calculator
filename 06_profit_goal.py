#functions go here

# checks that user has enetered yes / no to a question
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

def profit_goal(total_costs):

    # Initialise variables and error message
    error = "Please enter a valid profit goal\n"

    valid = False
    while not valid:

        # ask user for profit goal
        response = input("What is your profit goal? (eg $500 or 50%) ")

        # check if first character is $...
        if response[0] == "$":
            profit_type = "$"
            # Get amount (everything after the $)
            amount = response[1:]
            
            # check if last charcter is %
        elif response[-1] == "%":
            profit_type = "%"
            # Get amount (everything after the %)
            amount = response[:-1]

        else:
            # set response to amount for now
            profit_type = "unknown"
            amount = response

        try:
            # check amount is a number more than zero...
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue
        except ValueError:
            print(error)
            continue

        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no("Do you mean ${:.2f} ie {:.2f} dollars?, y / n ".format(amount, amount))

            # set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            dollar_type = yes_no("Do you mean ${:.2f} ie {:.2f} dollars?, y / n ".format(amount, amount))

            # set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"               

        # return profit goal to main routine
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal


# Main routine goes here


