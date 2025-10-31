import threading

def square() -> int:
    total_square = []
    result = 0
    for i in range(1,11):
        result = i**2
        total_square.append(result)
    print(total_square)

def cubic() -> int:
    total_cubic = []
    result = 0
    for i in range(1,11):
        result = i**3
        total_cubic.append(result)
    print(total_cubic)


t1 = threading.Thread(target=square)
t2 = threading.Thread(target=cubic)


print("started")
t1.start()
t2.start()

t1.join()
t2.join()







