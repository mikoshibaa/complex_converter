from complex_converter import ComplexConverter
import numpy as np

if __name__ == "__main__":

    
    converter = ComplexConverter()



    z = np.array([
        [
            [1 + 2j],
            [3 + 4j]
        ]
    ])
    print("z:{}".format(z))

    z_CtoR = converter.CtoR(z)
    print("z_CtoR:{}".format(z_CtoR))

    z_RtoC = converter.RtoC(z_CtoR)
    print("z_RtoC:{}".format(z_RtoC))
    
    A = np.array([
        [
            [1 + 2j, 3 + 4j],
            [5 + 6j, 7 + 8j]
        ],
        [
            [9 + 10j, 11 + 12j],
            [13 + 14j, 15 + 16j]
        ]
    ])
    print("A:{}".format(A))

    A_CtoR = converter.CtoR(A)
    print("A:{}".format(A_CtoR))

    A_RtoC = converter.RtoC(A_CtoR)
    print("A_RtoC:{}".format(A_RtoC))
    