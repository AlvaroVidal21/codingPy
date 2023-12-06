
def my_fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"FizzBuzz - M3 & M5 {i}")
            continue
        
        elif i % 5 == 0:
            print(f"Buzz - M5 {i}")
            continue

        elif i % 3 == 0 :
            print(f"Fizz - M3 {i}")
            continue

        else:
            print(i)
            continue





def run():
    my_fizzbuzz()


if __name__ == '__main__':
    run()