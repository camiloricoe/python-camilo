def solution(product):
    # Check if the product is 0 or 1
    if product == 0:
        return 10
    if product == 1:
        return 1

    # Initialize the result to -1
    result = -1

    # Iterate through all integers starting from 2
    for i in range(2, 10**4):
        # Initialize the digit product to 1
        digit_product = 1

        # Calculate the product of the digits of i
        for digit in str(i):
            digit_product *= int(digit)

        # If the product of the digits is equal to the given product,
        # update the result and break out of the loop
        if digit_product == product:
            result = i
            break

    # Return the result
    return result
