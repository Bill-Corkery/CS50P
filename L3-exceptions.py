def main():
    x = get_int("What is X? ")
    print(f"x is {x}")

def get_int(prompt):
    while True: 
        try:
            x = int(input(prompt))
            #return X this is a way to return it. Can also remove x and only return int.     
        except ValueError:
            # print("x is not an integer") pass below also is a way to handle error. 
            pass
        else: #happens if try and succeeded
            return x

main()