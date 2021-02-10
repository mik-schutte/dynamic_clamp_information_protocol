'''
    plotter.py

    visualises one of the .csv files in the results folder that
    have been generated by the main.py code.
'''
import numpy as np
import matplotlib.pyplot as plt
import os
from brian2.units.stdunits import mV, ms, mS, uA

def plot_dynamicclamp(statemon, g_exc, g_inh, hiddenstate):
    '''Plots the injected conductance and voltage trace.
    '''
    fig, axs = plt.subplots(3, figsize=(12,12))
    fig.suptitle('Dynamic Clamp')
    axs[0].plot(statemon.t/ms, g_exc(statemon.t)/mS, c='red')
    axs[0].set(ylabel='Exc. conductance [mS]')

    axs[1].plot(statemon.t/ms, g_inh(statemon.t)/mS, c='blue')
    axs[1].set(ylabel='Inh. conductance [mS]')

    for idx, val in enumerate(hiddenstate):
        if val == 1:
            axs[2].axvline(idx*0.2, c='lightgray')
    axs[2].plot(statemon.t/ms, statemon.v[0].T/mV, c='black')
    axs[2].set(ylabel='Voltage [mV]', xlabel='Time [ms]')
    plt.show()
    return

def plot_currentclamp(statemon, hiddenstate):
    '''Plots the injected current and voltage trace
    '''
    fig, axs = plt.subplots(2, figsize=(12,12))
    fig.suptitle('Current Clamp')
    axs[0].plot(statemon.t/ms, statemon.I_inj[0]/uA, c='red')
    axs[0].set(ylabel='Input current [uA]')

    for idx, val in enumerate(hiddenstate):
        if val == 1:
            axs[1].axvline(idx*0.2, c='lightgray')
    axs[1].plot(statemon.t/ms, statemon.v[0].T/mV, c='black')
    axs[1].set(ylabel='Voltage [mV]', xlabel='Time [ms]')
    plt.show()
    return

def plot_compare(dynamic_statemon, current_statemon, hiddenstate):
    '''Compares the dynamic voltage trace and current voltage trace.
    '''
    fig, axs = plt.subplots(2, figsize=(12,12))
    fig.suptitle('Comparison between Dynamic and Current Clamp', y=0.95)

    for idx, val in enumerate(hiddenstate):
        if val == 1:
            axs[0].axvline(idx*0.2, c='lightgray')
    axs[0].title.set_text('Dynamic Clamp')
    axs[0].plot(dynamic_statemon.t/ms, dynamic_statemon.v[0].T/mV, c='black')
    axs[0].set(ylabel='Voltage [mV]', xlabel='Time [ms]')

    for idx, val in enumerate(hiddenstate):
        if val == 1:
            axs[1].axvline(idx*0.2, c='lightgray')
    axs[1].title.set_text('Current Clamp')
    axs[1].plot(current_statemon.t/ms, current_statemon.v[0].T/mV, c='black')
    axs[1].set(ylabel='Voltage [mV]', xlabel='Time [ms]')
    plt.show()
    return