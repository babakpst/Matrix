

####################################################################################################
# Purpose: This code computes the mass, stiffness matrix of Q4, Q8, T3, T6
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

def main(arg):

    # Import built-in libraries ====================================================================
    import sys
    import math  # 
    import os    #  You can create/del dir using this module
    import time  # time.sleep(2)
    from datetime import datetime 

    # Import user-defined modules ==================================================================
    import Compute_Class


    # Code begins =====================================================================================
    print()
    print("{:^80}".format("----------------------- Mass matrix comparison -----------------------"))
    print("{:^80}".format("---------- Developers:: Babak Poursartip/Clint Dawson ----------------"))
    print()
    print("{:^80}".format(" Simulation starts ..."))
    print()

    Results = Compute_Class.Compute_Class()
    Results.Compute_Matrices()

    print("{:80}".format("---------- Simulation was conducted successfully ----------"))
    print()


if __name__ == '__main__':
    import sys    
    main(sys.argv)