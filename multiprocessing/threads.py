import time
from threading import Thread


# def do_work():
# 	print("Starting work...")
# 	time.sleep(1)  # Simulate some work
# 	print("Work done!")


def do_work():
    print("Starting work...")
    i = 0
    for _ in range(10**6):
        i += 1
    print("Work done!")


loop_count = 500


ti = time.time()

for _ in range(loop_count):
    do_work()
print(f"Time taken without threads: {time.time() - ti:.2f} seconds")


ti = time.time()
threads = []
for _ in range(loop_count):
    thread = Thread(target=do_work)
    thread.start()
    threads.append(thread)


for thread in threads:
    thread.join()

print(f"Time taken with threads: {time.time() - ti:.2f} seconds")

# We use multi-threading when we have I/O-bound tasks, such as network requests or file operations.
