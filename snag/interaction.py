import numpy as np
# from scipy.sparse import diags_array

def nn_int_element(b):
    n_sites = len(b)
    nn_ints = 0
    for j in range(n_sites-1):
        if (b[j]=="1") and (b[j+1] == "1"):
            nn_ints += 1
    if (b[0] == "1") and (b[-1] == "1"):
        nn_ints += 1
    return nn_ints


def nn_int(basis):
    u_arr = [nn_int_element(b_i) for b_i in basis]
    return np.array(u_arr)