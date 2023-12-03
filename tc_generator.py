import random

def get_data(size) -> (set, list, list):
    U = set(range(1, size + 1))
    S = []
    covered = set() 
    max_list_size = size // 200
    while len(S) < max_list_size or covered != U:  
        temp = list(set(random.sample(U, random.randint(1, size))))
        S.append(temp)
        covered.update(temp)
    C = [random.randint(1, 100) for _ in range(len(S))]
    return U, S, C

def save_to_txt(file_path, U, S, C):
    with open(file_path, 'w') as file:
        file.write(f"m = {len(U)}\n")
        file.write(f"S = {S}\n")
        file.write(f"P = {C}\n")

if __name__ == "__main__":
    size = 2000  # Ganti dengan ukuran yang diinginkan
    U, S, C = get_data(size)
    save_to_txt("test_data_{0}.txt".format(size), U, S, C)
