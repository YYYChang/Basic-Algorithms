#select the biggest 2 num in a num set
def multiply_max2_1(numbers) :
    n = len(numbers)
    result = 0
    for i in range(n) :
        for j in range(i+1,n) :
            if result < numbers[i] * numbers[j] :
                result = numbers[i] * numbers[j]
    return result

def multiply_max2_2(numbers) :
    max1 = max(numbers)
    numbers.pop(numbers.index(max1))
    max2 = max(numbers)
    return max1*max2

def multiply_max2_3(numbers) :
    n = len(numbers)
    max1_index, max2_index = -1, -1
    for i in range(n) :
        if max1_index == -1 or numbers[max1_index] < numbers[i] :
            max1_index = i
    for i in range(n) :
        if i != max1_index and (max2_index == -1 or numbers[max2_index] < numbers[i]) :
            max2_index = i
    return(numbers[max1_index]*numbers[max2_index])

if __name__ == '__main__':
    try:
        qty = int(input())
    except:
        print('Enter shuld be number!')
        exit()
    while True :
        nstr = input()
        if nstr == 'quit' :
            print('Goodbye!')
            exit()
        nlst = list(map(int, nstr.split()))
        if len(nlst)!= qty :
            print('Wrong input qty.!')
        else : break
    print(multiply_max2_3(nlst))
