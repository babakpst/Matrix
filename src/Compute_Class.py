
#####################################################################
# Code developed by: Dr. Babak Poursartip
# Supervised by:     Dr. Clint Dawson
# The Institute for Computational Engineering and Sciences (ICES)
# The University of Texas at Austin
#
# Start date:    01/22/2018
# Latest update: 01/26/2018
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
        self.XYZ       = np.zeros((Input.NPoint, Input.NDim),  dtype=np.float64)  # Coordinates of nodes
        self.Conn      = np.zeros((Input.NNode, Input.NEl),    dtype=np.float64)  # Element's Connectivity
        self.ID        = np.zeros((Input.NPoints, Input.NDOF), dtype=np.float64)  # Constraints

        self.Me        = np.zeros((NEqEl, NEqEl), dtype=np.float64)  # Element mass matrix
        self.M_Global  = np.zeros((NEq, NEq), dtype=np.float64)      # Global mass matrix
        self.ND        = np.zeros((NEq, NEq), dtype=np.float64)      # Nodal connectivity

        self.WINT      = np.zeros(Input.NInt, dtype=np.float64)      # Weight coefficient for numerical integration
        self.XINT      = np.zeros(Input.NInt, dtype=np.float64)      # Integration points

        self.XT        = np.zeros((Input.NDim, Input.NNode), dtype=np.float64) # Local coordinates of the each element

        # Read arrays from input file ==============================================================
        Input.Read_Arrays()

        # Extracting Integration points
        Parameters = Parameters_Class.Parameters_Class(Input.NInt, Input.NInt_Type)
        GaussPoint = Parameters.Integration_Points_def()

        # Creating the Mass_Matrix object
        Mass = Mass_Matrix_Class.Mass_Matrix_Class()

        # Output folder
        Output_File = os.path.join( Ex.Output_Dir,("Mass_"+Input.Model) ) 
        Output = open(Output_File,"w")

        for IEl in range(NEl):

            print("{} {:d}".format(" Computing the mass matrix of element: ", IEl))

            # Finding the local coordinates for each element
            for ii in range(NDim):
                for jj in range(NNode):
                    self.XT[ii][jj] = self.XYZ[Conn[jj][IEl]][ii]

            # Initialize the mass matrix
            ME[:][:]  = 0.0

            # Choosing the right function
            if Input.El_Type == 1: # Quad elements
                Mass.Mass_2D_4N(                                 \
                    IEL, Input.NNode, Input.NDim, Input.NInt,    \   # ! Integer Variables
                    Input.Rho,                                   \   # ! Real Variables
                    self.XT, self.ME,                            \   # ! Real Arrays
                    self.XINT, self.WINT
                )
            elif Input.El_Type == 2: # Triangle element
                Mass.Mass_2D_3N()

            Output.write(" The mass matrix of element number ")
            Output.write(str(IEl))
            Output.write("\n")
            Matrix = np.matrix(self.ME)
            for line in Matrix:
                np.savetxt(Output, line, fmt="%.6f")
            Output.write("\n")
            Output.write("\n")
            

            Assemble()

        # print results
        del Output



    def Assemble (self):
        
















        
