import sys

if len(sys.argv) != 3: #to check if the user has provided exactly 2 arguments
    print("Error: Please provide exactly 2 arguments.")
    print("Usage: python script.py <arg1> <arg2>")
    sys.exit(1)
#populate the threshold and limit variables with the command line arguments
threshold = float(sys.argv[1])
limit = float(sys.argv[2])


input_numbers = []

#assuming there is no empty line between the numbers. And assuming empty line as a end of input
for _ in range(100):
    try:
        line = input().strip()
        if not line:
            break
        mynum = float(line)
        if not (0.0 <= mynum <= 1000000000.0):
            print("Please enter a number between 0.0 and 1000000000.0 (inclusive).")
            exit()
        input_numbers.append(mynum)
    except ValueError:
        print("Please enter a valid number.")
        exit()
    except EOFError:
        break
    

output = []
cummulative_sum = 0

#implementation of the business logic according to the given instructions at https://github.com/analyzere/problem_readme/
for num in input_numbers:
    processed_num = max(0, num - threshold)
    if cummulative_sum + processed_num >= limit:
        output.append(float(limit - cummulative_sum))
        cummulative_sum = limit
    else:
        output.append(float(processed_num))
        cummulative_sum += processed_num
output.append(float(cummulative_sum))

print(*output, sep="\n")

#writing the output to a separate file
output_filename = "output.txt"

with open(output_filename, "w") as file:
    for num in output:
        file.write(f"{num}\n")