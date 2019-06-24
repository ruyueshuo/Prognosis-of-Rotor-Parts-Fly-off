#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/24 17:47
# @Author  : FengDa
# @File    : feature_extract.py
# @Software: PyCharm
import glob
import math
import os
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats


def extract_time_feature(data):
    """
    获取时域特征。
    :param data: np.array.时域信号
    :return: timeFeatList: 时域特征
    """
    dfMean = np.mean(data)  # 均值
    dfVar = np.var(data)  # 方差
    dfStd = np.std(data)  # 标准差
    dfRMS = math.sqrt(pow(dfMean, 2) + pow(dfStd, 2))  # 均方根
    dataSorted = np.sort(np.abs(data))
    dfPeak = np.mean(dataSorted[-10:])
    dfSkew = stats.skew(data)  # 偏度
    dfKurt = stats.kurtosis(data)  # 峭度
    dfPeakFactor = dfPeak / dfRMS  # 峰值因子
    dfPulseFactor = dfPeak / np.mean(np.abs(data))  # 脉冲因子

    timeFeatList = [dfMean, dfVar, dfRMS, dfPeak, dfSkew, dfKurt, dfPeakFactor, dfPulseFactor]
    timeFeatName = ['Mean', 'Var', 'RMS', 'Peak', 'Skew', 'Kurt', 'PeakFactor', 'PulseFactor']
    return timeFeatList, timeFeatName


def generate_FFT(y, Fs):
    '''
    对时域信号通过快速傅立叶变化，产生频域信号。
    :param y: ndarray. 原始时域信号。
    :param Fs: float. 采样频率。
    :param date: str. 采样的时间戳。
    :param description: list.风机，对应的测点，采样频率等信息，用于画图显示
    :return: frq: list, 频率
            abs(Y): list, 幅值
    '''

    n = len(y)  # 时域信号的长度
    k = np.arange(n) / n  # （n-1）/n
    frq1 = Fs * k  # 两侧的频率范围
    frq = frq1[range(int(n / 2))]  # 一侧的频率范围

    Y1 = np.fft.fft(y)  # FFT计算
    Y2 = Y1 / n  # fft归一化
    Y = Y2[range(int(n / 2))]  # 一侧频率对应的振幅

    return frq, abs(Y)  # 返回频率和对应幅值