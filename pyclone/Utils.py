import numpy as np
import pandas as pd
import dill as pickle

#################
# Function Town #
#################
def unique_tuples(seq, l=4):
    ''' Takes string of nucleic acids as input. Returns all tuples of length l.
    Useful for converting sequences into sets of overhangs (e.g., golden gate
    assembly)

    Parameters
    ----------
    seq : str or 1darray
        DNA sequence to convert to str tuples
    l : int
        length of overhangs
    Returns
    -------
    overhangs : set
        set of unique tuples of length l in seq
    '''
    return set([seq[i+l] for i in range(len(x) - l + 1)])

##############
# Class Town #
##############
