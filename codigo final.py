import os
import time
import random
from tkinter import *
############################################################################################################################################################################################################################################################################################
def borrarPantalla():
  if os.name=="posix":
    os.system("clear")
  else:
    os.system("cls")

def mostrarMapa():
  mapa=input("¿desea abrir el mapa?")
  if mapa=="si" or mapa== "Si":
    print("a continuacion, el mapa general, con los respectivos soldados")
    print(mapaGeneral)
    print("en otra ventana se esta mostrando el mapa de la U, el programa no continuara hasta que cierres el mapa\n")
    ventana=Tk()
    ventana.geometry("500x500")
    imagen=PhotoImage(file="mapaunal.png")
    fondo=Label(ventana,image=imagen).place(x=0,y=0)
    ventana.mainloop()
#######################################################################################################################################################################################################################################################################
EquipoAdministrativos={101:"Torre de enfermería", 102:"Biblioteca central", 103:"División de registro", 251:"Capilla", 207:"Museo Leopoldo Rother", 408: "Cade", 413:"Observatorio"}
EquipoSociales={201:"Facultad de Derecho", 205:"Depar. de Sociología", 214:"Edificio Antonio Nariño", 217 :"Edificio Francisco de Paula", 212:"Facultad de Ciencias Humanas", 310:"Facultad de Ciencias Económicas"}
EquipoMedicina={210:"Facultad de Odontología", 228: "Facultad de Enfermería ", 450: "Farmacia", 471:"Medicina", 476:"Ciencias", 481 :"Facultad de Veterinaria", 503:"Anfiteatro Anatomía ", 555:"Auditorio Alexis Omaña"}
EquipoArtes={301:"Escuela de Bellas Artes", 303:"edificio demolido arquitectura", 305:"conservatorio",104:"Auditorio Leon de Greiff", 314 :"SINDU", 317:"Museo de Arte", 701:"Escuela de Cine y Televisión",731:"Estadio"}
EquipoIngenieria = {401: "facultad de ingeniería", 406: "IEI", 411: "Laboratorios Ingenieria",412: "Laboratorios de quimica", 409: "Laboratorios de hidráulica", 451: "Quimica", 453: "aulas ing", 454: "CyT", 407: "Posgrado Materiales y Procesos", 405:"Takeuchi"}


#Cercanos A territorios del equipo de administrativos
cercanoA101=[102, 103, 104, 305, 317, 251]
cercanoA102=[201, 471, 450, 104, 101, 103, 205]
cercanoA103=[102, 101, 207, 205, 251, 317, 201]
cercanoA251=[317, 305, 101, 103, 207, 217]
cercanoA207=[217, 103, 205, 214, 212, 251, 317]
cercanoA408=[405, 310, 409, 411, 406, 303, 407]
cercanoA413=[701, 453, 412, 411, 406, 407]
#Cercanos a territorios del equipo sociales
cercanoA201=[228, 471, 102, 103, 205]
cercanoA205=[228, 201, 102, 212, 210, 207, 214, 217, 103]
cercanoA214=[212, 217, 207, 205]
cercanoA217=[207, 214, 205, 251]
cercanoA212=[205, 214, 210]
cercanoA310=[303, 408, 405, 314, 305, 409]
#Cercanos a territorios del equipo medicina
cercanoA210=[503, 228, 201, 205, 212]
cercanoA228=[481, 503, 201, 205, 210, 212, 471, 555]
cercanoA450=[451, 401, 471]
cercanoA471=[201, 481, 228, 450, 451, 401, 102, 476, 104]
cercanoA476=[471, 481, 454, 451, 555]
cercanoA481=[476, 471, 228, 503, 555]
cercanoA503=[228, 210, 555]
cercanoA555=[476, 481, 471, 228, 503]
#Cercanos a territorios del equipo artes
cercanoA301=[303, 104, 305, 401, 102, 471]
cercanoA303=[314, 305, 104, 301, 401, 405, 408, 409, 310]
cercanoA305=[104, 301, 303, 317, 310, 314, 101]
cercanoA104=[101, 301, 102, 305, 103, 471]
cercanoA314=[317, 305, 303, 310]
cercanoA317=[314, 305, 101, 103, 251, 207, 217]
cercanoA701=[731, 453, 413, 454]
cercanoA731=[701, 453, 454, 476]
#Cercanos a territorios del equipo de ingenieria
cercanoA401=[471, 450, 451, 301, 405, 406, 303, 412, 104, 102]
cercanoA406=[453, 411, 409, 405, 408, 412]
cercanoA411=[413, 407, 409, 408, 406, 412, 453]
cercanoA412=[453, 411, 406, 413, 451, 405, 401, 450, 454]
cercanoA409=[408, 406, 411, 407, 310]
cercanoA451=[454, 453, 412, 451, 401, 450, 471, 476]
cercanoA453=[454, 451, 412, 413, 406, 411, 731, 701]
cercanoA454=[701, 731, 453, 451, 476, 412]
cercanoA405=[303, 401, 408, 406, 310, 301, 412]
cercanoA407=[413, 411, 406, 405, 408, 409]

TerrenoCercanoA={101:cercanoA101, 102:cercanoA102, 103:cercanoA103, 251:cercanoA251, 207:cercanoA207, 408:cercanoA408, 413:cercanoA413, 201:cercanoA201, 205:cercanoA205, 214:cercanoA214, 217:cercanoA217, 212:cercanoA212, 310:cercanoA310, 210:cercanoA210, 228:cercanoA228, 450:cercanoA450, 471:cercanoA471, 476:cercanoA476, 481:cercanoA481, 503:cercanoA503, 555:cercanoA555, 301:cercanoA301, 303:cercanoA303, 305:cercanoA305, 104:cercanoA104, 314:cercanoA314, 317:cercanoA317, 701:cercanoA701, 731:cercanoA731, 401:cercanoA401, 406:cercanoA406, 411:cercanoA411, 412:cercanoA412, 409:cercanoA409, 451:cercanoA451, 453:cercanoA453, 454:cercanoA454, 405:cercanoA405, 407:cercanoA407}

########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
territoriosAdministrativos={}
territoriosSociales={}
territoriosMedicina={}
territoriosArtes={}
territoriosIngenieria={}

mapaGeneral=[territoriosAdministrativos,territoriosSociales,territoriosMedicina,territoriosArtes,territoriosIngenieria]

global totalLugares
totalLugares=len(EquipoAdministrativos)+len(EquipoSociales)+len(EquipoMedicina)+len(EquipoArtes)+len(EquipoIngenieria)


for i in EquipoAdministrativos:
    territoriosAdministrativos[i]=[]
for i in EquipoSociales:
    territoriosSociales[i]=[]
for i in EquipoMedicina:
    territoriosMedicina[i]=[]
for i in EquipoArtes:
    territoriosArtes[i]=[]
for i in EquipoIngenieria:
    territoriosIngenieria[i]=[]

    
global jugadores
jugadores={}


global Soldados
Soldados={}

    
def añadir_jugador():
    global b
    global JUGCOD
    NJugador1=0
    NJugador2=0
    NJugador3=0
    NJugador4=0
    NJugador5=0
    while True:
      try:
        b=int(input("Seleccione la cantidad de jugadores, recuerde que mínimo deben ser 2 y máximo 5 -->"))
        break
      except ValueError:
        print("Esta pregunta solo acepta valores enteros")
        time.sleep(2)
        borrarPantalla() 
    Jugadores=[]	
    Jugcod=[NJugador1,NJugador2,NJugador3,NJugador4,NJugador5]
    JUGCOD=[]
    if b> 5 or b<2:
        print("Esa cantidad no esta permitida\n\n")
        time.sleep(2)
        borrarPantalla()
        añadir_jugador()
    else:
        for i in range(b):
          Jugadores.append(input(f"\n Jugador {i+1}, ingresa tu nombre de usuario -->"))
        for i in range(len(Jugadores)):
            for j in range(len(Jugcod)):
                if i==j:
                    Jugcod[j]=Jugadores[i]
        for i in range(len(Jugadores)):
            JUGCOD.append(Jugcod[i])
        borrarPantalla()            
  


def agregar_SoldadosTerritorios_inicio(numeroDeJugadores):
    for i in range(numeroDeJugadores):
        Soldados[i+1]=22
    for i in range(numeroDeJugadores):
        jugadores[i+1]=[]
    global nombre

def evaluar_a_que_territorio_pertenece_un_edificio(e):
    global territorio
    for i in territoriosAdministrativos:
        if i==e:
            territorio=territoriosAdministrativos
        else:
            pass
    for i in territoriosSociales:
        if i==e:
            territorio=territoriosSociales
        else:
            pass
    for i in territoriosMedicina:
        if i==e:
            territorio=territoriosMedicina
        else:
            pass
    for i in territoriosArtes :
        if i==e:
            territorio=territoriosArtes
        else:
            pass
    for i in territoriosIngenieria:
        if i==e:
            territorio=territoriosIngenieria
        else:
            pass





def elegir_territorios(j):
    nombre=JUGCOD[j-1]
    global totalLugares
    zona=False
    edificio=False
    print(f"{nombre}, seleccione un teritorio\n\n")
    while zona==False or edificio==False:
      print("1.Administrativos")
      print("2.Sociales")
      print("3.Medicina")
      print("4.Artes")
      print("5.Ingieniería")
      print()
      while True:
        try:
          z=int(input("¿En qué zona desea agregar primero sus soldados?-->"))
          break
        except ValueError:
          print("Esta pregunta solo acepta valores enteros")
      if z==1:
        m=territoriosAdministrativos
      elif z==2:
        m=territoriosSociales
      elif z==3:
        m=territoriosMedicina
      elif z==4:
        m=territoriosArtes
      elif z==5:
        m=territoriosIngenieria
      if z!=1 and z!=2 and z!=3 and z!=4 and z!=5:
        print("La zona que elegiste no existe\n\n")
        time.sleep(2)
        borrarPantalla() 
      else:
        zona=True
        print("estos son los edificios disponibles que se encuentran en la zona, si ves que todos estan ocupados, presiona 1 para cambiar de zona")
        for i in m:
            if m[i]:
                pass
            else:
                print(i)
            
        while True:
          try:
            y=int(input("¿En qué edificio desea colocar sus soldados?-->"))
            break
          except ValueError:
            print("Esta pregunta solo acepta valores enteros")
        if y not in m:
          print("Este edificio no se encuentra en esta zona\n\n")
          time.sleep(2)
          borrarPantalla() 
        else:
          if m[y]:
              print("En esta ronda solo puedes escoger edificios vacios, este esta ocupado\n\n")
              time.sleep(2)
              borrarPantalla()
          else:
             edificio=True   
    m[y].append(j)
    nsa=Soldados[j]-1
    Soldados[j]=nsa
    print(f"Felicidades {nombre}, te apoderaste de el edificio {y}\n\n")
    totalLugares-=1
    time.sleep(2)
    borrarPantalla()
    


def evaluar_territorios(k):
    jugadores[k]=[]
    for i in territoriosAdministrativos:
        for j in territoriosAdministrativos[i]:
            if j==k:
                jugadores[k].append(i)
                break
        else:
            pass
    for i in territoriosSociales :
        for j in territoriosSociales[i]:
            if j==k:
                jugadores[k].append(i)
                break
        else:
            pass
    for i in territoriosMedicina:
        for j in territoriosMedicina[i]:
            if j==k:
                jugadores[k].append(i)
                break
        else:
            pass
    for i in territoriosArtes :
        for j in territoriosArtes[i]:
            if j==k:
                jugadores[k].append(i)
                break
    for i in territoriosIngenieria :
      for j in territoriosIngenieria[i]:
        if j==k:
          jugadores[k].append(i)
          break
        else:
            pass




def agregar_soldados_comienzo_de_ronda(j):
  if len(jugadores[j])<9:
    sn=3
  else:
    sn=int(len(jugadores[j])/3)
  Soldados[j]=sn
    
        


def agregar_soldados_a_territorio(j):
    nombre=JUGCOD[j-1]
    global territorio
    print(f"{nombre}, agregue sus soldados\n\n")
    while Soldados[j]>0:
        edificio=False
        while edificio==False:
            print("Estos son tus territorios con sus respectivos soldados\n\n")
            for i in jugadores[j]:
              evaluar_a_que_territorio_pertenece_un_edificio(i)
              print(f" en {i} tienes {len(territorio[i])} soldados") 
              print()
            while True:
              try:
                z=int(input("¿En qué edificio deseas agregar tus soldados?-->"))   
                break
              except ValueError:
                print("Esta pregunta solo acepta valores enteros")     
            if z not in jugadores[j]:
                print("El edificio que elegiste no es tuyo!!, elige de nuevo\n\n")
                time.sleep(2)
                borrarPantalla()
            else:
                edificio=True
        cantidadAdecuada=False
        while cantidadAdecuada==False:
            while True:
                try:
                    y=int(input(f"¿Cuántos soldados deseas colocar?, recuerda que tienes {Soldados[j]} disponoible(s) -->"))
                    break
                except ValueError:
                    print("Esta pregunta solo acepta valores enteros")      
            if y>Soldados[j]:
                print("No tienes tantos soldados, intenta de nuevo\n\n")
                time.sleep(2)
                borrarPantalla()
            else:
                Soldados[j]=Soldados[j]-y
                cantidadAdecuada=True
        evaluar_a_que_territorio_pertenece_un_edificio(z)
        for i in range(y):
            territorio[z].append(j)
        borrarPantalla()
            
def redistribuir_soldados(j):
    nombre=JUGCOD[j-1]
    redistribuir=input(f"¿Desea mover sus soldados de posicion {nombre}?-->")
    print()
    if redistribuir=="si":
        posicionValida=False
        while posicionValida==False:
            print("Estos son sus territorios y sus soldados\n\n")
            for i in jugadores[j]:
              evaluar_a_que_territorio_pertenece_un_edificio(i)
              print(f" en {i} tienes {len(territorio[i])} soldados") 
              print()
            while True:
              try:
                desde=int(input("¿Desde cual edificio quiere mover soldados?-->"))
                break
              except ValueError:
                print("Esta pregunta solo acepta valores enteros")    
            evaluar_a_que_territorio_pertenece_un_edificio(desde)
            if desde not in jugadores[j]:
                print("No tienes soldados en este territorio\n\n")
                time.sleep(2)
                borrarPantalla()
            elif len(territorio[desde])==1:
                print("En este territorio solo tienes un soldado, no puedes moverlo\n\n")
                time.sleep(2)
                borrarPantalla
            else:
                cantidadCorrecta=False
                while cantidadCorrecta==False:
                     while True:
                       try:
                         cantidad=int(input(f"¿Cuantos soldados deseas mover desde aca?, recuerda que tienes {len(territorio[desde])} y que debes dejar mínimo 1 en el territorio base-->"))
                         break
                       except ValueError:
                         print("Esta pregunta solo acepta valores enteros")  
                     if cantidad>=len(territorio[desde]):
                         print("No tienes los soldados suficientes\n\n")
                         time.sleep(2)
                         borrarPantalla()
                     else:
                         print("estos son tus terrenos cercanos")
                         for i in TerrenoCercanoA[desde]:
                           for k in jugadores[j]:
                             if i==k:
                               print(i)
                         while True:
                           try:
                              hacia=int(input("¿Hacia dónde los deseas mover?-->"))
                              break
                           except ValueError:
                             print("Esta pregunta solo acepta valores enteros")  
                         if hacia not in TerrenoCercanoA[desde]:
                             print("Este terreno no esta cerca al que elegiste, intentalo de nuevo\n\n")
                             time.sleep(2)
                             borrarPantalla()
                         elif hacia not in jugadores[j]:
                             print("Este territorio no es tuyo, selecciona uno que si lo sea\n\n")
                             time.sleep(2)
                             borrarPantalla()
                         else:
                             for i in range(cantidad):
                                 evaluar_a_que_territorio_pertenece_un_edificio(desde)
                                 territorio[desde].remove(j)
                                 evaluar_a_que_territorio_pertenece_un_edificio(hacia)
                                 territorio[hacia].append(j)
                             cantidadCorrecta=True
                             posicionValida=True
                             redistribuir_soldados(j)
                             borrarPantalla()
    else:
        pass
        borrarPantalla()

def evaluar_si_un_territorio_cercano_son_de_uno(territorioelegido,j):
  noHayTerritorioParaAtacar=False
  for i in TerrenoCercanoA[territorioelegido]:
    if i not in jugadores[j]:
      break
    else:
      noHayTerritorioParaAtacar=True
  return noHayTerritorioParaAtacar
      
    
      
      
  
  
      
def ataque(Usuario):
    mostrarMapa()
    nombre=JUGCOD[Usuario-1]
    Desde=True
    while Desde==True:
        for i in jugadores[Usuario]:
            evaluar_a_que_territorio_pertenece_un_edificio(i)
            print(f"{nombre} en {i} tienes {len(territorio[i])} soldados")
        while True:
          try:
            desde=int(input("¿Desde dónde desea realizar el ataque?-->"))
            break
          except ValueError:
            print("Esta pregunta solo acepta valores enteros")  
        evaluar_a_que_territorio_pertenece_un_edificio(desde)
        NPAtacar=evaluar_si_un_territorio_cercano_son_de_uno(desde,Usuario)
        if desde not in jugadores[Usuario]:
            print("El territorio no se encuentra en su poder")
            time.sleep(2)
            borrarPantalla()
        elif len(territorio[desde]) <2:
            print("No puede atacar desde un territorio con menos de 2 soldados")
            time.sleep(2)
            borrarPantalla()
        elif NPAtacar==True:
          print("no hay territorios para atacar desde aqui")
          time.sleep(2)
          borrarPantalla()  
        else:
            print("\n cercanos estan...\n")
            for i in TerrenoCercanoA[desde]:
                evaluar_a_que_territorio_pertenece_un_edificio(i)
                print(f" en {i} estan los siguientes soldados{territorio[i]}\n")
            Hacia=True
            while Hacia==True:
              while True:
                try:
                  hacia=int(input("¿Hacia dónde dirige su ataque?-->"))
                  break
                except ValueError:
                  print("Esta pregunta solo acepta valores enteros")  
              if hacia not in TerrenoCercanoA[desde]:
                  print("El territorio no se encuentra cerca para atacarlo\n\n")
                  time.sleep(2)
                  borrarPantalla()
              elif hacia in jugadores[Usuario]:
                  print("Usted ya posee ese territorio\n\n")
                  time.sleep(2)
                  borrarPantalla()
              else:
                NoSoldados=True
                while NoSoldados==True:
                  while True:
                    try:
                      numeroSoldados=int(input("¿Con cuántos soldados planea atacar?-->"))
                      break
                    except ValueError:
                      print("Esta pregunta solo acepta valores enteros")
                  evaluar_a_que_territorio_pertenece_un_edificio(desde)
                  if numeroSoldados>= len(territorio[desde]):
                    print("No tiene suficientes soldados en el territorio\n\n")
                    time.sleep(2)
                  elif numeroSoldados<1:
                    print("Debe atacar con al menos ún soldado\n\n")
                    time.sleep(2)
                  elif numeroSoldados>3:
                    print("No puede atacar con mas de tres soldados\n\n")
                    time.sleep(2)
                  else:
                    print(f"{nombre} ataca el territorio {hacia} con {numeroSoldados} soldados\n\n")
                    DadosAtaque= dados(numeroSoldados)
                    Desde=False
                    Hacia=False          
                    NoSoldados=False
                    return desde, hacia, DadosAtaque
                    time.sleep(2)
                    borrarPantalla()
                                
        
def defensa(defender):
    for i in jugadores:
        if defender in jugadores[i]:
            Defensor=i
    nombre=JUGCOD[Defensor-1]
    Defensa=True
    evaluar_a_que_territorio_pertenece_un_edificio(defender)
    print(f"{nombre}, el territorio a defender tiene {len(territorio[defender])} soldados\n\n")
    while Defensa==True:
      while True:
        try:
          NoDefensa=int(input(f"{nombre}, ¿con cuantos soldados vas a defender?-->"))
          break
        except ValueError:
          print("Esta pregunta solo acepta valores enteros") 
      if NoDefensa<1:
          print("Se tiene que defender con al menos un soldado\n\n")
      elif NoDefensa>2:
          print("Solamente se puede defender con dos soldados\n\n")
      else:
          print(f"{Defensor} se defiende con {NoDefensa} soldados\n\n")
          print(jugadores)
          DadosDefensa=dados(NoDefensa)
          Defensa=False
          return DadosDefensa
          time.sleep(2)
          borrarPantalla()
          
        


def Comparar_Dados(Attack,Defense):
    pierde_defensa=0
    pierde_ataque=0
    for i in range(len(Defense)):
        if len(Attack)>0:
            if Attack[0]>Defense[0]:
                pierde_defensa+=1
            else:
                pierde_ataque+=1 
            Attack.pop(0)
            Defense.pop(0)
        else:
            break
    print(f"La defensa pierde {pierde_defensa} soldados, y los invasores {pierde_ataque} soldados\n\n")
    return  pierde_defensa, pierde_ataque
    time.sleep(5)
    borrarPantalla()

def resultado_dados(pierde_defensa,pierde_ataque,hacia,desde,j):
    nombre=JUGCOD[j-1]
    for i in range(pierde_defensa):
        evaluar_a_que_territorio_pertenece_un_edificio(hacia)
        territorio[hacia].pop()
    for i in range(pierde_ataque):
        evaluar_a_que_territorio_pertenece_un_edificio(desde)
        territorio[desde].pop()
    evaluar_a_que_territorio_pertenece_un_edificio(hacia)    
    if territorio[hacia]:
        pass
    else:
        territorio[hacia].append(j)
        print(f"{nombre} ha conquistado el territorio {hacia}\n\n")
        for o in jugadores:
            evaluar_territorios(o)
    time.sleep(5)
    borrarPantalla()
      	

def dados(CDados):
    Dados=[]
    for i in range(CDados):
        Dados.append(random.randint(1,6))
    Dados.sort()
    Dados.reverse()
    return Dados        
########################################################################################################################################################################################################

print("Bienvenido al juego Risk Unal, el objetivo es conquistar de manera no pacífica todos los territorios disponibles del campus, saca tu capucho estratega interno. Este juego necesita de mucha concentración, y te recomendamos que cada jugador tenga una hoja de papel al lado y en otra pestaña el mapa que se adjunto con este código, lo van a necesitar. Esperemos lo disfrutes.\n\n")
Partida=False
while Partida == False:
    print("A continuación seleccione una de las opciones.\n\n")
    print("1. Iniciar el juego")
    print("2. Ver el mapa")
    print("3. Ver lista de territorios")
    print("4. Salir del programa\n")
    while True:
      try:
        a=int(input("-->"))
        if a!=1 and a!=2 and a!=3 and a!=4:
          print("Porfavor elige un numero de la lista")
        else:
          break
      except ValueError:
        print("Porfavor elige un numero de la lista")
        time.sleep(1)
    print()
    borrarPantalla()
    if a==1:
        ListaDeJugadores=añadir_jugador()
        agregar_SoldadosTerritorios_inicio(b)
        print("A continuación, se van a turnar cada jugador para escoger edificios, cada jugador escogerá hasta que todos los edificios tengan un dueño\n\n")
        while totalLugares>0:
            for i in Soldados:
                if totalLugares==0:
                    break
                else:
                    elegir_territorios(i)
        for i in jugadores:
            evaluar_territorios(i)
        for i in Soldados:
          while Soldados[i]>0:
            agregar_soldados_a_territorio(i)
        Juego=True
        print("\n Que empiece el juego")
        time.sleep(2)
        borrarPantalla
        while Juego==True:
          for i in jugadores:
            if jugadores[i]==[]:
              jugadores.pop(i)
              Soldados.pop(i)
          for i in jugadores:
            if jugadores[i]:
              agregar_soldados_comienzo_de_ronda(i)
              name=JUGCOD[i-1]
              agregar_soldados_a_territorio(i)
              Response=input(f"{name}, ¿Desea atacar?-->")
              while Response=="si" or Response=="Si" or Response=="yes" or Response=="SI":
                  TerritorioInvadir,TerritorioInvadido,DadosAtaque=ataque(i)
                  DadosDefensa=defensa(TerritorioInvadido)
                  print(f"los dados del atacante son: {DadosAtaque}\n Los dados de la defensa son: {DadosDefensa}")
                  pierde_defensa, pierde_ataque=Comparar_Dados(DadosAtaque,DadosDefensa)
                  resultado_dados(pierde_defensa,pierde_ataque,TerritorioInvadido,TerritorioInvadir,i)
                  if len(jugadores[i])<totalLugares2:
                    Response=input(f"{name}, ¿desea seguir atacando?-->")
                    if Response=="si" or Response=="Si" or Response=="yes" or Response=="SI":
                      pass
                    else:
                      redistribuir_soldados(i)
                  else:
                    Response="no"
                    Juego=False
              else:
                pass
        Clave=jugadores.keys()
        for i in Clave:
            ClaveGanador=i
        Ganador=JUGCOD[ClaveGanador-1]
        print(f"felicidades {Ganador}, usted es el capucho mas áspero de este chuzo, no se deje meter miedo de los tombos del esmad, ni se deje meter un gancho ciego de ningun bobo güevon, la buena perro\n\n")
        Partida=True
    elif a==2:
      mostrarMapa()
      borrarPantalla()
 
    elif a==3:
      print("El juego consta de 5 equipos")
      print("Equipo de Administrativos: ",EquipoAdministrativos)
      print()
      print("Equipo de Sociales: ", EquipoSociales)
      print()
      print("Equipo de Medicina: ",EquipoMedicina)
      print()
      print("Equipo de Artes: ", EquipoArtes)
      print()
      print("Equipo de Ingeniería: ", EquipoIngenieria)
      input("\npresione enter para continuar")
      borrarPantalla()

    elif a==4:
      Partida=True
      print("saliste del juego")

input()
