from test_2 import Test2


def addition(first,second):
    return first + second

print(addition(1,2))

if __name__ == '__main__':
    sum = addition(10,20)
    sum2 = Test2.divition(10,100)
    sum += 20
    print(sum)
    print(sum2)