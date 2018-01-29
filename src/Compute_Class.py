####################################################################################################
# Purpose: This class containts the functions that computes the mass matrix.
#
# Developed by: Babak Poursartip
# 
# The Institute for Computational Engineering and Sciences (ICES)
# The University of Texas at Austin
#
# ================================ V E R S I O N ===================================================
# V0.0: 01/22/2018 - Class initiation.
# V0.1: 01/29/2018 - Function compiled successfully for the first time.
#
# File version $Id
#
#
# ================================ L O C A L   V A R I A B L E S ===================================
# (Refer to the main code to see the list of imported variables)
#  . . . . . . . . . . . . . . . . Variables . . . . . . . . . . . . . . . . . . . . . . . . . . . .
# - NDOF: Number of Degrees of Freedoms for each node -read from the input file.
# - NNode: Total number of nodes in each element - read from the input file.
# - NEqEl: Total number of equations for each element= NDOF*NNode - Computed in the code
#
#  . . . . . . . . . . . . . . . . Arrays  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
# -ND[NEqEl] (int): Nodal location array. We use this array to determine the location of matrix 
#                   assembling in the global matrix.
# -ID[NPoints][NDOF] (int): Holds the constrains on all grid points --read from the input file. 
#
####################################################################################################

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

    # Read data from input file ================================================================
    Input = Input_Class.Input_Class()
    Input.Read_Data()  # Reads the address file 
    Input.Read_Input() # Reads the initial data to create arrays

    # Basic calculations =======================================================================
    NEqEl  = Input.NDOF * Input.NNode      # Number of Equations(NDOF) for each element
    NEq    = Input.NDOF * Input.NPoints    # Number of Equations(NDOF) for the entire model


    # Define Arrays ============================================================================
    self.XYZ       = np.zeros((Input.NPoints, Input.NDim),  dtype=np.float64)  # Coordinates of nodes
    self.Conn      = np.zeros((Input.NNode, Input.NEl),    dtype=np.float64)  # Element's Connectivity
    self.ID        = np.zeros((Input.NPoints, Input.NDOF), dtype=np.float64)  # Constraints

    self.Me        = np.zeros((NEqEl, NEqEl), dtype=np.float64)  # Element mass matrix
    self.M_Global  = np.zeros((NEq, NEq), dtype=np.float64)      # Global mass matrix
    self.ND        = np.zeros(NEqEl, dtype=np.float64)             # Nodal connectivity

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
        Mass.Mass_2D_4N(                               
          IEL, Input.NNode, Input.NDim, Input.NInt,       # ! Integer Variables
          Input.Rho,                                      # ! Real Variables
          self.XT, self.ME,                               # ! Real Arrays
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
        
      # Form the ND array for assembling - This array indicates how to assemble the element 
      # matrix in the global matrix
      for ii in range(NNode):
        for jj in range(NDOF):
          ND[(jj-1) * NNode + ii ] = ID[Conn[ii][IEl]][jj]

      Assemble(                
                self.NEqEl,                # Integer Variables
                self.ND,                   # Integer Arrays
                self.ME, self.M_Global     # Real Arrays  
                )


    Output.write(" Global mass matrix")
    Output.write("\n")
    Matrix = np.matrix(self.M_Global)
    for line in Matrix:
      np.savetxt(Output, line, fmt="%.6f")
    Output.write("\n")
    Output.write("\n")

    del Output


####################################################################################################
# Purpose: This funciton assembles the local matrix in the global matrix.
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
#
#
####################################################################################################

  def Assemble (self,                
                NEqEl,                # Integer Variables
                ND,                   # Integer Arrays
                ME, M_Global          # Real Arrays  
                ):

    for ll in range(NEqEl):
      for nn in range(NEqEl):
        ii  = ND[ll]
        jj  = ND[nn]

        if ii == 0 or jj == 0:
          continue

        M_Global[ii][jj] += ME[ll][nn]

