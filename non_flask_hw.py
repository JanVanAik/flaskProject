import threading
import asyncio
import multiprocessing
import time
import requests
import aiohttp
import sys

"""

    Вторым аргументом передается метод - async, threading, multiprocessing


"""


def gather_info(args):
    urls = {}
    for arg in args:
        for el in arg.split("/"):
            if ".jpg" in el:
                ind = el.find('.jpg') + 4
                name = el[:ind]
                break
        urls[arg] = name
    return urls


async def asyncr_upload(k, v): # key = url, v = file name
    pass


async def asyncr(urls, time):
    pass
    tasks = []
    for k, v in urls.items():
        task = asyncio.ensure_future(asyncr_upload(k,v))
        tasks.append(task)
    await asyncio.gather(*tasks)


def thread_upload(k, v, thread_time):
    single_thread_time = thread_time
    response = requests.get(k)
    with open(v, 'wb') as f:
        f.write(response.content)
        print(f'Изображение {f.name} загружено Мультипотоком. Время работы {time.time() - single_thread_time} ')


def thread(urls):
    threads = []
    for k, v in urls.items():
        thread_time = time.time()
        thread = threading.Thread(target=thread_upload, args=(k, v, thread_time))
        threads.append(thread)
        thread.start()
    print(f'Итоговое время работы программы: {time.time() - start_time}')

def proc_upload(k, v, proc_time):
    single_proc_time = proc_time
    response = requests.get(k)
    with open(v, 'wb') as f:
        f.write(response.content)
        print(f'Изображение {f.name} загружено Мультипроцессингом. Время работы {time.time() - single_proc_time} ')


def multiprocess(urls):
    multiprocs = []
    for k, v in urls.items():
        proc_time = time.time()
        proc = multiprocessing.Process(target=proc_upload, args=(k, v, proc_time))
        multiprocs.append(proc)
        proc.start()
    for proc in multiprocs:
        proc.join()
    print(f'Итоговое время работы программы: {time.time() - start_time}')


start_time = time.time()
functions = {
    'thread': thread,
    'multiprocess': multiprocess,
    'asyncr': asyncr
}


def main(*args):
    # method = sys.argv[0]
    # method(gather_info(sys.argv[1:]))
    method = args[0]
    functions[method](gather_info(list(args[1:])))

#
# main("thread",
#      "https://sun1-92.userapi.com/impg/lfno5dmntkm5WYFW8RDb5e7zA77eA21J4lTHrg/Hcl_pIdhBnM.jpg?size=1620x2160&quality=96&sign=4e2a3dca23b0d93b1b85d4029448ce8f&type=album",
#      "https://sun1-18.userapi.com/impg/bM1xTJC9Zcg8YviAyl1lIiiLfihFZqC9TMM7FA/obIUL1lNUpM.jpg?size=1620x2160&quality=95&sign=984baeee09ceb93a2606bc73a994954a&type=album")

# main("multiprocess",
#      "https://sun1-92.userapi.com/impg/lfno5dmntkm5WYFW8RDb5e7zA77eA21J4lTHrg/Hcl_pIdhBnM.jpg?size=1620x2160&quality=96&sign=4e2a3dca23b0d93b1b85d4029448ce8f&type=album",
#      "https://sun1-18.userapi.com/impg/bM1xTJC9Zcg8YviAyl1lIiiLfihFZqC9TMM7FA/obIUL1lNUpM.jpg?size=1620x2160&quality=95&sign=984baeee09ceb93a2606bc73a994954a&type=album")

main("asyncr",
     "https://sun1-92.userapi.com/impg/lfno5dmntkm5WYFW8RDb5e7zA77eA21J4lTHrg/Hcl_pIdhBnM.jpg?size=1620x2160&quality=96&sign=4e2a3dca23b0d93b1b85d4029448ce8f&type=album",
     "https://sun1-18.userapi.com/impg/bM1xTJC9Zcg8YviAyl1lIiiLfihFZqC9TMM7FA/obIUL1lNUpM.jpg?size=1620x2160&quality=95&sign=984baeee09ceb93a2606bc73a994954a&type=album")

# if __name__ == '__main__':
#     print('Первым аргументом передайте желаемый метод обработки.\n'
#           '"asyncr" : Асинхронный подход\n'
#           '"thread": Мультипотоковый подход\n'
#           '"multiprocess": Мультипроцессовый подход\n'
#           'Последующими аргументами передайте url адреса')
#     main()
