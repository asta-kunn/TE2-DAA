__author__ = "Andrea Rubbi"
import time
import tracemalloc


def set_cover(universe, subsets,costs):
    cost=0
    elements = set(e for s in subsets for e in s)
    if elements != universe:
        return None
    covered = set()
    cover = []
    while covered != elements:
        subset = max(subsets, key=lambda s: len(s - covered)/costs[subsets.index(s)])
        cover.append(subset)
        cost+=costs[subsets.index(subset)]
        covered |= subset
 
    return cover, cost
 

def main(input_file, z=time.time()):
    tracemalloc.clear_traces()  # Me-reset pemantauan memori
    tracemalloc.start()  # Memulai pemantauan memori
    try:
        with open(input_file, 'r') as file:
            content = file.readlines()

        m = int(content[0].split('=')[1].strip())
        S = eval(content[1].split('=')[1].strip())
        P = eval(content[2].split('=')[1].strip())

        universe = set(range(1, m+1))
        subsets = [set(x) for x in S]

        result = set_cover(universe, subsets, P)

        if result is not None:
            cover, cost = result
            print('covering sets= ', cover, '\n',
                  'cost= ', cost, '$')
            print('time:', time.time() - z)

            # Memantau penggunaan memori
            current, peak = tracemalloc.get_traced_memory()
            print(f"Current memory usage: {(current)} bytes")
            print(f"Peak memory usage: {(peak)} bytes")
        else:
            print("No valid cover found for the given subsets.")
    finally:
        tracemalloc.stop()  # Menghentikan pemantauan memori

if __name__ == "__main__":
    input_file1 = "test_data_20.txt"
    main(input_file1)
    
    input_file2 = "test_data_200.txt"
    main(input_file2)
    
    input_file3 = "test_data_2000.txt"
    main(input_file3)

