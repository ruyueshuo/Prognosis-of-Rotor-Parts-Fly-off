#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/24 17:21
# @Author  : FengDa
# @File    : data_import.py
# @Software: PyCharm
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from data_process.feature_extract import extract_time_feature, generate_FFT

train_path = "F:/Competition/Prognosis of Rotor Parts Fly-off/data/training_data/training_data"
device_list = os.listdir(train_path)
for device in device_list:
    device_path = train_path + '/' + device
    process_list = os.listdir(device_path)
    for process in process_list:
        process_path = device_path + '/' + process
        component_list = os.listdir(process_path)
        for component in component_list:
            component_path = process_path + '/' + component
            file_list = os.listdir(component_path)
            cols = ['Mean', 'Var', 'RMS', 'Peak', 'Skew', 'Kurt', 'PeakFactor', 'PulseFactor']
            time_feature = pd.DataFrame(columns=cols)
            for file in file_list:
                print(file)
                file_path = component_path + '/' + file
                with open(file_path, 'r') as f:
                    data = f.readlines()
                    freq = np.float(data[0].split(',')[1])
                    cycles = np.int(data[1].split(',')[1])
                    type = data[2].split(',')[1]
                    speed = np.int(data[3].split(',')[1])
                    samples = np.int(data[4].split(',')[1])
                    wave = np.array(data[5].split(',')[1:]).astype(np.float)
                    timeFeatList, timeFeatName = extract_time_feature(wave)
                    index = np.int(file[5:-4])
                    time_feature.loc[index] = timeFeatList
            time_feature.sort_index(inplace=True)
            result_path = "F:/Competition/Prognosis of Rotor Parts Fly-off/data/feature/train/"
            time_feature.to_csv("{}{}/{}_{}_{}.csv".format(result_path, device, process, component, index))
            # print('1')
                    # fig = plt.figure(figsize=(12, 6))
                    # plt.plot(wave)
                    # plt.show()
                    # plt.close()
                    # print('Finishu')
                    # for line in

print("Finish..")