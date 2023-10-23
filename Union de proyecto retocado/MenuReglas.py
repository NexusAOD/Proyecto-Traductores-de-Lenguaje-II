from R0 import R0
from R1 import R1
from R2 import R2
from R3 import R3
from R4 import R4
from R6 import R6
from R7 import R7


class MenuReglas:

    def select_option(self, NoPila, mi_pila):
        r0 = R0()
        r1 = R1()
        r2 = R2()
        r3 = R3()
        r4 = R4()
        r6 = R6()
        r7 = R7()
        if NoPila == 0:
            return "Has seleccionado la Opción 1."
        elif NoPila == -1:
            instancia = r0.manipular_pila(mi_pila)
            return instancia
        elif NoPila == -2:
            instancia = r1.manipular_pila(mi_pila)
            return instancia
        elif NoPila == -3:
            instancia = r2.manipular_pila(mi_pila)
            return instancia
        elif NoPila == -4:
            instancia = r3.manipular_pila(mi_pila)
            return instancia
        elif NoPila == -5:
            instancia = r4.manipular_pila(mi_pila)
            return instancia
        elif NoPila == -6:
            return "Has seleccionado la Opción 53."
        elif NoPila == -7:
            instancia = r6.manipular_pila(mi_pila)
            return instancia
        elif NoPila == -8:
            instancia = r7.manipular_pila(mi_pila)
            return instancia
        elif NoPila == -9:
            return "Has seleccionado la Opción 53."
        elif NoPila == -10:
            return "Has seleccionado la Opción 53."
        elif NoPila == -11:
            return "Has seleccionado la Opción 53."
        elif NoPila == -12:
            return "Has seleccionado la Opción 2."
        elif NoPila == -13:
            return "Has seleccionado la Opción 3."
        elif NoPila == -14:
            return "Has seleccionado la Opción 53."
        elif NoPila == -15:
            return "Has seleccionado la Opción 53."
        elif NoPila == -16:
            return "Has seleccionado la Opción 2."
        elif NoPila == -17:
            return "Has seleccionado la Opción 3."
        elif NoPila == -18:
            return "Has seleccionado la Opción 53."
        elif NoPila == -19:
            return "Has seleccionado la Opción 53."
        elif NoPila == -20:
            return "Has seleccionado la Opción 53."
        elif NoPila == -21:
            return "Has seleccionado la Opción 53."
        elif NoPila == -22:
            return "Has seleccionado la Opción 2."
        elif NoPila == -23:
            return "Has seleccionado la Opción 3."
        elif NoPila == -24:
            return "Has seleccionado la Opción 53."
        elif NoPila == -25:
            return "Has seleccionado la Opción 53."
        elif NoPila == -26:
            return "Has seleccionado la Opción 53."
        elif NoPila == -27:
            return "Has seleccionado la Opción 2."
        elif NoPila == -28:
            return "Has seleccionado la Opción 3."
        elif NoPila == -29:
            return "Has seleccionado la Opción 53."
        elif NoPila == -30:
            return "Has seleccionado la Opción 53."
        elif NoPila == -31:
            return "Has seleccionado la Opción 2."
        elif NoPila == -32:
            return "Has seleccionado la Opción 3."
        elif NoPila == -33:
            return "Has seleccionado la Opción 53."
        elif NoPila == -34:
            return "Has seleccionado la Opción 53."
        elif NoPila == -35:
            return "Has seleccionado la Opción 53."
        elif NoPila == -36:
            return "Has seleccionado la Opción 53."
        elif NoPila == -37:
            return "Has seleccionado la Opción 2."
        elif NoPila == -38:
            return "Has seleccionado la Opción 3."
        elif NoPila == -39:
            return "Has seleccionado la Opción 53."
        elif NoPila == -40:
            return "Has seleccionado la Opción 53."
        elif NoPila == -41:
            return "Has seleccionado la Opción 53."
        elif NoPila == -42:
            return "Has seleccionado la Opción 2."
        elif NoPila == -43:
            return "Has seleccionado la Opción 3."
        elif NoPila == -44:
            return "Has seleccionado la Opción 53."
        elif NoPila == -45:
            return "Has seleccionado la Opción 53."
        elif NoPila == -46:
            return "Has seleccionado la Opción 2."
        elif NoPila == -47:
            return "Has seleccionado la Opción 3."
        elif NoPila == -48:
            return "Has seleccionado la Opción 53."
        elif NoPila == -49:
            return "Has seleccionado la Opción 53."
        elif NoPila == -50:
            return "Has seleccionado la Opción 53."
        elif NoPila == -51:
            return "Has seleccionado la Opción 53."
        elif NoPila == -52:
            return "Has seleccionado la Opción 2."
        elif NoPila == -53:
            return "Has seleccionado la Opción 3."
        elif NoPila == -54:
            return "Has seleccionado la Opción 3."
        else:
            return "Opción no válida."