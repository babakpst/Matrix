
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

class Mass_Matrix_Class:

    def __int__(self)
        pass

    def Mass_2D_4N(self,
                   IEL, NNode, NDim, NInt,                \   # ! Integer Variables
                   Rho,                                   \   # ! Real Variables
                   XT, ME,                                \   # ! Real Arrays
                   GAUSS_PNT                              \   # ! Type 
                   ):

        # Import built-in libraries ================================================================
        import numpy as np

        # Import user-defined modules ==============================================================
        import Parameters_Class

        # Define arrays ============================================================================


        # Code =====================================================================================
        Parameters = Parameters_Class.Parameters_Class()


        # Integrate over integration points
        for LY in range(NInt):

        DO LY = 1, NInt ;
            SF%X2  = GAUSS_PNT%XINT ( LY ) ;
            WY     = GAUSS_PNT%WINT ( LY ) ;

            DO LX = 1, NInt ;
                SF%X1  = GAUSS_PNT%XINT ( LX ) ;
                WX     = GAUSS_PNT%WINT ( LX ) ;

                WSTAR  = WX * WY ;

                ! SHAPE FUNCTIONS AND DIFFERENTIAL OF SHAPE FUNCTIONS
                !Call     ShapeFuncSub (  SF ) ;
                !Call DIF_ShapeFuncSub ( DSF ) ;
                SF%FN    =     ShapeFunc_2_4 (  SF%X1,  SF%X2 ) ;
                DSF%DFXI = Dif_ShapeFunc_2_4 ( DSF%X1, DSF%X2 ) ;

                DJ   = MATMuL ( XT, DSF%DFXI ) ;
                DETJ = DJ ( 1, 1 ) * DJ ( 2, 2 ) - DJ ( 2, 1 ) * DJ ( 1, 2 ) ;
                FAC  = WSTAR * DETJ ;

                IF ( DETJ <= 0.0_DBL ) Then ;
                    Write(*,"('ELEMENT NUMBER',3I6,'|J|<0  -ERROR-', 'DETJ = ',E17.10)" ) IEL, LX, LY, DETJ ;
                    Write(*, Fmt_End) ; Read(*,*) ;  STOP ;
                End If ;

                ! CALCULATING THE INVERSE OF THE JACOBIAN
                !#Call DLINRG (NDim,DJ,NDim,DJI,NDim) ;
                DJI ( 1, 1 ) =   DJ ( 2, 2 ) ;
                DJI ( 2, 2 ) =   DJ ( 1, 1 ) ;
                DJI ( 1, 2 ) = - DJ ( 1, 2 ) ;
                DJI ( 2, 1 ) = - DJ ( 2, 1 ) ;

                DJI = DJI  / DETJ ;

                DFX = MATMuL ( DSF%DFXI, DJI ) ;

                !#Phi_Phi_T   = MATMuL ( SF%FN, TRANSPOSE (SF%FN) )                * FAC ;
                !#PhiX_PhiX_T = MATMuL ( DFX (:, 1), TRANSPOSE ( DFX ( : , 1 ) ) ) * FAC ;
                !#PhiY_PhiY_T = MATMuL ( DFX (:, 1), TRANSPOSE () )                * FAC ;
                !#PhiX_PhiY_T = MATMuL ( DFX (:, 1), TRANSPOSE (DFX ( : , 2 )) )   * FAC ;
                !#PhiY_PhiX_T = MATMuL ( DFX (:, 2), TRANSPOSE (DFX ( : , 1 )) )   * FAC ;

                DO I = 1, NNode   ;
                    DO J = 1, NNode ;
                        Phi_Phi_T   ( I, J ) = SF%FN ( I )     * SF%FN ( J )     * FAC ;
                    End Do ;
                End Do ;

                ! MASS MATRIX
                ForAll ( I = 1:NNode, J = 1:NNode, K = 1:NDim ) ME ( ( K -1 ) * NNode + I, ( K -1 ) * NNode + J ) = ME ( ( K -1 ) * NNode + I, ( K -1 ) * NNode + J ) + Rho * Phi_Phi_T ( I, J ) ;




            End Do ;
        End Do ;



!#Write(*    ,*) 'End Subroutine < MassDampStiffSLD_2D_4N >' ;
!#Write(UnInf,*) 'End Subroutine < MassDampStiffSLD_2D_4N >' ;
Return ;
End Subroutine MassDampStiffSLD_2D_4N ;



! - Real Arrays -------------------------------------------------------------------------------------------------------------------------------------
Real (Kind=DBL)      :: XI ( 2 ) ;                ! Temprary variable for Gauss points
Real (Kind=DBL)      :: DJ ( NDim, NDim ) ;       ! Jacobian Matrix
Real (Kind=DBL)      :: VN ( 2 ) ;                ! Normal vector
Real (Kind=DBL)      :: DJI ( NDim, NDim )        ! Inverse of Jacobian Matrix
Real (Kind=DBL)      :: DFX ( NNode, NDim )       ! Temprary Matrix
Real (Kind=DBL)      :: Phi_Phi_T ( NNode, NNode ), PhiX_PhiX_T ( NNode, NNode ), PhiY_PhiY_T ( NNode, NNode ), PhiX_PhiY_T ( NNode, NNode ), PhiY_PhiX_T ( NNode, NNode ) ;

! - Complex Variables -------------------------------------------------------------------------------------------------------------------------------
!#Complex  ::  ;
! - Character Variables -----------------------------------------------------------------------------------------------------------------------------
!#Character   ::  ;
! - Logical Variables -------------------------------------------------------------------------------------------------------------------------------
!#Logical   ::  ;

! - Type DECLERATIONS -------------------------------------------------------------------------------------------------------------------------------
Type (  SF_2_4 ) ::  SF ;  ! SHAPE FUNCTION
Type ( DSF_2_4 ) :: DSF ;  ! DIFFERENTIALS OF SHAPE FUNCTION