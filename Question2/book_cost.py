"""
file:       book_cost.py
created:    9/28/2021 11:08 PM
author:     ciaran mcdevitt
version:    v1.0.0
licensing:  (c) 2021 Ciaran McDevitt, LYIT
            available under the GNU Public License (GPL)

description:  Program to accept book title & cost input and output a running total
credits:

"""
running_total = 0.0

if __name__ == "__main__":
    '''
    main function to accept 5 user inputted book titles and prices, then prints 
    out the cost of the 5 books 
    
    Parameters:
    argument1 (float): running_total (initialized to 0.0, cost of each book added inside for loop)
    
    User inputted:
    argument2 (str): title (user inputted book title)
    argument3 (str): price (user defined price - input as string and cast to a 
                    float in the try block)
                    
    Output:
    string: prints a formatted string of the title, price and running_total
      
    '''
    print("Enter the title and price of 5 books you wish to get a quote for\n")
    for i in range(5):
        title = input(f"Enter book #{i + 1}'s title:\t")
        try:
            price = float(input(f"Enter the price of {title}:\t$"))

        # output ValueError if price can't be cast to a float, and continue to accept user input
        except ValueError:
            print("Invalid price entered!\n")
            continue
        running_total += price
        print(f"-{title}\t\t${price}\t\trunning_total: (${running_total:.2f})")

    print(f"\nTotal cost: ${running_total:.2f}")



