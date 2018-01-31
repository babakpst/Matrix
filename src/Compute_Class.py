
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
# V0.2: 01/31/2018 - General modifications
#
# File version $Id
#
#
# ================================ L O C A L   V A R I A B L E S ===================================
# (Refer to the main code to see the list of imported variables)
#  . . . . . . . . . . . . . . . . Variables . . . . . . . . . . . . . . . . . . . . . . . . . . . .
#
####################################################################################################

class Compute_Class:

  def __init__(self):
      pass


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

        if ii == -1 or jj == -1:
          continue
        M_Global[ii][jj] += ME[ll][nn]



####################################################################################################
# Purpose: This function manages the funciton calls to compute the mass and stiffness matrix.
#
# Developed by: Babak Poursartip
# 
# The Institute for Computational Engineering and Sciences (ICES)
# The University of Texas at Austin
#
# ================================ V E R S I O N ===================================================
# V0.0: 01/22/2018 - Class initiation.
# V0.1: 01/29/2018 - Function compiled successfully for the first time.
# V0.2: 01/31/2018 - General modifications
#
# File version $Id
#
#
# ================================ L O C A L   V A R I A B L E S ===================================
# (Refer to the main code to see the list of imported variables)
#  . . . . . . . . . . . . . . . . Variables . . . . . . . . . . . . . . . . . . . . . . . . . . . .
# -NEqEl: Total number of equations for each element= NDOF*NNode - Computed in the code
# -NDOF: Number of Degrees of Freedoms for each node -read from the input file.
# -NNode: Total number of nodes in each element - read from the input file.
#
#  . . . . . . . . . . . . . . . . Arrays  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
# -XYZ[NPoints][Input.NDim] (float64): Holds the coordinates of all nodes.
# -ME[NEqEl][NEqEl] (float64): Element mass matrix
# -M_Sum[NEl] (float): Holds the total mass matrix of each element
# -Conn = [NNode][NEl] (int32): Holds Connectivity of elements (CCW order)
# -ND[NEqEl] (int): Nodal location array. We use this array to determine the location of matrix 
#                   assembling in the global matrix.
# -ID[NPoints][NDOF] (int): Holds the constrains on all grid points --read from the input file. 
# -M_Global[NEq][NEq] (float64): Global mass matrix
# -XINT[Coe*NInt] (float64): Integration points
# -WINT[Coe*NInt] (float64): Integration weight
#
####################################################################################################

  def Compute_Matrices(self):

    # Import built-in libraries ================================================================
    import numpy as np
    import os
    import shutil
    import csv

    # Import user-defined modules ==============================================================
    import Input_Class
    import Parameters_Class
    import Mass_Matrix_Class

    # Read data from input file ================================================================
    Input = Input_Class.Input_Class()
    Input.Read_Data_def()  # Reads the address file 
    Input.Read_Input_def() # Reads the initial data to create arrays

    # Basic calculations =======================================================================
    NEqEl  = Input.NDOF * Input.NNode      # Number of Equations(NDOF) for each element
    #NEq    = Input.NDOF * Input.NPoints    # Number of Equations(NDOF) for the entire model
    #self.NEq = 0    

    # Define Arrays ============================================================================
    self.XYZ  = np.zeros((Input.NPoints, Input.NDim), dtype=np.float64)  # Coordinates of nodes
    self.Conn = np.zeros((Input.NNode, Input.NEl),    dtype=np.int32)     # Element's Connectivity
    self.ID   = np.zeros((Input.NPoints, Input.NDOF), dtype=np.int32)     # Constraints

    self.ME   = np.zeros((NEqEl, NEqEl), dtype=np.float64)  # Element mass matrix
    self.M_Sum= np.zeros(Input.NEl, dtype=np.float64)             # Holds the total mass of each element
    self.ND   = np.zeros(NEqEl, dtype=np.int32)             # Nodal connectivity

    if Input.NInt_Type == 1:
      Coe = 1
    elif Input.NInt_Type == 2:
      Coe = 2

    self.XINT = np.zeros(Coe*Input.NInt, dtype=np.float64) # Integration points
    self.WINT = np.zeros(Input.NInt, dtype=np.float64) # Weight coefficients for num. integration
    
    self.XT   = np.zeros((Input.NDim, Input.NNode), dtype=np.float64) # Local coordinates of each element

    # Read arrays from input file ==============================================================
    Input.Read_Arrays_def(self.XYZ, self.Conn, self.ID)

    print("{} {:d}".format(" Total number of equations are: ", Input.NEq))
    self.M_Global  = np.zeros((Input.NEq, Input.NEq), dtype=np.float64)      # Global mass matrix

    # Extracting Integration points
    Parameters = Parameters_Class.Parameters_Class(Input.NInt, Input.NInt_Type)
    GaussPoint = Parameters.Integration_Points_def(self.XINT, self.WINT)

    # Creating the Mass_Matrix object
    Mass = Mass_Matrix_Class.Mass_Matrix_Class()

    # Output folder
    #Output_File = os.path.join(Input.Output_Dir,("Mass_"+os.path.splitext(Input.Model)[0]+".csv")) 
    Output_File = os.path.join(Input.Output_Dir,("Mass_"+Input.Model)) 
    Output = open(Output_File,'w')

    # Loop over the elements to find the element matrix
    for IEl in range(Input.NEl):

      print("{} {:d}".format(" Computing the mass matrix of element: ", IEl))

      # Finding the local coordinates for each element
      for ii in range(Input.NDim):
        for jj in range(Input.NNode):
          self.XT[ii][jj] = self.XYZ[self.Conn[jj][IEl]][ii]

      # Initialize the mass matrix
      self.ME[:][:]  = 0.0

      # Choosing the right function
      if Input.El_Type == 1: # Quad elements
        Mass.Mass_2D_4N_def(                               
          IEl, Input.NNode, Input.NDim, Input.NInt, NEqEl,# ! Integer Variables
          Input.Rho,                                      # ! Real Variables
          self.XT, self.ME, self.M_Sum,                   # ! Real Arrays
          self.XINT, self.WINT
        )
      elif Input.El_Type == 2: # Triangle element
          Mass.Mass_2D_3N_def(
            IEl, Input.NNode, Input.NDim, Input.NInt, NEqEl,# ! Integer Variables
            Input.Rho,                                      # ! Real Variables
            self.XT, self.ME, self.M_Sum,                   # ! Real Arrays
            self.XINT, self.WINT            
            )

      # Writing the element mass matrix in the file
      Output.write(" The mass matrix of element number: ")
      Output.write(str(IEl))
      Output.write("- The total mass is: ")
      Output.write(str(self.M_Sum[IEl]))
      Output.write("\n")
      for ii in range(NEqEl):
        for jj in range(NEqEl):
          Output.write("{:9.6f}".format(self.ME[ii][jj] ))
          Output.write("  ")
        Output.write("\n")
      Output.write("\n")
      Output.write("\n")
        
      # Form the ND array for assembling - This array indicates how to assemble the element 
      # matrix in the global matrix
      for ii in range(Input.NNode):
        for jj in range(Input.NDOF):
          self.ND[(jj-1) * Input.NNode + ii ] = self.ID[self.Conn[ii][IEl]][jj]

      # Assemgble the local mass matrix in the global mass matrix
      self.Assemble(                
                NEqEl,                # Integer Variables
                self.ND,                   # Integer Arrays
                self.ME, self.M_Global     # Real Arrays  
                )


    # Writing the global matrix on the file
    Output.write(" Global mass matrix")
    Output.write("\n")
    for ii in range(Input.NEq):
      for jj in range(Input.NEq):
        Output.write("{:9.6f}".format(self.M_Global[ii][jj] ))
        Output.write("  ")
      Output.write("\n")
    Output.write("\n")
    Output.write("\n")

    del Output


