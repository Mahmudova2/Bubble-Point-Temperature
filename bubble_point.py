import math

def bubble_point(x_benzene, total_pressure):
    # Antoine constants for Benzene
    A_Ben = 13.7819
    B_Ben = 2726.81
    C_Ben = 217.572

    # Antoine constants for Toluene
    A_Tol = 13.9320
    B_Tol = 3056.96
    C_Tol = 217.625

    diff_dict = {}

    for T in range(1, 201):
        p_sat_ben = math.exp(A_Ben - (B_Ben / (C_Ben + T)))
        p_sat_tol = math.exp(A_Tol - (B_Tol / (C_Tol + T)))

        calculated_pressure = (x_benzene * p_sat_ben) + (1 - x_benzene) * p_sat_tol

        diff = calculated_pressure - total_pressure
        diff_dict[T] = abs(diff)

    Tb = min(diff_dict, key=diff_dict.get)
    return Tb


Tb = bubble_point(0.5, 101.325)
print("Bubble Point Temperature =", Tb)