#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/24 18:49
# @Author  : FengDa
# @File    : feature_explore.py
# @Software: PyCharm
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
feature_path = "F:/Competition/Prognosis of Rotor Parts Fly-off/data/feature/train/"
device_list = os.listdir(feature_path)
for device in device_list:
    device_path = feature_path + '/' + device
    file_list = os.listdir(device_path)
    component_list = [file[4:] for file in file_list]
    component_list = np.unique(component_list)
    for component in component_list:
        component_df = pd.DataFrame()
        for file in file_list:
            if file[4:] == component:
                data = pd.read_csv(device_path + '/' + file)
                component_df = component_df.append(data)
        component_df = component_df.reset_index(drop=True)
        for col in component_df.columns.tolist():
            fig = plt.figure(figsize=(12, 6))
            plt.plot(component_df[col])
            plt.title(col)
            plt.show()
            plt.close()
        print('1')