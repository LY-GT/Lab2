def main():
    print("ET075 (DevOpsfor AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    TempAvg = calc_average_temperature(num_list)
    minmax = calc_min_max_temperature(num_list)
    print ("The average temperature is " + str(TempAvg))
    print ("The highest temperature is " + str(minmax[0]))
    print ("The lowest temperature is " + str(minmax[1]))
    print (num_list)
    print (TempAvg)

def display_main_menu():
    print("Enter some numbers seperated by commas (e.g. 5,67,32)")

def get_user_input():
    usr_str = input()
    inputs = usr_str.split(",")
    return ([float(x) for x in inputs])

def calc_average_temperature(list_of_no):
    x = len(list_of_no)
    sum = 0
    for i in range(x):
        sum = list_of_no[i] + sum
    avg = sum / x
    return avg

def calc_min_max_temperature(list_of_no):
    high = max(list_of_no)
    low = min(list_of_no)
    return [high,low]

if __name__ == "__main__":
    main()
