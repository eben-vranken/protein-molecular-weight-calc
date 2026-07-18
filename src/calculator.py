amino_weights = {
    "A": 71.08,
    "R": 156.19,
    "N": 114.10,
    "D": 115.09,
    "C": 103.14,
    "Q": 128.13,
    "E": 129.12,
    "G": 57.05,
    "H": 137.14,
    "I": 113.16,
    "L": 113.16,
    "K": 128.17,
    "M": 131.20,
    "F": 147.18,
    "P": 97.12,
    "S": 87.08,
    "T": 101.11,
    "W": 186.21,
    "Y": 163.18,
    "V": 99.13,
}


def weigh_sequence(sequence):
    weight = 0

    for c in sequence:
        weight += amino_weights[c]

    return weight