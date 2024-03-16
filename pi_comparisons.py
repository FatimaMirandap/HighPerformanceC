import random
import cProfile
import pstats
from multiprocessing import Pool


def sample():
    x, y = random.uniform(-1, 1), random.uniform(-1, 1)
    return 1 if x ** 2 + y ** 2 <= 1 else 0

def sample_multiple(samples):
    hits = sum(sample() for _ in range(samples))
    return hits

def pi_serial(samples):
    hits = sum(sample() for _ in range(samples))
    return (4.0 * hits) / samples

def pi_apply_async(samples):
    with Pool() as pool:
        results_async = [pool.apply_async(sample) for _ in range(samples)]
        hits = sum(r.get() for r in results_async)
    return (4.0 * hits) / samples

def pi_apply_async_chunked(samples, n_tasks=10):
    chunk_size = samples // n_tasks
    with Pool() as pool:
        tasks = [pool.apply_async(sample_multiple, (chunk_size,)) for _ in range(n_tasks)]
        hits = sum(task.get() for task in tasks)
    return (4.0 * hits) / samples

def profile_function(func, *args):
    pr = cProfile.Profile()
    pr.enable()
    result = func(*args)
    pr.disable()
    ps = pstats.Stats(pr)
    ps.sort_stats('cumulative')
    ps.print_stats()
    return result

if __name__ == '__main__':
    samples = 10000  
    print("Serial:")
    pi_serial_estimate = profile_function(pi_serial, samples)
    print("Parallel apply_async:")
    pi_apply_async_estimate = profile_function(pi_apply_async, samples)
    print("Parallel apply_async_chunked:")
    pi_apply_async_chunked_estimate = profile_function(pi_apply_async_chunked, samples, 10)

    print(f"Estimación de Pi (serial): {pi_serial_estimate}")
    print(f"Estimación de Pi (apply_async): {pi_apply_async_estimate}")
    print(f"Estimación de Pi (apply_async_chunked): {pi_apply_async_chunked_estimate}")