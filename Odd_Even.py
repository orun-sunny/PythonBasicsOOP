def is_even (number):
    if number%2 == 0:
        return True
    else:
        return False
even_numbers = []
starting =0
use_input = int(input("Limit:"))
while starting <= use_input:
    if is_even(starting):
        even_numbers.append(starting)

    starting =starting+1
print(f"Even number : {even_numbers} ")

print("Finished")