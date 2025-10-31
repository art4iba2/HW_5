import threading
import time

def print_numbers(thread_name):
    for i in range(1, 11):
        print(f"{thread_name}: {i}")
        time.sleep(1)

threads = []
for n in range(3):
    thread = threading.Thread(target=print_numbers, args=(f"Поток-{n+1}",))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Все потоки завершили работу.")
