import concurrent.futures
import random
from tqdm import tqdm

def estimate_pi_part(n):
    count = 0
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            count += 1
    return count

def estimate_pi(num_points, num_processes):
    points_per_process = num_points // num_processes
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(estimate_pi_part, points_per_process) for _ in range(num_processes)]
        results = []
        for future in tqdm(concurrent.futures.as_completed(futures), total=num_processes):
            results.append(future.result())
    return 4 * sum(results) / num_points

# 使用10个进程和10000个点来估计π
print(estimate_pi(1000000, 10))
