def HP_LP_Skin_Laminate_Pattern_Areas(user_area, shape_factor, flange_length, flange_width):
    area = (user_area * shape_factor) + (flange_length * (flange_width/1000.))
    return area

area1 = HP_LP_Skin_Laminate_Pattern_Areas(213.7,1.2,68.75,150.)
print(area1)