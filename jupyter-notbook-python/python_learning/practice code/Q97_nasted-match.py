# Use nested match statements to match a number and print detailed info (e.g., even/odd and positive/negative).

def detailed_info(num):
    match num:
        case 0:
            print("Number is zero")
        case _:
            # First, check if number is positive or negative
            match num > 0:
                case True:
                    pos_neg = "positive"
                case False:
                    pos_neg = "negative"

            # Then, check if number is even or odd
            match num % 2 == 0:
                case True:
                    even_odd = "even"
                case False:
                    even_odd = "odd"

            print(f"Number is {pos_neg} and {even_odd}")

# Test examples
detailed_info(10)   # Number is positive and even
detailed_info(-7)   # Number is negative and odd
detailed_info(0)    # Number is zero
