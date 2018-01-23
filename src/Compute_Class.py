
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

class Compute_Class:

    def __init__(self):
        pass

    def Compute_Matrices(self, NEl)

        # Import built-in libraries ================================================================
        import numpy as np        

        # Import user-defined modules ==============================================================
        import Input_Class
        import Parameters_Class
        import Mass_Matrix_Class

        # Read data from input file ================================================================
        Input = Input_Class.Input_Class()
        Input.Read_Data()  # Reads the address file 
        Input.Read_Input()

        # Basic calculations =======================================================================
        NEqEl  = NDim * NNode
        NEq    = NDim * NPoints

        

        # Define Arrays ============================================================================
        Me        = np.zeros(NEqEl, NEqEl, dtype=np.float64) # Elemental Equations
        M_Global  = np.zeros(NEq, NEq, dtype=np.float64) # Elemental Equations
        XYZ       = np.zeros(NPoint, NDim, dtype=np.float64) # Elemental Equations

        Input.Read_Arrays()

        for IEl in range(NEl):
            # call for elemental matrices
            # call assemble

        # print results

    def Assemble (self)
