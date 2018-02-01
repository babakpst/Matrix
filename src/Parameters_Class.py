

####################################################################################################
# Purpose: This class contains the integration points/weights.
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
#  . . . . . . . . . . . . . . . . Arrays  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
# -XINT[Coe*NInt] (float64): Integration points
# -WINT[Coe*NInt] (float64): Integration weight
#
####################################################################################################

class Parameters_Class:

    def __init__(self, NInt, NInt_Type):
        self.NInt      = NInt
        self.NInt_Type = NInt_Type

    def Integration_Points_def(self, XINT, WINT):

        # Import built-in libraries ====================================================================
        import math

        # Import user-defined modules ==================================================================


        # Code
        if self.NInt_Type == 1: # Quadrilateral elements

            if   self.NInt ==  1: # polynomial degree 1
                XINT[0] = 0.0    # ABSCISSAE

                WINT[0] = +2.0   # WEIGHTS

            elif self.NInt ==  2: # polynomial degree 3
                XINT[0] = -math.sqrt(1.0/3.0)   # ABSCISSAE
                XINT[1] = +math.sqrt(1.0/3.0)   # ABSCISSAE

                WINT[0] = +1.0  # WEIGHTS
                WINT[1] = +1.0  # WEIGHTS
            
            elif self.NInt ==  3: # polynomial degree 5
                XINT[0] = -math.sqrt(3.0/5.0)  # ABSCISSAE
                XINT[1] = 0.0                  # ABSCISSAE
                XINT[2] = +math.sqrt(3.0/5.0)  # ABSCISSAE

                WINT[0] = 5.0/9.0  # WEIGHTS
                WINT[1] = 8.0/9.0  # WEIGHTS
                WINT[2] = 5.0/9.0  # WEIGHTS

            elif self.NInt ==  4: # polynomial degree 7
                XINT[0] = -math.sqrt((3.0+2.0*math.sqrt(6.0/5.0))/7.0) # ABSCISSAE
                XINT[1] = -math.sqrt((3.0-2.0*math.sqrt(6.0/5.0))/7.0) # ABSCISSAE
                XINT[2] = +math.sqrt((3.0-2.0*math.sqrt(6.0/5.0))/7.0) # ABSCISSAE
                XINT[3] = +math.sqrt((3.0+2.0*math.sqrt(6.0/5.0))/7.0) # ABSCISSAE

                WINT[0] = (18.0-math.sqrt(30.0))/36.0 # WEIGHTS
                WINT[1] = (18.0+math.sqrt(30.0))/36.0 # WEIGHTS
                WINT[2] = (18.0+math.sqrt(30.0))/36.0 # WEIGHTS
                WINT[3] = (18.0-math.sqrt(30.0))/36.0 # WEIGHTS

            elif self.NInt ==  5: # polynomial degree 9
                XINT[0] = -math.sqrt((5.0+2.0*math.sqrt(10.0/7.0))/9.0) # ABSCISSAE
                XINT[1] = -math.sqrt((5.0-2.0*math.sqrt(10.0/7.0))/9.0) # ABSCISSAE
                XINT[2] = 0.0                                           # ABSCISSAE
                XINT[3] = +math.sqrt((5.0-2.0*math.sqrt(10.0/7.0))/9.0) # ABSCISSAE
                XINT[4] = +math.sqrt((5.0+2.0*math.sqrt(10.0/7.0))/9.0) # ABSCISSAE

                WINT[0] = (322.0-13.0*math.sqrt(70.0))/900.0 # WEIGHTS
                WINT[1] = (322.0+13.0*math.sqrt(70.0))/900.0 # WEIGHTS
                WINT[2] = (128.0/225.0)                      # WEIGHTS
                WINT[3] = (322.0+13.0*math.sqrt(70.0))/900.0 # WEIGHTS
                WINT[4] = (322.0-13.0*math.sqrt(70.0))/900.0 # WEIGHTS
            else:
                print("{:^80}".format(" Error in the number of integration points. Enter a number btw 1 to 5."))
                sys.exit()

        elif self.NInt_Type == 2: # Integration points for triangle elements
            #Allocate ( GAUSS_POINTS%XINT ( 2_Smll * NInt ), GAUSS_POINTS%WINT ( NInt ) ) ;
            if self.NInt ==  1: # polynomial degree 1
                XINT[0] = 1.0/3.0  # ABSCISSAE
                XINT[1] = 1.0/3.0  # ABSCISSAE

                WINT[0] = 1.0 # WEIGHTS

            elif self.NInt ==  3: # polynomial degree 5
                XINT[0] = +2.00 / +3.00 # ABSCISSAE
                XINT[1] = +1.00 / +6.00 # ABSCISSAE
                XINT[2] = +1.00 / +6.00 # ABSCISSAE
                XINT[3] = +1.00 / +6.00 # ABSCISSAE
                XINT[4] = +1.00 / +6.00 # ABSCISSAE
                XINT[5] = +2.00 / +3.00 # ABSCISSAE

                WINT[0] = +1.00 / +3.00  # WEIGHTS
                WINT[1] = +1.00 / +3.00  # WEIGHTS
                WINT[2] = +1.00 / +3.00  # WEIGHTS

            elif self.NInt ==  4: # polynomial degree 7
                XINT[0] = + 1.00 / + 3.00 # ABSCISSAE
                XINT[1] = + 3.00 / + 5.00 # ABSCISSAE
                XINT[2] = + 1.00 / + 5.00 # ABSCISSAE
                XINT[3] = + 1.00 / + 5.00 # ABSCISSAE
                XINT[4] = + 1.00 / + 3.00 # ABSCISSAE
                XINT[5] = + 1.00 / + 5.00 # ABSCISSAE
                XINT[6] = + 1.00 / + 5.00 # ABSCISSAE
                XINT[7] = + 3.00 / + 5.00 # ABSCISSAE
                
                WINT[0] = -27.00 / +48.00 # WEIGHTS
                WINT[1] = +25.00 / +48.00 # WEIGHTS
                WINT[2] = +25.00 / +48.00 # WEIGHTS
                WINT[3] = +25.00 / +48.00 # WEIGHTS

            else:
                print("{:^80}".format(" Error in the number of integration points. Enter a number btw 1 to 5."))
                sys.exit()
        else: 
            print("{:^80}".format(" Error in the type of the integration points. Enter a number btw 1 to 2."))
            sys.exit()

####################################################################################################
# Purpose: This class contains the shape functions and their derivatives,
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
#  . . . . . . . . . . . . . . . . Arrays  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
# -FN[NNode] (float64): shape functions in the local coordinates
# -DFXI[Coe*NInt] (float64): The derivative of shape functions in the local coordinates
#
####################################################################################################

class Shape_Function_Class:

    # Shape function of the first-order quad element
    def Shape_Func_2D_4N_def(self, FN, X1, X2):

        FN[0] = ( 1.0 + X1 ) * ( 1.0 - X2 ) * 0.25
        FN[1] = ( 1.0 + X1 ) * ( 1.0 + X2 ) * 0.25
        FN[2] = ( 1.0 - X1 ) * ( 1.0 + X2 ) * 0.25
        FN[3] = ( 1.0 - X1 ) * ( 1.0 - X2 ) * 0.25

    # Derivative of shape functions for the first-order quad element
    def Derivative_Shape_Func_2D_4N_def(self, DFXI, X1, X2):

        DFXI[0][0] = + ( 1.0 - X2 ) * 0.25
        DFXI[0][1] = - ( 1.0 + X1 ) * 0.25
        DFXI[1][0] = + ( 1.0 + X2 ) * 0.25
        DFXI[1][1] = + ( 1.0 + X1 ) * 0.25
        DFXI[2][0] = - ( 1.0 + X2 ) * 0.25
        DFXI[2][1] = + ( 1.0 - X1 ) * 0.25
        DFXI[3][0] = - ( 1.0 - X2 ) * 0.25
        DFXI[3][1] = - ( 1.0 - X1 ) * 0.25

    # Shape functions of the first-order triangle element
    def Shape_Func_2D_3N_def(self, FN, X1, X2):

        FN[0] = 1.0 - X1 - X2
        FN[1] = X1
        FN[2] = X2

    # Derivative of the shape function of the first-order triangle
    def Derivative_Shape_Func_2D_3N_def(self, DFXI, X1, X2):

        DFXI[0][0] = -1.0
        DFXI[0][1] = -1.0
        DFXI[1][0] = +1.0
        DFXI[1][1] =  0.0
        DFXI[2][0] =  0.0
        DFXI[2][1] = +1.0

    # Shape functions of the second-order triangle element
    def Shape_Func_2D_6N_def(self, FN, r, s):

        FN[0] = ( 1.0 - r - s ) * ( 1.0 - 2.0 * r - 2.0 * s ) 
        FN[1] = r * ( 2.0 * r - 1.0 )
        FN[2] = s * ( 2.0 * s - 1.0 ) 
        FN[3] = 4.0 * r * ( 1.0 - r - s )
        FN[4] = 4.0 * r * s
        FN[5] = 4.0 * s * ( 1.0 - r - s )


    # Derivative of the shape function of the second-order triangle
    def Derivative_Shape_Func_2D_6N_def(self, DFXI, r, s):

        DFXI[0][0] = - 3.0 + 4.0 * r + 4.0 * s
        DFXI[0][1] = - 3.0 + 4.0 * r + 4.0 * s
        DFXI[1][0] = + 4.0 * r - 1.0
        DFXI[1][1] =   0.0
        DFXI[2][0] =   0.0
        DFXI[2][1] = + 4.0 * s - 1.0
        DFXI[3][0] = + 4.0 - 8.0 * r - 4.0 * s
        DFXI[3][1] = - 4.0 * r
        DFXI[4][0] = + 4.0 * s
        DFXI[4][1] = + 4.0 * r
        DFXI[5][0] = - 4.0 * s
        DFXI[5][1] = + 4.0 - 4.0 * r - 8.0 * s


    # Shape function of the second-order quad element
    def Shape_Func_2D_8N_def(self, FN, X1, X2):

        FN[0] = ( 1.0 + X1 ) * ( 1.0 - X2 ) * ( -1.0 + X1 - X2 ) * 0.25 ; 
        FN[1] = ( 1.0 + X1 ) * ( 1.0 + X2 ) * ( -1.0 + X1 + X2 ) * 0.25 ; 
        FN[2] = ( 1.0 - X1 ) * ( 1.0 + X2 ) * ( -1.0 - X1 + X2 ) * 0.25 ; 
        FN[3] = ( 1.0 - X1 ) * ( 1.0 - X2 ) * ( -1.0 - X1 - X2 ) * 0.25 ; 

        FN[4] = ( 1.0 - X2 * X2 ) * ( 1.0 + X1 ) * 0.5 ; 
        FN[5] = ( 1.0 - X1 * X1 ) * ( 1.0 + X2 ) * 0.5 ; 
        FN[6] = ( 1.0 - X2 * X2 ) * ( 1.0 - X1 ) * 0.5 ; 
        FN[7] = ( 1.0 - X1 * X1 ) * ( 1.0 - X2 ) * 0.5 ; 


    # Derivative of shape functions for the second-order quad element
    def Derivative_Shape_Func_2D_8N_def(self, DFXI, X1, X2):
        
        DFXI[0][0] =  ( 1.0 - X2 ) * (   2.0 * X1 - X2 ) * 0.25 ; 
        DFXI[0][1] =  ( 1.0 + X1 ) * ( - X1 + 2.0 * X2 ) * 0.25 ; 
        DFXI[1][0] =  ( 1.0 + X2 ) * (   2.0 * X1 + X2 ) * 0.25 ; 
        DFXI[1][1] =  ( 1.0 + X1 ) * (   X1 + 2.0 * X2 ) * 0.25 ; 
        DFXI[2][0] =  ( 1.0 + X2 ) * (   2.0 * X1 - X2 ) * 0.25 ; 
        DFXI[2][1] =  ( 1.0 - X1 ) * ( - X1 + 2.0 * X2 ) * 0.25 ; 
        DFXI[3][0] =  ( 1.0 - X2 ) * (   2.0 * X1 + X2 ) * 0.25 ; 
        DFXI[3][1] =  ( 1.0 - X1 ) * (   X1 + 2.0 * X2 ) * 0.25 ; 

        DFXI[4][0] =  ( 1.0 - X2 * X2 ) * 0.5 ; 
        DFXI[4][1] = -( 1.0 + X1 ) * X2 ;
        DFXI[5][0] = -( 1.0 + X2 ) * X1 ;
        DFXI[5][1] =  ( 1.0 - X1 * X1 ) * 0.5 ; 
        DFXI[6][0] = -( 1.0 - X2 * X2 ) * 0.5 ; 
        DFXI[6][1] = -( 1.0 - X1 ) * X2 ;
        DFXI[7][0] = -( 1.0 - X2 ) * X1 ;
        DFXI[7][1] = -( 1.0 - X1 * X1 ) * 0.5 ; 

