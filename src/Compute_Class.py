
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

    def Compute_Matrices(self):

        # Import built-in libraries ================================================================
        import numpy as np        

        # Import user-defined modules ==============================================================
        import Input_Class
        import Parameters_Class
        import Mass_Matrix_Class
        import Results_Class

        # Read data from input file ================================================================
        Input = Input_Class.Input_Class()
        Input.Read_Data()  # Reads the address file 
        Input.Read_Input() # Reads the initial data to create arrays

        # Basic calculations =======================================================================
        NEqEl  = Input.NDOF * Input.NNode      # Number of Equations(NDOF) for each element
        NEq    = Input.NDOF * Input.NPoints    # Number of Equations(NDOF) for the entire model


        # Define Arrays ============================================================================
        self.XYZ       = np.zeros(Input.NPoint, Input.NDim, dtype=np.float64)  # Elemental Equations
        self.Conn      = np.zeros(Input.NEl, Input.NNode, dtype=np.float64)  # Elemental Equations
        self.ID        = np.zeros(Input.NPoints, Input.NDOF, dtype=np.float64) # Elemental Equations

        self.Me        = np.zeros(NEqEl, NEqEl, dtype=np.float64)  # Elemental Equations
        self.M_Global  = np.zeros(NEq, NEq, dtype=np.float64)      # Elemental Equations
        self.ND        = np.zeros(NEq, NEq, dtype=np.float64)      # Elemental Equations

        # Read arrays from input file ==============================================================
        Input.Read_Arrays()

        # Extracting Integration points
        Parameters = Parameters_Class.Parameters_Class(Input.NInt, Input.NInt_Type)
        GaussPoint = Parameters.Integration_Points_def()

        # Creating the Mass_Matrix object
        Mass = Mass_Matrix_Class.Mass_Matrix_Class()

        for IEl in range(NEl):

            if Input.El_Type == 1: # Quad elements
                Mass.Mass_2D_4N()
            elif Input.El_Type == 2: # Triangle element
                Mass.Mass_2D_3N()

            Assemble

        # print results

    def Assemble (self):
        pass
