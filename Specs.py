from User_Input import *

def HP_LP_Skin_Laminate_Pattern_Areas(user_area, shape_factor, flange_length, flange_width):
    area = (user_area * shape_factor) + (flange_length * (flange_width/1000.))
    return area


"""entire_surface_no_flanges_area1 = input("Area(sq m) of Entire Surface (w/out flanges): ");
entire_surface_no_flanges_shape_factor = input("Shape Factor of Entire Surface (w/out flanges): ");
entire_surface_no_flanges_area = entire_surface_no_flanges_area1 * entire_surface_no_flanges_shape_factor;"""
entire_surface_without_flanges_area = HP_LP_Skin_Laminate_Pattern_Areas(entire_surface_without_flanges_user_area, entire_surface_without_flanges_shape_factor,
                                                                     entire_surface_without_flanges_flange_length,entire_surface_without_flanges_flange_width)
print("Area(sq m) of Entire Surface (w/out flanges): ")
print(entire_surface_without_flanges_area);
"""entire_surface_flanges_area1 = input("Area(sq m) of Entire Surface with flanges: ");
entire_surface_flanges_shape_factor = input("Shape Factor of Entire Surface with flanges: ");
entire_surface_flanges_length = input("Flange Length(m) of Entire Surface: ");
entire_surface_flanges_width = input("Flange Width(mm) of Entire Surface: ");
entire_surface_flanges_area = (entire_surface_flanges_area1 * entire_surface_flanges_shape_factor) +\
                              (entire_surface_flanges_length * .001 * entire_surface_flanges_width)"""
entire_surface_with_flanges_area = HP_LP_Skin_Laminate_Pattern_Areas(entire_surface_with_flanges_user_area, entire_surface_with_flanges_shape_factor,
                                                                     entire_surface_with_flanges_flange_length,entire_surface_with_flanges_flange_width)
print("Area(sq m) of Entire Surface with flanges: ")
print(entire_surface_with_flanges_area)

fwd_balsa1_user_area = input("Area of Fwd Balsa #1: ");
fwd_balsa1_shape_factor = input("Shape Factor of Fwd Balsa #1: ");
fwd_balsa1_area = fwd_balsa1_user_area * fwd_balsa1_shape_factor;
print("Area(sq m) of Fwd Panel Balsa #1: ")
print(fwd_balsa1_area)
fwd_balsa2_user_area = input("Area of Fwd Balsa #2: ");
fwd_balsa2_shape_factor = input("Shape Factor of Fwd Balsa #2: ");
fwd_balsa2_area = fwd_balsa2_user_area * fwd_balsa2_shape_factor;
print("Area(sq m) of Fwd Panel Balsa #2: ")
print(fwd_balsa2_area)
fwd_balsa3_user_area = input("Area of Fwd Balsa #3: ");
fwd_balsa3_shape_factor = input("Shape Factor of Fwd Balsa #3: ");
fwd_balsa3_area = fwd_balsa3_user_area * fwd_balsa3_shape_factor;
print("Area(sq m) of Fwd Panel Balsa #3: ")
print(fwd_balsa3_area)

aft_balsa1_user_area = input("Area of Aft Balsa #1: ");
aft_balsa1_shape_factor = input("Shape Factor of Aft Balsa #1: ");
aft_balsa1_area = aft_balsa1_user_area * aft_balsa1_shape_factor;
print("Area(sq m) of Aft Panel Balsa #1: ")
print(aft_balsa1_area)
aft_balsa2_user_area = input("Area of Aft Balsa #2: ");
aft_balsa2_shape_factor = input("Shape Factor of Aft Balsa #2: ");
aft_balsa2_area = aft_balsa2_user_area * aft_balsa2_shape_factor;
print("Area(sq m) of Aft Panel Balsa #2: ")
print(aft_balsa2_area)
aft_balsa3_user_area = input("Area of Aft Balsa #3: ");
aft_balsa3_shape_factor = input("Shape Factor of Aft Balsa #3: ");
aft_balsa3_area = aft_balsa3_user_area * aft_balsa3_shape_factor;
print("Area(sq m) of Aft Panel Balsa #3: ")
print(aft_balsa3_area)

tip_mat_user_area = input("Area(sq m) of Tip Mat: ")
tip_mat_shape_factor = input("Shape Factor of Tip Mat: ")
tip_mat_area = tip_mat_user_area * tip_mat_shape_factor;
print("Area(sq m) of Tip Mat")
print(tip_mat_area)