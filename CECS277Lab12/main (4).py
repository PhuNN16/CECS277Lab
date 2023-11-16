import check_input
import green_beans
import large_plate
import pie
import potatoes
import small_plate
import stuffing
import turkey


def examine_plate(p):
    '''Prints the plate and its status'''
    print(p.description()[:-4])

    if p.area() <= 0 or p.weight() <= 0:
        return True
    
    print_list = ["Bending", "Weak", "Strong"]
    strength = min((p.weight() - 1) // 6, 2)
    print("Sturdiness: ",  print_list[strength])

    return False

def main():
    print('- Thanksgiving Dinner -')
    print('Serve yourself as much food as you ' + 
    'like from the buffet, but make sure ' + 
    'that your plate will hold without ' +
    'spilling everywhere!')

    plate_choice_string = 'Choose a plate:\n1. Small Sturdy Plate\n2. Large Flimsy Plate\n'
    plate_choice = check_input.get_int_range(plate_choice_string, 1, 2)
    list_of_plates = [small_plate.SmallPlate, large_plate.LargePlate]
    food_plate = list_of_plates[plate_choice - 1]()
    count = -1
    while True:
        food_choice_string = '1. Turkey\n2. Stuffing\n3. Potatoes\n4. Green Beans\n5. Pie\n6. Quit\n'
        food_choice = check_input.get_int_range(food_choice_string, 1, 6)
        count += 1
        if food_choice == 6:
            examine_plate(food_plate)
            print(f"Good job! You made it to the table with {count} items.",
                  f"There was still {food_plate.area()} square inches left ",
                  f"on your plate. Your plate could have held {food_plate.weight()}", 
                  "more ounces of food. Don't worry, you can always go back for more.",
                  "Happy Thanksgiving!")
            break
            
        list_of_food = [turkey.Turkey, stuffing.Stuffing, potatoes.Potatoes, 
                        green_beans.GreenBeans, pie.Pie]
        food_plate = list_of_food[food_choice - 1](food_plate)
        if examine_plate(food_plate) is True:
            print("Your plate isn't big enough for this much food!",
                  "\nYour food spills over the edge.")
            break
        


main()