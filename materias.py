#ESTO ES UN SCRIPT ECHO POR EP
import requests
import os
from colorama import init, Fore, Back, Style
def bp():
    if os.name == "posix":
       os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
       os.system ("cls")
       
def banner():
    bp()
    print("\033[1;33m"+"                 (      (                    )         (     \n             )\ )   )\ )     (        ( /(         )\ )  \n            (()/(  (()/(     )\       )\())  (    (()/(  \n             /(_))  /(_)) ((((_)(    ((_)\   )\    /(_)) \n            (_))   (_))    )\ _ )\  __ ((_) ((_)  (_))   \n            / __|  | |     (_)_\(_) \ \ / / | __| | _ \  \n            \__ \  | |__    / _ \    \ V /  | _|  |   /  \n            |___/  |____|  /_/ \_\    |_|   |___| |_|_\  \n"+'\033[0;m')
#COLORES
reset='\033[0;m'
rojo="\033[1;31m"
verde="\033[1;32m"
amarillo="\033[1;33m"
azul="\033[1;34m"
morado="\033[1;35m"
cian="\033[1;36m"
blanco="\033[1;37m"
while True:
    banner()
    print(azul+ "Inserte"+reset +" 0 AYUDA")
    print(azul+ "Inserte"+reset +" 1 MATEMATICA")
    print(azul+ "Inserte"+reset +" 2 FICICA")
    print(azul+ "Inserte"+reset +" 3 INGLES")
    print(azul+ "Inserte"+reset +" 4 LENGUAJE")
    print(azul+ "Inserte"+reset +" 5 AUTOCAT")
    print(azul+ "Inserte"+reset +" 6 SEGURIDAD")
    print(azul+ "Inserte"+reset +" 7 INFORMATICA")
    print(azul+ "Inserte"+reset +" 8 SALIR")
    CORRECTOR_INICIAL=input("Inserte >>")
#SALIR MENU INICIAL
    if CORRECTOR_INICIAL == "8" or CORRECTOR_INICIAL == "salir":
        print("ADIOS")
        break
#MATEMATICAS
    if CORRECTOR_INICIAL == "0" or CORRECTOR_INICIAL == "matematicas":
        while True:
            banner()
            print(amarillo +"Inserte"+ reset +"01 OPERACIONES BASICAS-ECUACIONES")
            print(amarillo +"Inserte"+ reset +"02 DISIBILIDAD- MINIMO COMUN MULTIPLO Y MAXIMO COMUN DIVISOR")
            print(amarillo +"Inserte"+ reset +"03 NOCIONES DE FRACCIONES")
            print(amarillo +"Inserte"+ reset +"04 OPERADORES CON FRACCIONES")
            print(amarillo +"Inserte"+ reset +"05 NUMEROS DECIMALES")
            print(amarillo +"Inserte"+ reset +"06 POTENCIACION Y RADICACION")
            print(amarillo +"Inserte"+ reset +"07 TRIGONOMETRIA BASICA")
            print(amarillo +"Inserte"+ reset +"08 MEDIDA DE TIEMPO")
            print(amarillo +"Inserte"+ reset +"09 RAZONES Y PROPORCIONES")
            print(amarillo +"Inserte"+ reset +"10 MAGNITUDES PROPORCIONALES Y REPARTO PROPORCIONAL")
            print(amarillo +"Inserte"+ reset +"12 REGLA DE TRES")
            print(amarillo +"Inserte"+ reset +"13 PORCENTAJE")
            print(amarillo +"Inserte"+ reset +"14 ANGULOS")
            print(amarillo +"Inserte"+ reset +"15 ANGULOS DE RECTAS PARALELAS CORTADA POR UNA SECANTE")
            print(amarillo +"Inserte"+ reset +"16 CIRCUNFERENCIA")
            print(amarillo +"Inserte"+ reset +"17 POLIGONOS:TRIANGULOS-CUADRITLATEROS")
            print(amarillo +"Inserte"+ reset +"18 MEDIDAS DE LONGITUD")
            print(amarillo +"Inserte"+ reset +"19 PERIMETRO")
            print(amarillo +"Inserte"+ reset +"20 MEDIDAS DE SUPERFICIE")
            print(amarillo +"Inserte"+ reset +"21 VOUMEN")
            corector_matematicas=input("INSERTE LA UNIDAD :: ")
            print("Inserto La Unidad >> ",corector_matematicas)
            if corector_matematicas== "1":
                while True:
                    print(morado +"Inserte"+ reset +" 01 Resultados")
                    print(morado +"Inserte"+ reset +" 02 Formulas")
                    print(morado +"Inserte"+ reset +" 03 Ejemplos")
                    print(morado +"Inserte"+ reset +" 04 Resolver")
                    print(morado +"Inserte"+ reset +" 05 Historia")
#INGLES#    
    if CORRECTOR_INICIAL == "3" or CORRECTOR_INICIAL == "ingles":
        while True:
            banner()
            print(azul +"Inserte"+ reset +" 0 Ayuda!")
            print(azul +"Inserte"+ reset +" 1 Traductor De español a Ingles!")
            print(azul +"Inserte"+ reset +" 2 Traductor De ingles a español!")
            print(azul +"Inserte"+ reset +" 3 Dicionario Completo!")
            print(azul +"Inserte"+ reset +" 4 Diccionario Rapido!")
            print(azul +"Inserte"+ reset +" 5 Mas conosimiento De el ingles!")
            print(azul +"Inserte"+ reset +" 6 Libro 'Inglish For Lite'!")
            print(azul +"Inserte"+ reset +" 7 Para Salir!")
            numero = input(verde+"INSERT: "+ reset)
            if numero == "banner":
                banner()
            if numero == "7":
                break
#numero 0 Ayuda
            if numero == "0" :
                print("1 >> Para tener acceso Ala base de datos")
                print("2 >> ###Creditos###")
                print("2 >> URL Usadas Para Plajiar en Aula")
                numero5=input(": ")
                while numero5 == "1" :
                    clave = input("Inserte Clave Secreta : ")
                    if clave == "cavesecretaxd":
                        print(">>>>>>>>>>>>>>NO HAY VACE DE DATOS BB :v<<<<<<<<<<<<<<<<<<")
                        break
                    if numero5 == "2":
                        print("lol")
                    if numero5 == "3":
                        print("DUOLINGO")
                        print("Estudo vajo :'v ")
#numero pagina 1 Traductor online xd
            if numero == "1":
                print(Fore.GREEN+"Para Salir de el traductor online ponga >bye<"+Back.RESET)
                def Traduccion(source, target, text):
                        parametros = {'sl': source, 'tl': target, 'q': text}
                        cabeceras = {"Charset":"UTF-8","User-Agent":"AndroidTranslate/5.3.0.RC02.130475354-53000263 5.1 phone TRANSLATE_OPM5_TEST_1"}
                        url = "https://translate.google.com/translate_a/single?client=at&dt=t&dt=ld&dt=qca&dt=rm&dt=bd&dj=1&hl=es-ES&ie=UTF-8&oe=UTF-8&inputm=2&otf=2&iid=1dd3b944-fa62-4b55-b330-74909a99969e"
                        response = requests.post(url, data=parametros, headers=cabeceras)
                        if response.status_code == 200:
                            for x in response.json()['sentences']:
                                return x['trans']
                        else:
                            return (azul +"No Hay coneccion Papu"+reset)
                while True:
                        text = input(verde +"Ingrese un texto para traducir: ")
                        if text == "bye":
                            break
                        else:
                            respuesta = Traduccion("es", "en", text)
                            print(azul +"Resultado: "+ reset + str(respuesta))
                            print("\n")
#numero pagina 2
            if numero == "2":
                banner()
                print("En prueva")
                input("Precione Cualquier tecla para continuar..")
## numero 3 para Diccionario completo
            if numero == "3":
                while True:
                    print ("Inserte::bye para salir")
                    letra = input("Inserte la letras que decea buscar..a,b,c etc..")
                    if letra == "bye":
                        banner()
                        break
                    elif letra == "a":
                        print(" 1. Act - actuar 2. Action - acción \n 3. Actor - actor \n 4. Accept - aceptar \n 5. Account - cuenta \n 6. According to - según \n 7. Acknowledge - confirmar, aceptar \n 8. Admit (to admit) - admitir \n 9. Adapt (to adapt) - adaptarse \n 10. Adopt (to adopt) - adoptar \n 11. Advertise (to advertise) - anunciar, publicitar \n 12. Adore (to adore) - adorar \n 13. Advice - consejo \n 14. After - después \n 15. Afford (to afford) - poder pagar, permitirse algo \n 16. Agree (to agree) - acordar, estar de acuerdo \n 17. Age - edad \n 18. Aim (to aim) - apuntar, aspirar \n 19. Aid (to aid) - auxiliar, ayudar \n 20. Air - aire \n 21. Always - siempre \n 22. Almost - casi \n 23. All - todo \n 24. Also - también \n 25. Already - ya \n 26. Alert​ (to alert) - alertar, alerta \n 27. Alarm (to alarm) - alarmar, alarma \n 28. Alter (to alter) - alterar \n 29. Align (to align) ​- alinear \n 30. Alligator - caimán \n 31. Alien - alienígena, extraterrestre \n 32. Also - también \n 33. Although - aunque \n 34. Alternative - alternativa \n 35. Ambition - ambición \n 36. Amber - ámbar \n 38. And - y \n 39. Another - otro \n 40. Animal - animal \n 41. Angel - ángel \n 42. Attack (to attack) - atacar \n 43. Apricot - albaricoque \n 44. Applause - aplauso \n 45. Appetite - apetito \n 46. Art - arte \n 47. Arrange (to arrange) - arreglar, programar, disponer \n 49. Awake - despierto \n 50. Aware - consciente de/ al tanto de")
                    elif letra == "b":
                        print ("En prueva dicionario en B")

#numero 4 pagina 
            if numero == "4":
                while True:
                    print("Inserte > bye < para salir" )
                    print("Palabras Faciles")
                    print("Asegurese de Poner el inicio y el final de la palabra")
                    print("Ejemplo:: action = an")
                    palabra = input("Inserte>>")
                    if palabra == "bye":
                        banner()
                        break
                    if palabra == "ro":
                        palabra1=input("Su palabra es Radio?: ")
                        if "s" == palabra1:
                            print("Radio en ingles es :: Radio")
                        else:
                            palabra2=print("Su palabra es rio: ")
                        if "s" == palabra2:
                            print("Rio en ingles es River")
                    else:
                        print("No se encontraron otros datos para su palabra >>> ", palabra)
#numero pagina 5 conosimiento
            if numero == "5":
                banner()
                print(azul+"1"+ reset + ">> Para saver las preposisiones: ")
                print(azul+"2"+ reset + ">> Para saver las Congugaciones: ")
                print(azul+"3"+ reset + ">> Para saver mas sobre como se escribe: ")
                print(azul+"4"+ reset + ">> Como se Usan el Negativo?' ")
                print(azul+"5"+ reset + ">> Como se usa el aprostico")
                input(amarillo+"Precione Cualquier tecla para continuar.."+reset)
#Libro 6
            if numero == "6":
                banner()
                print("En prueva")
                input("Precione Cualquier tecla para continuar..")
