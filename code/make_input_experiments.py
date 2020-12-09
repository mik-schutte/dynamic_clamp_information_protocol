'''
    make_input_experiments.py
    ADDITIONAL INFORMATION HERE
''' 
from code.input import Input
import numpy as np
import random

def make_input_experiments(qon_qoff_type, baseline, amplitude_scaling, tau, factor_ron_roff, mean_firing_rate, sampling_rate, duration, seed=None):
    '''Doc
    '''

    np.random.seed(seed)

    # Fixed parameters
    N = 1000
    dt = 1./sampling_rate
    tau_exponential_kernel = 5 #ms
    alpha = np.sqrt(1/8) # relation mean and std of the firing rates of the artificial neurons (firing rates should be positive)
    stdq = alpha*mean_firing_rate
    

    ron = 1./(tau*(1+factor_ron_roff))
    roff = factor_ron_roff*ron

    #Create input from artifical network
    input_bayes = Input()
    input_bayes.dt = dt
    input_bayes.T = duration
    input_bayes.kernel = 'exponential'
    input_bayes.kerneltau = tau_exponential_kernel
    input_bayes.ron = ron
    input_bayes.roff = roff
    input_bayes.seed = seed
    input_bayes.xseed = seed

    if qon_qoff_type == 'normal':
        [input_bayes.qon, input_bayes.qoff] = input_bates.create_qonqoff(mutheta, N, alphan, regime, qseed)
    elif qon_qoff_type == 'balanced':
        [input_bayes.qon, input_bayes.qoff] = input_bayes.create_qonqoff_balanced(N, mean_firing_rate, stdq, seed)
    elif qon_qoff_type == 'balanced_uniform':
        minq = 100
        maxq = 1000
        [input_bayes.qon, input_bayes.qoff] = input_bayes.create_qonqoff_balanced_uniform(N, minq, maxq, seed)
    else: 
        raise SyntaxError('No qon/qoff creation type specified')

    input_bayes.get_all()
    input_bayes.fHandle = input_bayes.markov()
    input_bayes.generate()

    #Scale for experiments
    input_current = amplitude_scaling*input_bayes.input+baseline
    input_theory = input_bayes.input
    hidden_state = input_bayes.x

    return [input_current, input_theory, hidden_state]