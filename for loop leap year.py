lp = [2020, 2021, 2022, 2023, 2024, 2025, 2026]

for i  in lp:
    if i > 2023:
        print(i)
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0 :
            print(f"The entered year {i} is an leap year.")
        else :
            print(f"The entered year {i} is not leap year.")
    else :
        print("Years under 2023 is not in your range")
         