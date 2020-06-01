import random
ROWS = 10
COLS = 5
def main():
    numbers = [[0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0]]
    counter = 0
    it = 0
    list = []
    while counter != 50:
        for r in range(ROWS):
            for c in range(COLS):
                while True:
                    num = random.randint(1, 50)
                    n = 5
                    it += 1
                    if num not in list and n != 0:
                        list.append(num)
                        counter += 1
                        numbers[r][c] = num
                        print(numbers[r][c], '\t', end='')
                        n -= 1
                        break
                    else:
                        continue
            print()
    print('\nIterations', it)
main()