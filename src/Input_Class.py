

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

    def Read_Data(self):

        # Import built-in libraries ================================================================
        import os
        import shutil

        # Input data ==========================================================
        # Read the name of the input file from address file
        print(" ============== Input Class ==============")
        Address = open("Address.txt","r")
        Temp = Address.readline().rstrip("\n")      # 1
        File = Address.readline().rstrip("\n")  # 2, Input file name
        
        Temp = Address.readline().rstrip("\n")  # 3
        Temp = Address.readline().rstrip("\n")  # 4
        Input_Dir = Address.readline().rstrip("\n")  # 5
        
        Temp = Address.readline().rstrip("\n")  # 6
        Temp = Address.readline().rstrip("\n")  # 7
        Output_Dir = Address.readline().rstrip("\n")  # 8

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
            Temp = input("Press Enter if it is alright, otherwise copy the content of the folder. --IS IT ALRIGHT? --")
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



    def Read_Input(self):

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
        self.NEl = float(Temp[0])
        print("{:40} {:f}".format(" The total number of elements is\are:", self.NEl))

        Temp = File_Input.readline().rstrip("\n")
        Temp = Temp.split()
        self.El_Type = float(Temp[0])
        print("{:40} {:f}".format(" The element type is:", self.El_Type))

        Temp = File_Input.readline().rstrip("\n")
        Temp = Temp.split()
        self.NInt_Type = float(Temp[0])
        print("{:40} {:f}".format(" The integration point type is:", self.NInt_Type))

        Temp = File_Input.readline().rstrip("\n")
        Temp = Temp.split()
        self.NInt = float(Temp[0])
        print("{:40} {:f}".format(" The integration point type is:", self.NInt))

        Temp = File_Input.readline().rstrip("\n")
        Temp = Temp.split()
        self.NDim = float(Temp[0])
        print("{:40} {:f}".format(" The dimension of space is:", self.NDim))

        Temp = File_Input.readline().rstrip("\n")
        Temp = Temp.split()
        self.NNode = float(Temp[0])
        print("{:40} {:f}".format(" The Number of Nodes of each element is:", self.NNode))

        Temp = File_Input.readline().rstrip("\n")
        Temp = Temp.split()
        self.NPoints = float(Temp[0])
        print("{:40} {:f}".format(" The Number of Points in the model:", self.NPoints))

        Temp = File_Input.readline().rstrip("\n")
        Temp = Temp.split()
        self.Rho = float(Temp[0])
        print("{:40} {:f}".format(" The density of the material is:", self.Rho))

        Temp = File_Input.readline().rstrip("\n")
        Temp = Temp.split()
        self.NDOF = float(Temp[0])

        close(File_Input)


    def Read_Arrays(self):

        # Import built-in libraries ================================================================
        import numpy as np

        # Import user-defined modules ==============================================================

        print(" Opening the data file ...")
        File_Input = open(self.DataFileName,"r")
        print()

        # Reading coordinates of each node
        Temp = File_Input.readline().rstrip("\n")
        for INode in range(NPoints):
            Temp = File_Input.readline().rstrip("\n")
            Temp = Temp.split()
            for ii in range(NDim)
                self.XYZ[INode][ii] = float(Temp[ii])

        # Reading connectivities
        Temp = File_Input.readline().rstrip("\n")
        Temp = File_Input.readline().rstrip("\n")
        for IEl in range(NEl):
            Temp = File_Input.readline().rstrip("\n")
            Temp = Temp.split()
            for INode in range(NNode)
                self.Conn[INode][Temp[0]] = Temp[INode+1]

        # Reading Constraints
        Temp = File_Input.readline().rstrip("\n")
        Temp = File_Input.readline().rstrip("\n")
        for INode in range(NPoints):
            Temp = File_Input.readline().rstrip("\n")
            Temp = Temp.split()
            for IDim in range(NDim)
                self.ID[Temp[0]][IDim] = Temp[IDim+1]


    
        