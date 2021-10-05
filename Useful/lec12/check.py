import concurrent.futures
import os
import time
import threading
import multiprocessing
from more_itertools import unique_everseen


def find_primes(end, start=3):
    if start > end:
        return "Начало больше конца"
    sieve = list(range(end + 1))
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    # sieve = list(set(sieve))
    sieve = list(unique_everseen(sieve))
    for nom, i in enumerate(sieve):
        if i >= start:
            sieve = sieve[int(nom):int(len(sieve))]
            break

    print(f'Найдено простых чисел в диапозонен от {start} до {end}: {len(sieve)}')
    print(sieve)
    return sieve


def all_calc(*args):
    print(f'This process {os.getpid()} processed values {args} ')
    time.sleep(0.1)  # чтобы разные процессы
    flag1 = False  # на список
    flag2 = False  # на строку
    final_result = 0  # изначально считаем что сумма чисел
    for arg in args:
        if type(arg) == list:  # соберем все в список
            flag1 = True
            final_result = []
            break
        if type(arg) == str:  # соберем все в строку
            flag2 = True
            final_result = ''

    for arg in args:
        if type(arg) != list and flag1 is True:  # соберем все в список
            final_result.append(arg)
        elif type(arg) != str and flag1 is False and flag2 is True:  # соберем все в строку
            final_result += str(arg)
        else:  # соберем все
            final_result += arg
    return final_result


def thread_function(atr1):

    __privater = threading.current_thread().name
    print(f'Имя процесса {atr1}: {__privater}')
    time.sleep(1)

    return __privater


if __name__ == "__main__":
    find_primes(10, 0)
    # Задание 1
    # от 3 до 10000, от 10001 до 20000, от 20001 до 30000
    start_time = time.time()
    print('Вариант1')
    find_primes(10000)
    find_primes(20000, 10001)
    find_primes(30000, 20001)
    print(f'Время выполнения 1 - {(time.time() - start_time)}', )

    # Вар2. без thr.start() - поток будет создан но не запущен
    # Метод join приостановит выполнение потока, вызвавшего его, и будет ждать когда поток th завершит свое выполнение.
    # Иначе выполнится код далее в вызвавщем потоке
    start_time = time.time()
    print('Вариант2')
    threads = []

    thr = threading.Thread(target=find_primes, args=(10000,))
    thr.start()
    threads.append(thr)

    thr = threading.Thread(target=find_primes, args=(20000, 10001))
    thr.start()
    threads.append(thr)

    thr = threading.Thread(target=find_primes, args=(30000, 20001))
    thr.start()
    threads.append(thr)

    for thr in threads:
        thr.join()
    print(f'Время выполнения 2 - {(time.time() - start_time)}', )

    # Вар3. start и join аналогичны threading.Thread
    # при по умолчанию, когда основной процесс готов к выходу, он неявно вызывает join()все запущенные
    # multiprocessing.Process экземпляры
    # можно установить daemon флаг, тогда по завершению основного процесса демонический процесс будет завершен
    start_time = time.time()
    print('Вариант3')
    p1 = multiprocessing.Process(target=find_primes, args=(10000,))
    p2 = multiprocessing.Process(target=find_primes, args=(20000, 10001))
    p3 = multiprocessing.Process(target=find_primes, args=(30000, 20001))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print(f'Время выполнения 3 - {(time.time() - start_time)}', )

    # Создание процессов трудаёмко и на таких диапазонах занимает больше времени,
    # если увеличить диапазон например до 30000000 то процессы будут быстрее

    # Задание 2
    #if __name__ == '__main__':
    with multiprocessing.Pool(processes=3) as pool:
        # pool = multiprocessing.Pool(processes=3)
        res1 = pool.starmap(all_calc, [(2, 1, 'Слово'), ('Сло', 'во'), ('Сло', 1), (5, 6)])
        res2 = pool.starmap(all_calc, [('sdr', [9, 'asdf'], 7, ['qwe', 2]), ])
    print(res1)
    print(res2[0])

    # Задание 3
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        all_tr = executor.map(thread_function, range(3))
    results = list(all_tr)
    print(f'Имена процессов: {results}')