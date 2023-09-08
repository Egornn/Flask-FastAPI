import threading
import time
import multiprocessing
import asyncio
from pathlib import Path
import requests
from multiprocessing import Process, Pool
import aiohttp
import shutil


def worker(num):
    print(f"Starting therad {num}")
    time.sleep(3)
    print(f"Ending thread {num}")


def first_threading():
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("All threads are done")


counter = 0


def increment():
    global counter
    for _ in range(1_000_000):
        counter += 1
    print(f"Counter: {counter:_}")


def second_threading():
    threads = []
    for i in range(5):
        t = threading.Thread(target=increment)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"Final counter: {counter:_}")


def worker(num):
    print(f"Process #{num}")
    time.sleep(3)
    print(f"End of process #{num}")


def first_multiprocessing():
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    print("All processes are done")


def second_multiprcoessing():
    processes = []
    for i in range(5):
        t = multiprocessing.Process(target=increment)
        processes.append(t)
        t.start()
    for t in processes:
        t.join()
    print(f"Final counter: {counter:_}")


multi_counter = multiprocessing.Value('i', 0)


def increment(cnt):
    for _ in range(10_000):
        with cnt.get_lock():
            cnt.value += 1
    print(f"Counter value: {cnt.value:_}")


def third_multiprocessing():
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=increment, args=(multi_counter,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    print(f"Value at the end: {multi_counter.value:_}")


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(1)


async def print_letters():
    for letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        print(letter)
        await asyncio.sleep(0.5)


async def main():
    task1 = asyncio.create_task(print_numbers())
    task2 = asyncio.create_task(print_letters())
    await task1
    await task2


async def count():
    print("Start")
    await asyncio.sleep(1)
    print("1 second passed")
    await asyncio.sleep(2)
    print("2 seconds passed")
    return "Done"


async def second_async():
    result = await asyncio.gather(count(), count(), count())
    print(result)


async def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        contents = f.read()
        # do some processing with the file contents
        print(f'{f.name} has {contents[:7]}...')


async def third_async():
    # dir_path = Path('/path/to/directory')
    dir_path = Path('./Lesson 1')
    file_paths = [file_path for file_path in dir_path.iterdir() if file_path.is_file()]
    tasks = [asyncio.create_task(process_file(file_path)) for file_path in file_paths]
    await asyncio.gather(*tasks)


def simple_download():
    urls = ['https://www.google.ru/',
            'https://gb.ru/',
            'https://ya.ru/',
            'https://www.python.org/',
            'https://habr.com/ru/all/',
            ]
    start_time = time.time()
    for url in urls:
        response = requests.get(url)
        filename = 'sync_' + url[url.rfind('/') + 1:]
        with open(filename, "w") as f:
            f.write(response.text)
            print(f"Downloaded {url} in {time.time() - start_time:.2f}seconds")


def thread_download(url_img):
    def download_2(url_link):
        response = requests.get(url_link, stream=True)
        filename = 'threading_' + url[url.rfind('/') + 1:]
        with open(filename, "wb") as f:
            shutil.copyfileobj(response.raw, f)
            print(f"Downloaded {url_link} in {time.time() - start_time:.2f}seconds")

    threads = []
    start_time = time.time()
    for url in url_img:
        thread = threading.Thread(target=download_2, args=[url])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


def download_process(url, start_time):
    response = requests.get(url)
    filename = 'multiprocessing_' + url[url.rfind('/') + 1:]
    with open(filename, "wb") as f:
        shutil.copyfileobj(response.raw, f)
        print(f"Downloaded {url} in {time.time() - start_time:.2f}seconds")


def multiprocessing_download(urls):
    processes = []
    start_time = time.time()
    for url in urls:
        process = Process(target=download_process, args=(url, start_time))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()


async def download_ass(url):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.read()
                filename = 'asyncio_' + url[url.rfind('/') + 1:]
                with open(filename, "wb") as f:
                    f.write(content)
                    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")
            else:
                print(f"Failed to download {url}. Status code: {response.status}")


async def async_download(urls):
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download_ass(url))
        tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    urls = ['https://www.google.com/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp.png',
            'https://www.wikimedia.org/static/images/wmf.png',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Generic_Camera_Icon.svg/100px-Generic_Camera_Icon.svg.png',
            ]
    # first_threading()
    # second_threading()
    # first_multiprocessing()
    # second_multiprcoessing()
    # third_multiprocessing()
    # asyncio.run(main())
    # asyncio.run(second_async())
    # asyncio.run(third_async())
    thread_download(urls)
    multiprocessing_download(urls)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_download(urls))
