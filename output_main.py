import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import datetime
from rdkit import Chem
import out_process as op
from SOA_temporal_trends import SOA_insolation
from Contour_SOA_time_sizebin import contour_SOA
from surface_area import surface_for_each_component
from surface_area import surface_for_SOA_total
from compare_simulation_observation import compare
from estimate_potential import estimate_potential


def main(path, time_interval_1, file_name_1, sheet_1, time_column_1, start_time_1, end_time_1, insolation_column,
         resolution, skip_num, SOA_list, time_column_2, start_time_2, end_time_2, time_interval_2, file_name_2,
         sheet_2):
    # path: the path where the user expect to store the results, given by user

    particulate_phase_mass_SOA = op.particulate_phase_mass_SOA
    time = op.time
    bin_number = op.bin_number
    components_number_SOA = op.components_number_SOA
    radius = op.radius
    components_number = op.components_number
    particulate_phase = op.particulate_phase
    particulate_phase_SOA = op.particulate_phase_SOA
    gas_phase_mass_SOA = op.gas_phase_mass_SOA
    total_particulate_mass_species_time_SOA = op.total_particulate_mass_species_time_SOA
    folder_name = op.folder_name

    os.chdir(path)
    SOA_insolation(time_interval_1, file_name_1, sheet_1, time_column_1, start_time_1, end_time_1, insolation_column,
                   particulate_phase_mass_SOA, folder_name)

    contour_SOA(time, bin_number, components_number_SOA, particulate_phase_mass_SOA, resolution)

    surface_for_each_component(radius, components_number, particulate_phase, time, folder_name)

    surface_for_SOA_total(radius, bin_number, components_number_SOA, particulate_phase_SOA, time, folder_name)

    compare(skip_num, SOA_list, time_column_2, start_time_2, end_time_2, particulate_phase_mass_SOA, time_interval_2,
            file_name_2, sheet_2, folder_name)

    estimate_potential(gas_phase_mass_SOA, total_particulate_mass_species_time_SOA, folder_name)

    ### one example:
    # main(r'C:\Users\24979\PycharmProjects\UROP\vacation1', 5, "Meteorology_2020.xlsx", "Our weather station", "Date&Time", "2020-11-19 17:00:00", "2020-11-19 17:55:00",
    # "Solar Radiation (W/m2)", 200, 2, ["MOOOA", "LOOOA", "OOA"], "DateTime", "2020-11-19 17:05:00", "2020-11-19 17:55:00", 10, "5-min SOA.xlsx", "AMS")
