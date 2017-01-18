#     These were found in the 'LP & HP Skins' spreadsheet of this excel document
area_mat = 24.8;        # sq yd
area_cdb = 8299.0;      # sq yd
area_elt = 881.8;       # sq yd
area_carbon = 1273.3;   # sq yd
area_foam20 = 1103.07;  # sq ft
area_foam40 = 3042.90;  # sq ft

weight_mat = 10.4;      # lbs
weight_cdb = 17013.0;   # lbs
weight_elt = 3020.0;    # lbs
weight_carbon = 3979.1; # lbs
weight_gelcoat = 700.6; # lbs
weight_foam20 = 521.13; # lbs
weight_foam40 = 2875.18;# lbs

weight_hunt_ly = 9803.89;   #lbs
weight_hunt_xp = 2941.17;   #lbs
#
#     These were found in the 'LESW Labor' and 'TESW Labor' spreadsheets of this excel document
area_saertex = 975.5;   # sq yd
area_foam50 = 2073.8;   # sq ft

weight_saertex = 2176.1;    # lbs
weight_foam50 = 2449.37;    # lbs
#
#      These were found in the Bond spreadsheet of this excel document
volume_plexus_a = 40.95;    # gal
volume_plexus_b = 4.10;     # gal

weight_plexus_a = 317.26;   #lbs
weight_plexus_b = 58.69;    #lbs
#
#     These were found in the Specs spreadsheet of this excel document
units_tbolt = 72;       # ea
units_barrel_nut = 72;  # ea
units_lps = 1;          # ea
#
#     These were found in the Consumables spreadsheet of this excel document
units_le_tape = .25;                # rolls
area_peel_ply = 7956.68;            # sq ft
area_non_sanding_peel_ply = 478.96; # sq ft
volume_adhesive_bulk = 5.97;        # gal
units_adhesive_cans = 15.91;        # cans
volume_release_agent = 5.01;        # gal
area_flow_medium = 5569.68;         # sq ft
length_tubing375 = 1008.86;     #ft
length_tubing5 = 1008.86;       #ft
length_tubing625 = 1008.86;     #ft
length_tubing75 = 1008.86;      #ft
length_tubing875 = 1008.86;     #ft
units_flange_tape = 18.00;      #rolls
units_tan_tape = 20.18;         #rolls
units_green_tape = 20.18;       #rolls
volume_white_lightning = 2.77;  #gal
units_hardener = 6.09;          #each
volume_paint = .55;             #gal
#
#     These were found in the Materials spreadsheet of this excel document
unit_cost_mat = 1.58;
unit_cost_cdb = 1.76;
unit_cost_elt = 2.40;
unit_cost_carbon = 16.80;
unit_cost_saertex = 1.85;
unit_cost_gelcoat = 3.28;
unit_cost_foam20 = 1.22;
unit_cost_foam40 = 1.07;
unit_cost_foam50 = 1.45;
unit_cost_hunt_ly = 1.65;
unit_cost_hunt_xp = 3.33;
unit_cost_plexus_a = 49.90;
unit_cost_plexus_b = 49.90;
unit_cost_tbolt = 25.00;
unit_cost_barrel_nut = 12.00;
unit_cost_lps = 2500.00;
unit_cost_le_tape = 576.00;
unit_cost_peel_ply = .18;
unit_cost_non_sanding_peel_ply = .15;
unit_cost_chopped_strand = .98;
unit_cost_adhesive_bulk = 25.60;
unit_cost_adhesive_cans = 6.65;
unit_cost_release_agent = 59.40;
unit_cost_flow_medium = .06;
unit_cost_tubing375 = .07;
unit_cost_tubing5 = .07;
unit_cost_tubing625 = .15;
unit_cost_tubing75 = .19;
unit_cost_tubing875 = .15;
unit_cost_flange_tape = 21.11;
unit_cost_tan_tape = 2.50;
unit_cost_green_tape = 5.50;
unit_cost_chop_fiber = 2.81;
unit_cost_white_lightning = 11.38;
unit_cost_hardener = 1.65;
unit_cost_patch_aid = 5.52;
unit_cost_paint = 56.00;
unit_cost_putty876 = 3.02;
unit_cost_putty880 = 2.81;
unit_cost_putty_catalyst = 3.58;
#
cost_mat = weight_mat * unit_cost_mat;
cost_cdb = weight_cdb * unit_cost_cdb;
cost_elt = weight_elt * unit_cost_elt;
cost_carbon = weight_carbon * unit_cost_carbon;
cost_saertex = weight_saertex * unit_cost_saertex;

print(cost_mat)
print(cost_cdb)
print(cost_elt)
print(cost_carbon)
print(cost_saertex)

