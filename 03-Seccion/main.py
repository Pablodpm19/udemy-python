nombre = input("Introduce tu nombre:\n")

print(f"\nHola {nombre}, Bienvenido a:")

print('''
                    _                      
                   | |                     
                 __| | ___   ___  _ __ ___ 
                / _` |/ _ \ / _ \| '__/ __|
               | (_| | (_) | (_) | |  \__ \         
                \__,_|\___/ \___/|_|  |___/
''')

comenzar = input(f"\n{nombre}, Eres una rescatista profesional y tu trabajo\nes encontrar a la pequeña Charlotte que se extravio\nen una casa un poco extraña.\n\n¿Deseas comenzar tu busqueda? SI o NO:\nR:").lower()

if comenzar == "si":
  print("\nEmpecemos...")
  
  print('''  
            __________       __________  
           |  __  __  |     |  __  __  |
           | |  ||  | |     | |  ||  | |
           | |  ||  | |     | |  ||  | |
           | |__||__| |     | |__||__| |
           |  __14__()|     |  __37__()|
           | |  ||  | |     | |  ||  | |
           | |  ||  | |     | |  ||  | |
           | |  ||  | |     | |  ||  | |
           | |  ||  | |     | |  ||  | |
           | |__||__| |     | |__||__| |
           |__________|     |__________|
              (Azul)           (Roja)
''')
  
  puerta = input(f"{nombre}, Frente de ti veras dos puertas, una de color rojo\ny otra de azul. En una de ella encontraras la entrada\nsegura a tu muerte, en la otra, te permitira seguir\nen tu busqueda de la pequeña Charlotte.\n\nTendras que elegir una de ellas para continuar.\n\n¿En que puerta deseas entrar? Azul o Roja:\nR:").lower()
  
  if puerta == "roja":
    print('''\n           ____    ____    ____    ____
          |2   |  |5   |  |9   |  |3   |
          |(\/)|  | /\ |  | /\ |  | &  |
          | \/ |  | \/ |  |(__)|  |&|& |
          |   2|  |   5|  | /\9|  | | 3|            
          `----`  `----'  `----'  `----' ''')
    
    tarj_acces = int(input(f"\n{nombre}, acabas de entrar a una habitación donde lo unico\nque hay son 4 naipes lon cuales son tarjeta de acceso\npara la puerta que se encuentra al final de la habitación,\nelige la tarjeta correcta.\nTen cuidado, en la pantalla de la puerta dice solo 1 intento.\n¿Cual tarjeta vas a introducir? 2; 5; 9; 3 :\nR:"))
    
  else:
    print("\nEntraste  a la habitación y te mataron perros asesinos")
    
    print('''     /\.-./~\       
    (o//o)|  \-._         .-"-.
    .~.'~ |  |    )`-----'     \._
   (").'/.|  |          (      /-.\          
    (_/-' \_/    |       \    |   \\          
           \ /  /   ____.-\  /     ))
           /\| /_.-'      \\ \    ((        
          // ||            \\ \    \|
          \\ ||'           // \\               
          (/ ||          _//   \\        
          " (_/         (_/   (_/     
            "           "     "''')
    
    print("GAME OVER")
  
    if tarj_acces == 9:
      print('''        _____________        _____________
       /      _      \      /      _      \    
       [] :: (_) :: []      [] :: (_) :: []
       [] ::::::::: []      [] ::::::::: []
       [] ::::::::: []      [] ::::::::: []
       [] :::123::: []      [] :::234::: []
       [] ::::::::: []      [] ::::::::: []
       [_____________]      [_____________]
           I     I              I     I
           I_   _I              I_   _I
            /   \                /   \    
            \   /                \   /
            (   )                (   )
            / A \                / B \    
            \___/                \___/     ''')
    
    llave_final = input(f"\n{nombre}, Acabas de entrar a la ultima habitación.\nlo unico que se llega a observar es dos llaves colgadas en la mitad de la habitación y una puerta al final de la misma.\nhay que introducir una de las 2 llaves\nTen cuidado pones la llave equivocada puede provocar un desastre\n¿Que llave deseas introducir? A o B:\n").lower()
    
    else:
    print("\nTARJETA INCORRECTA\n\nla habitación se lleno de agua provocandote la muerte\n\nGAME OVER")
    print('''                 ___
               /`  _\        
               |  x x|--.          
          -   / \_|0`/ /.`'._/)
      - ~ -^_| /-_~ ^- ~_` - -~ _
      -  ~  -| |   - ~ -  ~  -
             \ \, ~   -   ~
              \_| ''')
    
  if llave_final == "a":
    print(("\n¿ah...?\n"))
    
    print('''                ._________________.
                |.---------------.|
                ||               ||
                ||   PASSWORD    ||
                ||  *  *  *  *   ||
                ||               ||
                ||               ||
                ||_______________||
                /.-.-.-.-.-.-.-.-.\      
               /.-.-.-.-.-.-.-.-.-.\      
              /.-.-.-.-.-.-.-.-.-.-.\      
             /______/__________\___o_\      
             \_______________________/''')
    
    clave_final = int(input('\n!Espera¡\nAcaba de aparecer una laptop al lado de la\npuerta con una mensaje que dice:\n"INTRODUZCA CLAVE:* * * *"\ncon una pista que dice:\n"La clave de la vida son las buenas decisiones que tomamos"\nLa laptop pide una clave de 6 digitos, ten cuidado,\nsolo tienes 1 intento.\nINTRODUZCA LA CLAVE POR FAVOR:\n'))
    
  if clave_final == 379234:
    print('\n!CLAVE CORRECTA¡\n')

    print(f"\n¡Felicidades {nombre}! encontraste a la pequeña Charlotte\nEres un gran rescatista")
    
    print('''    (((')))
   (((o o)))
  (((( u ))))
  ((((\-/))))
    __,H,__
   /  \_/  \    
   ||  *  ||
   ||  *  ||
   WW  *  WW
    /     \    
   /_______\    
     || ||
    _|| ||_
   (__| |__)''')

    print("YOU WIN")
    
  else:
    print("\nacabas de morir incendiado\nGAME OVER\n")
    print('''
               (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ''')

else:
  print("Regresa cuando estes listo")