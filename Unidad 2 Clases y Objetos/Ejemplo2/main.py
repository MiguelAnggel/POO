from motor import Motor  # para poder importar otros archivos y clases
from llanta import Llanta 
from cochem import Coche as CocheMetodos # para poder diferenciar clases y que no colisionen
from cochea import Coche as CocheAtributos #hp

def main():
    #mandar a llamar 
    ejemploCocheMetodos()
    ejemploCocheAtributos()

def ejemploCocheMetodos():
    print("composicion por metodos")

    #composicion por metodos permite mas personalizacion
    motor= Motor("67894")
    coche = Coche()
    coche.encender(motor)

    fi = Llanta("FRONTAL IZQUIERDA")
    fi.inflar(28)
    fd = Llanta("FORNTAL DERECHA")
    fi.inflar(28)


    coche.agregarLlanta(fi)
    coche.agregarLlanta(fd)

    print(coche.Llantas [0]) # para poder imprimir la informacion

def ejemploCocheAtributos():
    print("Composicion por atributos")
    #composicion por atributos es mas sencillo de entender y leer
    
    coche = CocheAtributos("ABCDE")
    coche.encender()
    coche.inflarRuedas()

print(Coche.ruedas[2])



if __name__ == "__main__":
    main()