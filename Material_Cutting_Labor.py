#  CONSTANTS
load_roll_personel = input("Load Roll Personel: ");
cutting_personel = input("Cutting Personel: ");
kitting_personel = input("Kitting Personel: ")
clean_up_personel = input("Clean Up Personel: ")


unit_time_load_roll = input("What is the unit time for the Load Roll in minutes? ")
unit_time_load_roll = unit_time_load_roll / 60.0;
unit_time_kitting = input("What is the unit time for the Kitting in minutes? ")
unit_time_kitting = unit_time_load_roll / 60.0;

machine_rate_cutting = input("Machine Rate (sq yd/hr): ")
clean_rate_clean_up = input("Clean Rate(sq yd/hr): ")

"""INTERMEDIATE CALCULATIONS"""
"""These were found in the BOM spreadsheet of this excel document"""
"""from BOM import weight_mat; # lbs
from BOM import weight_cdb; # lbs
from BOM import weight_elt; # lbs
from BOM import weight_carbon; # lbs
from BOM import weight_saertex; # lbs
from BOM import area_mat; # sq yd
from BOM import area_cdb; # sq yd
from BOM import area_elt; # sq yd
from BOM import area_carbon; # sq yd
from BOM import area_saertex; # sq yd"""
from BOM import *
#    These were found in the Specs spreadsheet of this excel document
scrap_mat = 20.0;
scrap_cdb = 15.0;
scrap_elt = 5.0;
scrap_carbon = 5.0;
scrap_saertex = 15.0;
#    These were found in the Materials spreadsheet of this excel document
roll_area_mat = 474.1;
roll_area_cdb = 195.1;
roll_area_elt = 29.2;
roll_area_carbon = 32.0;
roll_area_saertex = 179.3;

roll_weight_mat = input("Typical Roll wt 3/4oz Mat: ");
roll_weight_cdb = input("Typical Roll wt CDB340: ");
roll_weight_elt = input("Typical Roll wt ELT-5500: ");
roll_weight_carbon = input("Typical Roll wt Carbon Uni: ");
roll_weight_saertex = input("Typical Roll wt Saertex +/-45: ");

ply_area_mat = area_mat + (area_mat * scrap_mat * .01);
ply_area_cdb = area_cdb + (area_cdb * scrap_cdb * .01);
ply_area_elt = area_elt + (area_elt * scrap_elt * .01);
ply_area_carbon = area_carbon + (area_carbon * scrap_carbon * .01);
ply_area_saertex = area_saertex + (area_saertex * scrap_saertex * .01);

per_blade_mat = (weight_mat + (weight_mat * scrap_mat * .01)) / roll_weight_mat;
per_blade_cdb = (weight_cdb + (weight_cdb * scrap_cdb * .01)) / roll_weight_cdb;
per_blade_elt = (weight_elt + (weight_elt * scrap_elt * .01)) / roll_weight_elt;
per_blade_carbon = (weight_carbon + (weight_carbon * scrap_carbon * .01)) / roll_weight_carbon;
per_blade_saertex = (weight_saertex + (weight_saertex * scrap_saertex * .01)) / roll_weight_saertex;

# LABOR AND CYCLE TIMES
mat_roll = per_blade_mat;
cut_station_mat = raw_input("Is the 3/4oz Mat cut at the station? Y or N: ");
if cut_station_mat in ['Y', 'y', 'yes', 'YES']:
    if mat_roll > int(mat_roll):
        mat_roll = int(mat_roll) + 1;
else:
    mat_roll = 0;

cdb_roll = per_blade_cdb;
cut_station_cbd = raw_input("Is the CDB340 cut at the station? Y or N: ");
if cut_station_cbd in ['Y', 'y', 'yes', 'YES']:
    if cdb_roll > int(cdb_roll):
        cdb_roll = int(cdb_roll) + 1;
else:
    cdb_roll = 0;

elt_roll = per_blade_elt;
cut_station_elt = raw_input("Is the ELT-5500 cut at the station? Y or N: ");
if cut_station_elt in ['Y', 'y', 'yes', 'YES']:
    if elt_roll > int(elt_roll):
        elt_roll = int(elt_roll) + 1;
else:
    elt_roll = 0;

carbon_roll = per_blade_carbon;
cut_station_carbon = raw_input("Is the Carbon Uni cut at the station? Y or N: ");
if cut_station_carbon in ['Y', 'y', 'yes', 'YES']:
    if carbon_roll > int(carbon_roll):
        carbon_roll = int(carbon_roll) + 1;
else:
    carbon_roll = 0;

saertex_roll = per_blade_saertex;
cut_station_saertex = raw_input("Is the Saertex +/-45 cut at the station? Y or N: ");
if cut_station_saertex in ['Y', 'y', 'yes', 'YES']:
    if saertex_roll > int(saertex_roll):
        saertex_roll = int(saertex_roll) + 1;
else:
    saertex_roll = 0;

rolls_to_load = mat_roll + cdb_roll + elt_roll + carbon_roll + saertex_roll;

prep_mat_labor = load_roll_personel * unit_time_load_roll * mat_roll;
prep_cdb_labor = load_roll_personel * unit_time_load_roll * cdb_roll;
prep_elt_labor = load_roll_personel * unit_time_load_roll * elt_roll;
prep_carbon_labor = load_roll_personel * unit_time_load_roll * carbon_roll;
prep_saertex_labor = load_roll_personel * unit_time_load_roll * saertex_roll;


prep_mat_cycle = unit_time_load_roll * mat_roll;
prep_cdb_cycle = unit_time_load_roll * cdb_roll;
prep_elt_cycle = unit_time_load_roll * elt_roll;
prep_carbon_cycle = unit_time_load_roll * carbon_roll;
prep_saertex_cycle = unit_time_load_roll * saertex_roll;

if cut_station_mat in ['Y', 'y', 'yes', 'YES']:
    cutting_mat_labor = (ply_area_mat / machine_rate_cutting) * cutting_personel;
else:
    cutting_mat_labor = 0;
if cut_station_cbd in ['Y', 'y', 'yes', 'YES']:
    cutting_cdb_labor = (ply_area_cdb / machine_rate_cutting) * cutting_personel;
else:
    cutting_cdb_labor = 0;
if cut_station_elt in ['Y', 'y', 'yes', 'YES']:
    cutting_elt_labor = (ply_area_elt / machine_rate_cutting) * cutting_personel;
else:
    cutting_elt_labor = 0;
if cut_station_carbon in ['Y', 'y', 'yes', 'YES']:
    cutting_carbon_labor = (ply_area_carbon / machine_rate_cutting) * cutting_personel;
else:
    cutting_carbon_labor = 0;
if cut_station_saertex in ['Y', 'y', 'yes', 'YES']:
    cutting_saertex_labor = (ply_area_saertex / machine_rate_cutting) * cutting_personel;
else:
    cutting_saertex_labor = 0;

cutting_mat_cycle = cutting_mat_labor / cutting_personel;
cutting_cdb_cycle = cutting_cdb_labor / cutting_personel;
cutting_elt_cycle = cutting_elt_labor / cutting_personel;
cutting_carbon_cycle = cutting_carbon_labor / cutting_personel;
cutting_saertex_cycle = cutting_saertex_labor / cutting_personel;

kitting_mat_labor = cutting_mat_cycle * kitting_personel;
kitting_cdb_labor = cutting_cdb_cycle * kitting_personel;
kitting_elt_labor = cutting_elt_cycle * kitting_personel;
kitting_carbon_labor = cutting_carbon_cycle * kitting_personel;
kitting_saertex_labor = cutting_saertex_cycle * kitting_personel;

kitting_mat_cycle = 0;
kitting_cdb_cycle = 0;
kitting_elt_cycle = 0;
kitting_carbon_cycle = 0;
kitting_saertex_cycle = 0;

if cut_station_mat in ['Y', 'y', 'yes', 'YES']:
    clean_up_mat_labor = (ply_area_mat - area_mat) / clean_rate_clean_up;
else:
    clean_up_mat_labor = 0;
if cut_station_cbd in ['Y', 'y', 'yes', 'YES']:
    clean_up_cdb_labor = (ply_area_cdb - area_cdb) / clean_rate_clean_up;
else:
    clean_up_cdb_labor = 0;
if cut_station_elt in ['Y', 'y', 'yes', 'YES']:
    clean_up_elt_labor = (ply_area_elt - area_elt) / clean_rate_clean_up;
else:
    clean_up_elt_labor = 0;
if cut_station_carbon in ['Y', 'y', 'yes', 'YES']:
    clean_up_carbon_labor = (ply_area_carbon - area_carbon) / clean_rate_clean_up;
else:
    clean_up_carbon_labor = 0;
if cut_station_saertex in ['Y', 'y', 'yes', 'YES']:
    clean_up_saertex_labor = (ply_area_saertex - area_saertex) / clean_rate_clean_up;
else:
    clean_up_saertex_labor = 0;

clean_up_mat_cycle = clean_up_mat_labor / clean_up_personel;
clean_up_cdb_cycle = clean_up_cdb_labor / clean_up_personel;
clean_up_elt_cycle = clean_up_elt_labor / clean_up_personel;
clean_up_carbon_cycle = clean_up_carbon_labor / clean_up_personel;
clean_up_saertex_cycle = clean_up_saertex_labor / clean_up_personel;

prep_labor_hours = prep_mat_labor + prep_cdb_labor + prep_elt_labor + prep_carbon_labor + prep_saertex_labor;
prep_cycle_hours = prep_mat_cycle + prep_cdb_cycle + prep_elt_cycle + prep_carbon_cycle + prep_saertex_cycle;
cutting_labor_hours = cutting_mat_labor + cutting_cdb_labor + cutting_elt_labor + cutting_carbon_labor + cutting_saertex_labor;
cutting_cycle_hours = cutting_mat_cycle + cutting_cdb_cycle + cutting_elt_cycle + cutting_carbon_cycle + cutting_saertex_cycle;
kitting_labor_hours = kitting_mat_labor + kitting_cdb_labor + kitting_elt_labor + kitting_carbon_labor + kitting_saertex_labor;
kitting_cycle_hours = kitting_mat_cycle + kitting_cdb_cycle + kitting_elt_cycle + kitting_carbon_cycle + kitting_saertex_cycle;
clean_up_labor_hours = clean_up_mat_labor + clean_up_cdb_labor + clean_up_elt_labor + clean_up_carbon_labor + clean_up_saertex_labor;
clean_up_cycle_hours = clean_up_mat_cycle + clean_up_cdb_cycle + clean_up_elt_cycle + clean_up_carbon_cycle + clean_up_saertex_cycle;

total_cutting_labor = prep_labor_hours + cutting_labor_hours + kitting_labor_hours + clean_up_labor_hours;
total_cutting_cycle_time = prep_cycle_hours + cutting_cycle_hours + kitting_cycle_hours + clean_up_cycle_hours;

# TOTALS
print("Rolls to Load:")
print(rolls_to_load)
print("Loading and Machine Prep Labor Hours:")
print(prep_labor_hours)
print("Loading and Machine Prep Cycle Time:")
print(prep_cycle_hours)
print("Cutting Labor Hours:")
print(cutting_labor_hours)
print("Cutting Cycle Time:")
print(cutting_cycle_hours)
print("Kitting Labor Hours:")
print(kitting_labor_hours)
print("Kitting Cycle Time:")
print(kitting_cycle_hours)
print("Clean-up Labor Hours:")
print(clean_up_labor_hours)
print("Clean-up Cycle Time:")
print(clean_up_cycle_hours)
print("Total Material Cutting Labor:")
print(total_cutting_labor)
print("Total Material Cutting Cycle Time:")
print(total_cutting_cycle_time)