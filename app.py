import time

def is_odd(number):
    if((number % 2) == 0):
        return False
    else:
        return True

def print_sleep(result):
    print(f'Value: {result}')
    time.sleep(0.3)

def calc(number_to_use):
    if(is_odd(number_to_use)):
        result = int((number_to_use*3)+1)
        print_sleep(result)
    else:
        result = int(number_to_use/2)
        print_sleep(result)
    return calc(result)



if(__name__ == '__main__'):
    number_to_use = input()

    calc(int(number_to_use))