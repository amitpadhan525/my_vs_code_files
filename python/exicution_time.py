import time
start=time.time()
for i in range(10000000):
    print(i)
end=time.time()
print(f"Execution Time: {end - start} seconds")