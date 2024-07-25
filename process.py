from multiprocessing import Process, cpu_count
from time import perf_counter


def factorize(number):
    result = []
    factors = []
    last = number + 1
    for i in range(1, last):
        if number % i == 0:
            factors.append(i)
    result.append(factors)
    print(result)
    


if __name__ == '__main__':
    start_time = perf_counter()

    # results = factorize(128, 255, 99999, 10651060)
    # a, b, c, d = results
    # a, b, c, d = factorize(128, 255, 9999, 10651060)
    # print(a)
    # print(b)
    # print(c)
    # print(d)
    process = []
    numbers = (128, 255, 99999, 10651060)
    for num in numbers:
        pr = Process(target=factorize, args=(num, ))
        pr.start()
        process.append(pr)

    [pr.join() for pr in process]

    # assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    # assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    # assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    # assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395,
    #              532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    cpu_num = cpu_count()
    print(f'Number of CPU = {cpu_num}')
    end_time = perf_counter()
    print (f'Complete in {end_time - start_time: 0.2f} seconds.')
