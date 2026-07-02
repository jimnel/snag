from scipy.sparse import coo_array

def kinetic_1d_element(b):
    n_sites = len(b)
    coupling = []
    signs = []
    for j in range(n_sites-1):
        if b[j] != b[j+1]:
            coupling.append(b[:j]+b[j+1]+b[j]+b[j+2:])
            signs.append(-1)
    if b[0] != b[-1]:
        coupling.append(b[-1] + b[1:-1] + b[0])
        s_fac = b[1:-1].count("1")+1
        signs.append((-1)**s_fac)
    return coupling, signs


def kinetic_1d(basis):
    row = []
    col = []
    data = []

    for b_i in basis:
        coupling, signs = kinetic_1d_element(b_i)
        row += [basis[b_i]]*len(signs)
        col += [basis[c] for c in coupling]
        data += signs

    return coo_array((data, (row, col))).toarray()
