
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


####################################################################################################
# Purpose: This funciton conducts a matrix-matrix multiplication.
#
# Developed by: Babak Poursartip
# 
# The Institute for Computational Engineering and Sciences (ICES)
# The University of Texas at Austin
#
# ================================ V E R S I O N ===================================================
# V0.0: 01/29/2018 - Function initiation.
# V0.1: 01/29/2018 - Function compiled successfully for the first time.
#
# File version $Id
#
#
# ================================ L O C A L   V A R I A B L E S ===================================
# (Refer to the main code to see the list of imported variables)
#
# -C[len(A)][len(B)] (float64): The result matrix.
#
#
#
####################################################################################################

    def matrixmult_def(self, A, B):

        import numpy as np

        C = np.zeros( (len(A),len(B)), dtype=np.float64)
        
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    C[i][j] += A[i][k]*B[k][j]
        return C



####################################################################################################
# Purpose: This funciton computes the mass matrix of a quad element: 2D 4 noded.
#
# Developed by: Babak Poursartip
# 
# The Institute for Computational Engineering and Sciences (ICES)
# The University of Texas at Austin
#
# ================================ V E R S I O N ===================================================
# V0.0: 01/22/2018 - Function initiation.
# V0.1: 01/29/2018 - Function compiled successfully for the first time.
# V0.2: 01/30/2018 - Minor changes.
#
# File version $Id
#
#
# ================================ L O C A L   V A R I A B L E S ===================================
# (Refer to the main code to see the list of imported variables)
#
# -DJ[NDim][NDim] (float):  Jacobian matrix in the local coordinates
# -DJI[NDim][NDim] (float):  Jacobian inverse matrix
# -DFX[NNode][NDim] (float64):  Jacobian matrix in the global coordinates
# -DFXI[NNode][NDim] (float64):  Inverse Jacobian matrix in the global coordinates
# -Phi_Phi_T[NNode][NNode] (float64)  A matrix holding N.N^T
# -FN[NNode] (float64): Shape function array
#
#
####################################################################################################
    def Mass_2D_4N_def(self,
                   IEL, NNode, NDim, NInt,                   #  Integer Variables
                   Rho,                                      #  Real Variables
                   XT, ME,                                   #  Real Arrays
                   XINT, WINT                                #  Type 
                   ):

        # Import built-in libraries ================================================================
        import numpy as np

        # Import user-defined modules ==============================================================
        import Parameters_Class

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

                # Shape funcitons and derivative of shape functions
                ShapeFunc.Shape_Func_2D_4N_def(FN, X1, X2)
                ShapeFunc.Derivative_Shape_Func_2D_4N_def(DFXI, X1, X2)

                DJ   = self.matrixmult_def(XT, DFXI)

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

                DFX = self.matrixmult_def(DFXI,DJI) 

                for I in range(NNode):
                    for J in range(NNode):
                        Phi_Phi_T[I][J] = FN[I] * FN[J] * FAC

                # Element mass matrix <Modify>
                for IDim in range(NDim):
                  for INode in range(NNode):
                    for JNode in range(NNode):
                      ME[IDim*NNode+INode][IDim*NNode+JNode] += Rho * Phi_Phi_T[INode][JNode]





####################################################################################################
# Purpose: This funciton computes the mass matrix of a quad element: 2D 4 noded.
#
# Developed by: Babak Poursartip
# 
# The Institute for Computational Engineering and Sciences (ICES)
# The University of Texas at Austin
#
# ================================ V E R S I O N ===================================================
# V0.0: 01/22/2018 - Function initiation.
# V0.1: 01/29/2018 - Function compiled successfully for the first time.
# V0.2: 01/30/2018 - Minor changes.
#
# File version $Id
#
#
# ================================ L O C A L   V A R I A B L E S ===================================
# (Refer to the main code to see the list of imported variables)
#
# -DJ[NDim][NDim] (float):  Jacobian matrix in the local coordinates
# -DJI[NDim][NDim] (float):  Jacobian inverse matrix
# -DFX[NNode][NDim] (float64):  Jacobian matrix in the global coordinates
# -DFXI[NNode][NDim] (float64):  Inverse Jacobian matrix in the global coordinates
# -Phi_Phi_T[NNode][NNode] (float64)  A matrix holding N.N^T
# -FN[NNode] (float64): Shape function array
#
#
####################################################################################################

    def Mass_2D_3N_def(self,
            IEL, NNode, NDim, NInt,            # Integer Variables
            Rho,                               # Real Variables
            XT, ME,                            # Real Arrays
            XINT, WINT                         #  Type 
            ):

        # Import built-in libraries ================================================================
        import numpy as np

        # Import user-defined modules ==============================================================
        import Parameters_Class

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
        for ll in range(NInt):
  
            r     = XINT[ll]
            s     = XINT[ll+NInt]
            WStar = WINT[ll]

            # Shape funcitons and derivative of shape functions
            ShapeFunc.Shape_Func_2D_3N_def(FN, r, s)
            ShapeFunc.Derivative_Shape_Func_2D_3N_def(DFXI, r, s)

            DJ   = self.matrixmult_def(XT, DFXI)

            DETJ = DJ[0][0] * DJ[1][1] - DJ[1][0] * DJ[0][1]
            FAC  = WStar * DETJ * 0.5

            if DETJ <= 0.0:
              print("{} {:d} {} {:d}".format(" Fatal error: The Jacobian for element ", IEl, " is negative: ", DETJ))

            # Calculating the Jacobian Inverse
            DJI[0][0] =   DJ[1][1]
            DJI[1][1] =   DJ[0][0]
            DJI[0][1] = - DJ[0][1]
            DJI[1][0] = - DJ[1][0]

            DJI = DJI  / DETJ 

            DFX = self.matrixmult_def(DFXI,DJI) 

            for I in range(NNode):
                for J in range(NNode):
                    Phi_Phi_T[I][J] = FN[I] * FN[J] * FAC

            # Element mass matrix <Modify>
            for IDim in range(NDim):
              for INode in range(NNode):
                for JNode in range(NNode):
                  ME[IDim*NNode+INode][IDim*NNode+JNode] += Rho * Phi_Phi_T[INode][JNode]



