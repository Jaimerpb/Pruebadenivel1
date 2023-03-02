import  unittest
from  Vehiculos.Coche  import  Coche


class  TestCoche( unittest . TestCase ):
    def  test_coche( self ):
        coche = Coche( "rojo" ,  4 ,  120 ,  1000 )
        self . assertEqual ( coche . color ,  "rojo")
        self . assertEqual ( coche . ruedas ,  4 )
        self . assertEqual ( coche . velocidad , 120 )
        self . assertEqual ( coche . cilindrada , 1000 )
        self . assertEqual ( str ( coche ),  "rojo, 4 ruedas, 120 km/h, 1000cc" )
        
