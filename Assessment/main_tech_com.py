import pandas
import math
def string_checker(question, valid_ans_list, num_letters = 1):
    """checks if the user has input a valid answer from a list and also allows for """
    while True:
        response = input(question).lower()
        for item in valid_ans_list:
            if response == item:
                return item
            elif response == item[:num_letters]:
                return item
        print(f"Please choose an option from {valid_ans_list}")

def make_statement(statement, decoration):
    """formats a statement to make it look appealing to the user"""
    print(f"{decoration * 3} {statement} {decoration * 3}")
def num_check(question, num_type, exit_code='xxx'):
    """checks if the users number is more than 0"""
    if num_type == "integer":
        error = "Please enter a integer more than zero"
        change_to = int
    else:
        error = "Please enter a number more than zero"
        change_to = float
    while True:
        response = input(question).lower()
        if response == exit_code:
            return response
        try:
            response = change_to(response)
            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)
#main routine
# title
make_statement("Welcome to the area/perimeter calculator","#")
#instructions
instructions = ("first input how many questions you would like to solve"
                "then you input if you are solving a area or perimeter question"
                "after that you input what shape you are solving"
                "then you input the dimensions of the shape"
                "")
# initialise num_questions
num_questions = 0
# initialise lists/ pandas lists
yes_no = ['yes', 'no']
area_or_perimeter = ['area', 'perimeter', 'xxx']
shapes = ['square', 'triangle', 'rectangle', 'circle', 'xxx']
ans_list = []
num_questions_list = []
working_list = []

# pandas dictionary
panda_dict = {
    'Question': num_questions_list,
    'Working': working_list,
    'Answer': ans_list
}

# prints instructions on request
want_instructions = string_checker("Do you want to see the instructions? ",yes_no,1)
if want_instructions == "yes":
    make_statement("Instructions", "+")
    print(instructions)
# asks the user how many questions
how_many = num_check("How many questions do you want to solve? ", "int", "xxx")

# runs the questions
while num_questions < how_many:
    num_questions += 1
    make_statement(f"Question {num_questions}", '-')
    what_mode = string_checker("area or perimeter? ", area_or_perimeter,)
    what_shape = string_checker("What shape are you trying to solve? ", shapes,)

    # checks if the user is working out the perimeter
    if what_mode == "perimeter":
        # checks if the exit code is used during a perimeter shape selection
        if what_shape == "xxx":
            break
        # checks if the shape is a circle and if so then apply the right formula
        if what_shape == "circle":
            radius = num_check("what is the radius? ", float)
            ans = 2 * math.pi * radius
            working = f"2 x pi x {radius:.2f}"

        # checks if the shape is a triangle and if so then apply the right formula
        elif what_shape == "triangle":
           #checks if the user has all 3 sides if not gives an error, if so continues
           have_sides = string_checker("do you have all 3 sides? ", yes_no)
           if have_sides == "yes":
               s1 = num_check("what is side 1? ", float)
               s2 = num_check("what is side 2? ", float)
               s3 = num_check("what is side 3? ", float)
               ans = s1 + s2 + s3
               working = f"{s1:.2f} + {s2:.2f} + {s3:.2f}"
           else:
               tri_error = "you cant solve this questions without all 3 sides"
               print(tri_error)
               ans = "n/a"
               working = "n/a"

        # checks if the shape is a square and if so then apply the right formula
        elif what_shape == "square":
            side = num_check("what is the base? ", float)
            ans = 4 * side
            working = f"{side:.2f} + {side:.2f} + {side:.2f} + {side:.2f} "
        # if it's not any other shape it deems it to be a rectangle
        else:
            base = num_check("what is the base? ", float)
            height = num_check("what is the height? ", float)
            ans = 2 * height + 2 * base
            working = f"{height:.2f} + {base:.2f} + {height:.2f} + {base:.2f} "

    #checks if it is working out the area
    if what_mode == "area":
        # checks if the exit code is used during an area shape selection
        if what_shape == "xxx":
            break
        # checks if the shape is a circle and if so then apply the right formula
        if what_shape == "circle":
            radius = num_check("what is the radius? ", float)
            ans =   math.pi * (radius * radius)
            working = f"pi x {radius:.2f} squared"
        # checks if the shape is a triangle and if so then apply the right formula
        elif what_shape == "triangle":
            base = num_check("what is the base? ", float)
            height = num_check("what is the height? ", float)
            ans = (1/2 * base) * height
            working = f"(1/2 * {base:.2f}) * {height:.2f}"
        # checks if the shape is a square and if so then apply the right formula
        elif what_shape == "square":
            side = num_check("what is a side? ", float)
            ans = side * side
            working = f"{side:.2f} × {side:.2f}"
        # if it's not any other shape it deems it to be a rectangle
        else:
            base = num_check("what is the base? ", float)
            height = num_check("what is the height? ", float)
            ans = height * base
            working = f"{height:.2f} × {base:.2f}"
    # checks if the exit code (xxx) is used during area perimeter selection
    elif what_mode == "xxx":
        break
    #prints the working
    print(working)
    # prints the answer
    print()
    if what_mode == "perimeter":
        if what_shape == "triangle" and have_sides == "no":
            print(f"{ans}")
        else:
            print(f"the {what_mode} is {ans:.2f} units")
    else:
        print(f"the {what_mode} is {ans:.2f} units squared")
    #adds to a list at the end of a round
    ans_list.append(f"{ans:.2f}")
    num_questions_list.append(num_questions)
    working_list.append(working)
#pandas
panda_frame = pandas.DataFrame(panda_dict)
panda_string = panda_frame.to_string(index=False)
#prints panda
print(panda_string)