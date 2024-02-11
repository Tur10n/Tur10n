lp_y = int(input(print("Please enter the year you would like to check:")))
if (lp_y % 4 == 0 and lp_y % 100 != 0) or lp_y % 400 == 0 :
    print(f"The entered year {lp_y} is an leap year.")
else :
    print(f"The entered year {lp_y} is not leap year.")