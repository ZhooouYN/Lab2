def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    cal_average(num_list)
    find_min_max(num_list)
    ordered = sort_temperature(num_list)
    cal_median_temperature(ordered)

def display_main_menu():
    print("Enter some numbers separated by commas : ")

def get_user_input():
    num = input().split(",")
    Nums = [float(ele) for ele in num]
    print(Nums)
    return Nums

def cal_average(num_list):
    average = sum(num_list)/len(num_list) 
    print("the average value is " + average)
    return average

def find_min_max(nums):
    minimum = min(nums)
    maximum = max(nums)
    Num_list = [minimum, maximum]
    print("minimum and maximum values are: " + Num_list)
    return Num_list
    
def sort_temperature(List):
    ordered = List.sort()
    return ordered

def cal_median_temperature(List):
    L = len(List)
    if L%2 == 1: #odd number
        median = List[(L-1)/2]
    else:        #even number
        median = List[((L/2-1)+(L/2))/2]
        #print(statistics.median(List))
    print("the median value is : " + median)
    return median

if __name__ =="__main__":
    main()
