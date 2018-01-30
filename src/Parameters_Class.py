
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


class Shape_Function_Class:

    # Shape function of the quad element
    def Shape_Func_2D_4N_def(self, FN, X1, X2):

        FN[0] = ( 1.0 + X1 ) * ( 1.0 - X2 ) * 0.25
        FN[1] = ( 1.0 + X1 ) * ( 1.0 + X2 ) * 0.25
        FN[2] = ( 1.0 - X1 ) * ( 1.0 + X2 ) * 0.25
        FN[3] = ( 1.0 - X1 ) * ( 1.0 - X2 ) * 0.25

    # Derivative of shape functions for the quad element
    def Derivative_Shape_Func_2D_4N_def(self, DFXI, X1, X2):

        DFXI[0][0] = + ( 1.0 - X2 ) * 0.25
        DFXI[0][1] = - ( 1.0 + X1 ) * 0.25
        DFXI[1][0] = + ( 1.0 + X2 ) * 0.25
        DFXI[1][1] = + ( 1.0 + X1 ) * 0.25
        DFXI[2][0] = - ( 1.0 + X2 ) * 0.25
        DFXI[2][1] = + ( 1.0 - X1 ) * 0.25
        DFXI[3][0] = - ( 1.0 - X2 ) * 0.25
        DFXI[3][1] = - ( 1.0 - X1 ) * 0.25

    # Shape functions of the triangle element
    def Shape_Func_2D_3N_def(self, FN, X1, X2):

        FN[0] = 1.0 - X1 - X2
        FN[1] = X1
        FN[2] = X2

    # Derivative of the shape function of the triangle
    def Derivative_Shape_Func_2D_3N_def(self, DFXI, X1, X2):

        DFXI[0][0] = -1.0
        DFXI[0][1] = -1.0
        DFXI[1][0] = +1.0
        DFXI[1][1] =  0.0
        DFXI[2][0] =  0.0
        DFXI[2][1] = +1.0


        