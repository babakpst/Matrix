

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

class Input_Class:

    def __int__(self):
        pass

    def Read_Data_def(self):

        # Import built-in libraries ================================================================
        import os
        import shutil

        # Input data ==========================================================
        # Read the name of the input file from address file
        print(" ============== Input Class ==============")
        Address = open("Address.txt","r")
                        
        Temp = Address.readline().rstrip("\n")      # 1
        File = Address.readline().rstrip("\n")      # 2, Input file name
        
        Temp = Address.readline().rstrip("\n")      # 3
        Temp = Address.readline().rstrip("\n")      # 4
        Input_Dir = Address.readline().rstrip("\n") # 5
        
        Temp = Address.readline().rstrip("\n")      # 6
        Temp = Address.readline().rstrip("\n")      # 7
        Output_Dir = Address.readline().rstrip("\n")# 8

        # Create Input/Output directories
        self.Model = File
        self.InputFileName = os.path.join(Input_Dir, File) 
        self.Output_Dir = os.path.join(Output_Dir, os.path.splitext(File)[0])
        self.DataFileName = os.path.join(Input_Dir, (os.path.splitext(File)[0])+".dat")

        print(" {0} {1}".format("The input file name is:", self.InputFileName))
        print(" {0} {1}".format(" The output path is:", self.Output_Dir))

        # Check whether the input file exists 
        if not os.path.exists(self.InputFileName):
            print("{}".format("       FATAL ERROR   "))
            print("{}".format(" The input file does not exist!"))
            print("{}".format(" Please double check the input file or dirctory"))
            print("{}".format(" Simulation terminates"))

        # Create or Clean the output directory
        if os.path.exists(self.Output_Dir):
            print(" The output folder exists! The content of this folder would be emptied.")
            #Temp = input("Press Enter if it is alright, otherwise copy the content of the folder. --IS IT ALRIGHT? --")
            shutil.rmtree(self.Output_Dir, ignore_errors=True)
            os.makedirs(self.Output_Dir)
        elif not os.path.exists(self.Output_Dir):
            print(" The output directory does not exist. ")
            print(" Creating the output directory ... ")
            os.makedirs(self.Output_Dir)

        # Empty memory
        Address.close()
        del Temp
        del File
        del Input_Dir



    def Read_Input_def(self):

        # Import built-in libraries ================================================================
        import numpy as np

        # Import user-defined modules ==============================================================


        print(" Opening the input file ...")
        File_Input = open(self.InputFileName,"r")
        print()

        # -- Opens and Reads data from the input file
        Temp = File_Input.readline().rstrip("\n")
        Temp = File_Input.readline().rstrip("\n")

        Temp = File_Input.readline().rstrip("\n")
        Temp = Temp.split()
        self.NEl = int(Temp[0])
        print("{:40} {:f}".format(" The total number of elements is/are:", self.NEl))

        Temp = File_Input.readline().rstrip("\n")
        Temp = Temp.split()
        self.El_Type = int(Temp[0])
        print("{:40} {:f}".format(" The element type is:", self.El_Type))

        Temp = File_Input.readline().rstrip("\n")
        Temp = Temp.split()
        self.NInt_Type = int(Temp[0])
        print("{:40} {:f}".format(" The integration point type is:", self.NInt_Type))

        Temp = File_Input.readline().rstrip("\n")
        Temp = Temp.split()
        self.NInt = int(Temp[0])
        print("{:40} {:f}".format(" Number of integration points:", self.NInt))

        Temp = File_Input.readline().rstrip("\n")
        Temp = Temp.split()
        self.NDim = int(Temp[0])
        print("{:40} {:f}".format(" The dimension of space is:", self.NDim))

        Temp = File_Input.readline().rstrip("\n")
        Temp = Temp.split()
        self.NNode = int(Temp[0])
        print("{:40} {:f}".format(" The Number of Nodes of each element is:", self.NNode))

        Temp = File_Input.readline().rstrip("\n")
        Temp = Temp.split()
        self.NPoints = int(Temp[0])
        print("{:40} {:f}".format(" The Number of Points in the model:", self.NPoints))

        Temp = File_Input.readline().rstrip("\n")
        Temp = Temp.split()
        self.Rho = float(Temp[0])
        print("{:40} {:f}".format(" The density of the material is:", self.Rho))

        Temp = File_Input.readline().rstrip("\n")
        Temp = Temp.split()
        self.NDOF = int(Temp[0])
        print("{:40} {:f}".format(" Degrees of freedom of each node:", self.NDOF))

        del File_Input


    def Read_Arrays_def(self, NEq, XYZ, Conn, ID):

        # Import built-in libraries ================================================================
        import numpy as np
        import sys

        # Import user-defined modules ==============================================================

        print(" Opening the data file ...")
        File_Input = open(self.DataFileName,"r")
        print()

        # Reading coordinates of each node
        print(" Reading coordinates ...")
        Temp = File_Input.readline().rstrip("\n")
        for INode in range(self.NPoints):
            Temp = File_Input.readline().rstrip("\n")
            Temp = Temp.split()
            for ii in range(self.NDim):
                XYZ[INode][ii] = float(Temp[ii])

        # Reading connectivities
        print(" Reading connectivities ...")
        Temp = File_Input.readline().rstrip("\n")
        Temp = File_Input.readline().rstrip("\n")
        for IEl in range(self.NEl):
            Temp = File_Input.readline().rstrip("\n")
            Temp = Temp.split()
            for INode in range(self.NNode):
                Conn[INode][int(Temp[0])-1] = int(Temp[INode+1])-1

        # Reading Constraints
        print(" Reading constraints ...")
        Temp = File_Input.readline().rstrip("\n")
        Temp = File_Input.readline().rstrip("\n")
        for INode in range(self.NPoints):
            Temp = File_Input.readline().rstrip("\n")
            Temp = Temp.split()
            for IDim in range(self.NDim):
                ID[int(Temp[0])-1][IDim] = int(Temp[IDim+1])
                if (not ID[int(Temp[0])-1][IDim] == 0) or (not ID[int(Temp[0])-1][IDim] == 0):
                    print(" Wrong input for constraints. Modify the input file.")
                    sys.exit(" The simulation terminated due to the input file.")



        # Finding the equation number
        NEq = -1
        for IDim in range(self.NDim):
            for INode in range(self.NPoints):
                if ID[INode][IDim] == 0:
                    NEq += 1
                    ID[INode][IDim] = NEq
                elif ID[INode][IDim] == 1:
                    ID[INode][IDim] = -1
        
        print("{} {:d}".format(" Total number of equations: ",NEq))



    
        