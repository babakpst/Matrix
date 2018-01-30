
#####################################################################
# Code developed by: Dr. Babak Poursartip
# Supervised by:     Dr. Clint Dawson
# The Institute for Computational Engineering and Sciences (ICES)
# The University of Texas at Austin
#
# Start date:    01/22/2018
# Latest update: 01/22/2018
#
# Comment: This class specifies the shape functions
#
#####################################################################

class Mass_Matrix_Class:

    def __int__(self):
        pass


    def Mass_2D_4N_def(self,
                   IEL, NNode, NDim, NInt,                   # ! Integer Variables
                   Rho,                                      # ! Real Variables
                   XT, ME,                                   # ! Real Arrays
                   XINT, WINT                                # ! Type 
                   ):

        # Import built-in libraries ================================================================
        import numpy as np

        # Import user-defined modules ==============================================================
        import Parameters_Class


        def matrixmult_def(A, B):

            import numpy as np

            #C = [[0 for row in range(len(A))] for col in range(len(B[0]))]
            C = np.zeros( (len(A),len(B)), dtype=np.float64)
            print(C)
            print(len(A))
            print(len(B))
            
            for i in range(len(A)):
                for j in range(len(B[0])):
                    for k in range(len(B)):
                        print("i=", i, "j=", j,"k=", k)
                        C[i][j] += A[i][k]*B[k][j]

            print(" Multiplication is done.")
            return C

        # Define arrays ============================================================================
        DJ        = np.zeros((NDim, NDim),   dtype=np.float64)  # Jacobian matrix in the local coordinates
        DJI       = np.zeros((NDim, NDim),   dtype=np.float64)  # Jacobian inverse matrix
        DFX       = np.zeros((NNode, NDim),  dtype=np.float64)  # Jacobian matrix in the global coordinates
        DFXI      = np.zeros((NNode, NDim),  dtype=np.float64)  # Jacobian matrix in the global coordinates
        Phi_Phi_T = np.zeros((NNode, NNode), dtype=np.float64)  # 
        FN        = np.zeros(NNode, dtype=np.float64)           # Shape function array

        # Code =====================================================================================
        ShapeFunc = Parameters_Class.Shape_Function_Class()

        # Integrate over integration points
        for LY in range(NInt):

            X2  = XINT[LY]
            WY  = WINT[LY]

            for LX in range(NInt):
                X1  = XINT[LX]
                WX  = WINT[LX]

                WSTAR  = WX * WY

                # SHAPE FUNCTIONS AND DIFFERENTIAL OF SHAPE FUNCTIONS
                ShapeFunc.Shape_Func_2D_4N_def(FN, X1, X2)
                ShapeFunc.Derivative_Shape_Func_2D_4N_def(DFXI, X1, X2)

                DJ   = matrixmult_def(XT, DFXI)

                DETJ = DJ[0][0] * DJ[1][1] - DJ[1][0] * DJ[0][1]
                FAC  = WSTAR * DETJ

                if DETJ <= 0.0:
                    print("{} {:d} {} {:d}".format(" Fatal error: The Jacobian for element ", IEl, " is negative: ", DETJ))

                # Calculating the Jacobian Inverse
                DJI[0][0] =   DJ[1][1]
                DJI[1][1] =   DJ[0][0]
                DJI[0][1] = - DJ[0][1]
                DJI[1][0] = - DJ[1][0]

                DJI = DJI  / DETJ 

                DFX = matrixmult_def(DFXI,DJI) 

                for I in range(NNode):
                    for J in range(NNode):
                        Phi_Phi_T[I][J] = FN[I] * FN[J] * FAC

                # Element mass matrix <Modify>
                for IDim in range(NDim):
                    for INode in range(NNode):
                      for JNode in range(NNode):
                        ME[IDim*NNode+INode][IDim*NNode+JNode] += Rho * Phi_Phi_T[INode][JNode]

    def Mass_2D_3N_def(self):
        pass

