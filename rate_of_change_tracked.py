import numpy as np
import pandas as pd
import os
import out_process as op

### Convert rate of change of tracked components files to csv files (unit: molecules/cc.s (air) & ppb)
path = r'C:\Users\janet\Documents\nBox\0. SOAFP-PyCHAM output\PR3_simulation\Simulation results\20Nov_1700_1759_89VOCs_20bins'
os.chdir(path)
directories = os.listdir(path)

factor = op.factor
file_list = []
for file in directories:
    if "_rate_of_change" in file:
        rate_of_change = open(file, "r+")
        rate_of_change = rate_of_change.readlines()
        rate_of_change = np.array([rate_of_change[i].split(",") for i in range(1, len(rate_of_change))])
        rate_of_change = rate_of_change.astype(float)
        for j in range(len(rate_of_change[0])):
            rate_of_change[0][j] = rate_of_change[0][j] + 1

        # number concentration, unit: molecules/cc.s (air)
        rate_of_change_number = rate_of_change
        rate_of_change_number = rate_of_change_number.transpose()
        rate_of_change_number_with_sum = np.empty([len(rate_of_change_number), len(rate_of_change_number[0]) + 1])
        sum_time = np.sum(rate_of_change_number[:, 1:], axis=0)
        sum_time = np.concatenate((np.array([" "]), sum_time))
        sum_time = np.concatenate((sum_time, np.array([" "])))
        for i in range(len(rate_of_change_number)):
            rate_of_change_number_with_sum[i] = np.append(rate_of_change_number[i],
                                                          np.sum(rate_of_change_number[i][1:]))
        rate_of_change_number_with_sum = np.vstack((rate_of_change_number_with_sum, sum_time))
        pd.DataFrame(rate_of_change_number_with_sum).to_csv(file + " (molecules.(cc.s (air)).\u207B\u00b9).csv", index=False,
                                                   header=False)

        # ppb
        rate_of_change_ppb = rate_of_change
        rate_of_change_ppb[1:] = (rate_of_change_ppb[1:].transpose() / factor[:-1]).transpose()
        rate_of_change_ppb = rate_of_change_ppb.transpose()
        rate_of_change_ppb_with_sum = np.empty([len(rate_of_change_ppb), len(rate_of_change_ppb[0]) + 1])
        sum_time = np.sum(rate_of_change_ppb[:, 1:], axis=0)
        sum_time = np.concatenate((np.array([" "]), sum_time))
        sum_time = np.concatenate((sum_time, np.array([" "])))
        for i in range(len(rate_of_change_ppb)):
            rate_of_change_ppb_with_sum[i] = np.append(rate_of_change_ppb[i], np.sum(rate_of_change_ppb[i][1:]))
        rate_of_change_ppb_with_sum = np.vstack((rate_of_change_ppb_with_sum, sum_time))
        pd.DataFrame(rate_of_change_ppb_with_sum).to_csv(file + " rate of change (ppb.s\u207B\u00b9).csv", index=False,
                                                header=False)
