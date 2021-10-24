from codegen.constants import MAX_N

if __name__ == "__main__":
    for i in range(2, MAX_N):
        print(f"from typesafe_parmap.parmap import par_map_{i}")
    print("from typesafe_parmap.parmap import par_map_n")
