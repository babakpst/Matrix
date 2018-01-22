

####################################################################################################
#
# Code developed by: Dr. Babak Poursartip
# Supervised by:     Dr. Clint Dawson
# 
# The Institute for Computational Engineering and Sciences (ICES)
# The University of Texas at Austin
#
# Start date:    01/22/2018
# Latest update: 01/22/2018
#
# Comment: This code computes the mass matrix of CST and Quad elements and compares them together.
#
####################################################################################################

def main(arg):

    # Import built-in libraries =======================================================================
    # import numpy as np --delete

    # Import classes ==================================================================================
    import sys
    import math  # 
    import os    #  You can create/del dir using this module
    import time  # time.sleep(2)
    from datetime import datetime 

    # Code begins =====================================================================================
    print()
    print("{:^80}".format("----------------------- Mass matrix comparison -----------------------"))
    print("{:^80}".format("---------- Developers:: Babak Poursartip/Clint Dawson ----------------"))
    print()
    print("{:^80}".format(" Simulation starts ..."))
    print()

    #Results = Solver_Class.Solver()

    print("{:80}".format("---------- Simulation was conducted successfully ----------"))
    print()


if __name__ == '__main__':
    import sys    
    main(sys.argv)