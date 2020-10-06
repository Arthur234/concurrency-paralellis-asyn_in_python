from datetime import datetime
from threading import Thread
import urllib.request as requests
import csv


def download_image(image_path, file_name):
    print("Downloading image from ", file_name)
    requests.urlretrieve(image_path, file_name)


def execute_thread(iteration):
    image_name = f'delete_me/image-{iteration}.jpg'
    download_image(
        image_path="http://lorempixel.com/400/200/sports",
        file_name=image_name,
    )


def main(iterations):
    threads = []
    for iteration in range(iterations):
        thread = Thread(target=execute_thread, args=(iteration,))
        threads.append(thread)
        print(f"Thread: {thread} started")
        thread.start()

    for thread in threads:
        thread.join()
        print(f"Thread {thread} joined.")


def write_logs(files_count, duration, filename="log_file.csv"):
    with open(filename, 'a+') as log_file:
        reader = csv.DictWriter(log_file, fieldnames=["Files", "Duration"])
        reader.writerow({
            "Files": files_count,
            "Duration": str(duration)
        })


if __name__ == '__main__':
    number_of_cycles = 1

    for _ in range(number_of_cycles):
        number_of_iterations = 997
        start = datetime.now()
        main(number_of_iterations)
        duration = datetime.now() - start
        # write_logs(number_of_iterations, duration)
