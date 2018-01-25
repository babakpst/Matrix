

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

        # Create or Clean the output directory
        if os.path.exists(self.Output_Dir):
            print(" The output folder exists! The content of this folder would be emptied.")
            Temp = input("Press Enter if it is alright, otherwise copy the content of the folder. --IS IT ALRIGHT? --")
            shutil.rmtree(self.Output_Dir, ignore_errors=True)
            os.makedirs(self.Output_Dir)

        if not os.path.exists(self.Output_Dir):
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
        Temp = File_Input.readline().rstrip("\n")
        self.Total_Time = float(Temp)  # Total simulation time
        #print("{:40} {:f}".format(" The total simulation time is:", self.Total_Time))

        Temp = File_Input.readline().rstrip("\n")
        Temp = File_Input.readline().rstrip("\n")
        Temp = File_Input.readline().rstrip("\n")
        self.El_Type = float(Temp) # 1 for quad, 2 for triangle

        Temp = File_Input.readline().rstrip("\n")
        Temp = File_Input.readline().rstrip("\n")
        Temp = File_Input.readline().rstrip("\n")
        self.NNode = float(Temp)

        Temp = File_Input.readline().rstrip("\n")
        Temp = File_Input.readline().rstrip("\n")
        Temp = File_Input.readline().rstrip("\n")
        self.NDim = float(Temp)

        Temp = File_Input.readline().rstrip("\n")
        Temp = File_Input.readline().rstrip("\n")
        Temp = File_Input.readline().rstrip("\n")
        self.NInt = float(Temp)

        Temp = File_Input.readline().rstrip("\n")
        Temp = File_Input.readline().rstrip("\n")
        Temp = File_Input.readline().rsself.trip("\n")
        self.Rho = float(Temp)

        Temp = File_Input.readline().rstrip("\n")
        Temp = File_Input.readline().rstrip("\n")
        Temp = File_Input.readline().rstrip("\n")
        self.NPoints = float(Temp)

        Temp = File_Input.readline().rstrip("\n")
        Temp = File_Input.readline().rstrip("\n")
        Temp = File_Input.readline().rstrip("\n")
        self.NEl = float(Temp)

        Temp = File_Input.readline().rstrip("\n")
        Temp = File_Input.readline().rstrip("\n")
        Temp = File_Input.readline().rstrip("\n")
        self.NDOF = float(Temp) # Number of Degree of Freedom

        close(File_Input)


    def Read_Arrays(self):

        # Import built-in libraries ================================================================
        import numpy as np

        # Import user-defined modules ==============================================================



        print(" Opening the data file ...")
        File_Input = open(self.DataFileName,"r")
        print()

        for INode in range(NPoints):
            Temp = File_Input.readline().rstrip("\n")
            self.XYZ[INode,1] = float()
            self.XYZ[INode,1] = float()
            self.XYZ[INode,1] = float()

        for IEl in range(NEl):
            for INode in range(NNode)
            self.Conn[IEl,INode] = 

        for INode in range(NPoints):
            Temp = File_Input.readline().rstrip("\n")
            self.ID[INode,]
    
        