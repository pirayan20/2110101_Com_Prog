def make_car_type(CM, m, t): 
    # return True if the maker m makes the car type t, otherwise return False
    if t in CM[m]:
        return True
    else:
        return False

def find_makers(CM, t):
    # return a list of car makers that makes the car type t in alphabetical order (A-Z).    
    l = []
    for i in CM:
        if t in CM[i]:
            l.append(i)
    l.sort()
    return l

def print_maker_with_most_type(CM):
    # print the maker that makes the most car types. 
    # if there are more than one maker that makes the most car types, 
    #   print all those makers in alphabetical order (A-Z) seperated by comma (,)
    most = []
    max = 0
    for brand in CM:
        if len(CM[brand]) > max:
            max = len(CM[brand])
            most = [brand]
        elif len(CM[brand]) == max:
            most.append(brand)
    most = sorted(most)
    print(','.join(most))

def read_cm() :
    # build a dictionary CM from inputs, of which structure is shown in the example given above
    CM = dict()
    while True:
        d = input().split(' : ')
        if len(d) == 1 : break
        else:
            brand = d[1].split(',')
            for i in brand:
                if i not in CM:
                    CM[i] = set()
                CM[i].add(d[0])
    return CM

x = read_cm()
print(make_car_type(x,'BMW','Coupe'))