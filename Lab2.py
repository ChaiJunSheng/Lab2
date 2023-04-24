def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_input = input("Enter temp:")
    num_list =user_input.split(",")
    float_list = list(map(float, num_list))  #Change str type to floating number
    print(float_list)
    return float_list

def calc_average_temperature(float_list): #(float_list), taking varible from a different function
    average = sum(float_list)/len(float_list) #sum(),is to find the sum. len(), number of numbers in the list
    print(average)

def calc_min_max_temperature(float_list):
    print("The min value is=" + str(min(float_list)))  #min(), find the min in list
    print("The max value is=" + str(max(float_list)))  #max(), find the max in list
    import statistics   #Need import library, like c++ include
    print("The median value is=" + str(statistics.median(float_list)))  #statistics.median(),find median


def main():
    display_main_menu()
    float_list=get_user_input()
    calc_average_temperature(float_list)
    calc_min_max_temperature(float_list)

if __name__ == "__main__":
    main()

