table = 0
max_table = 10

while table <= max_table:
    print(f"Table de {table}: ", end="")
    multiplier = 0
    
    while multiplier <= max_table:
        print(f"{table * multiplier} ", end="")
        multiplier += 1
    
    print("")  
    table += 1
