
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

    def Mass_2D_4N(self,
                   IEL, NNode, NDim, NInt,                \   # ! Integer Variables
                   Rho,                                   \   # ! Real Variables
                   XT, ME,                                \   # ! Real Arrays
                   XINT, WINT                             \   # ! Type 
                   ):

        # Import built-in libraries ================================================================
        import numpy as np

        # Import user-defined modules ==============================================================
        import Parameters_Class

        # Define arrays ============================================================================
        DJ        = np.zeros((NDim, NDim),   dtype=np.float64)  # Jacobian matrix in the local coordinates
        DJI       = np.zeros((NDim, NDim),   dtype=np.float64)  # Jacobian inverse matrix
        DFX       = np.zeros((NNode, NDim),  dtype=np.float64)  # Jacobian matrix in the global coordinates
        Phi_Phi_T = np.zeros((NNode, NNode), dtype=np.float64)  # 

        # Code =====================================================================================
        ShapeFunc = Parameters_Class.Parameters_Class()

        # Integrate over integration points
        for LY in range(NInt):

            X2  = XINT[LY]
            WY  = WINT[LY]

            for LX in range(NInt):
                X1  = XINT[LX]
                WX  = WINT[LX]

                WSTAR  = WX * WY

                # SHAPE FUNCTIONS AND DIFFERENTIAL OF SHAPE FUNCTIONS
                ShapeFunc.Shape_Func_2D_4N(FN, X1, X2)
                ShapeFunc.Derivative_Shape_Func_2D_4N(DFXI, X1, X2)

                DJ   = numpy.matmul( XT, DFXI )

                DETJ = DJ[1][1] * DJ[2][2] - DJ[2][1] * DJ[1][2]
                FAC  = WSTAR * DETJ

                if DETJ <= 0.0:
                    print("{} {:d} {} {:d}".format(" Fatal error: The Jacobian for element ", IEl, " is negative: ", DETJ))

                # Calculating the Jacobian Inverse
                DJI[1][1] =   DJ[2][2]
                DJI[2][2] =   DJ[1][1]
                DJI[1][2] = - DJ[1][2]
                DJI[2][1] = - DJ[2][1]

                DJI = DJI  / DETJ 

                DFX = numpy.matmul( DFXI, DJI ) 

                for I in range(NNode)
                    for J in range(NNode)
                        Phi_Phi_T[I][J] = FN[I] * FN[J] * FAC

                # Element mass matrix <Modify>
                for IDim in range(NDim):
                    ME[IDim*NNode:(IDim+1)*NNode][IDim*NNode:(IDim+1)*NNode] += Rho * Phi_Phi_T[:][:]

    def Mass_2D_3N(self):
        pass