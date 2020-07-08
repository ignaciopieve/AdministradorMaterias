from definicionMaterias import *
from tabulate import tabulate
import os


def menu():
    if not os.path.exists('data.db'):
        opc = input('No existe un archivo de datos... Desea crear uno nuevo vacio? (S/N): ')
        if opc == 's' or opc == 'S':
            crear_archivo_base()
        else:
            return None

    base_datos = leef_base()

    while True:
        opc = int(input(('1- Listar materias\n'
                         '2- Cargar cursado (regularidad)\n'
                         '3- Cargar aprobacion\n'
                         '4- Eliminar cursado\n'
                         '5- Eliminar regularidad\n'
                         '6- Datos de una materia especifica\n'
                         '7- Agregar o eliminar materias\n'
                         '8- Herramientas de desarrollo\n'
                         '9- Guardar cambios\n'
                         'Ingrese su opcion: ')))
        if opc == 1:
            os.system('cls')
            lista = [[], [], [], [], [], []]
            materias_cursando = 0
            materias_aprobadas = 0
            electivas_aprobadas = 0
            horas_electivas = 0
            for a in base_datos.lista[0]:
                estado = a.get_estado(base_datos)
                es_rendible = a.es_rendible(base_datos)
                lista[a.nivel].append([a.id, a.nivel, a.nombre,a.abreviacion,  estado + es_rendible, base_datos.obtener_nota(a.id)])
                if estado == 'Cursando':
                    materias_cursando += 1
                elif estado == 'Aprobada' and a.nivel != 0:
                    materias_aprobadas += 1
                if a.nivel == 0 and estado == 'Aprobada':
                    electivas_aprobadas += 1
                    horas_electivas += a.horas
            materias_restantes = 35 - materias_aprobadas
            horas_electivas_restantes = 46 - horas_electivas

            rendidas_totales = 0
            suma_total = 0
            promedios = []
            for a in range(6):
                c = 0
                t = 0
                for b in lista[a]:
                    if b[-1] != '-':
                        t += b[-1]
                        c += 1
                if c > 0:
                    promedios.append(str(round(t / c, 2)))
                else:
                    promedios.append('-')
                rendidas_totales += c
                suma_total += t
            promedio_general = round(suma_total / rendidas_totales, 2)
            msg = 'Fecha actualizacion: ' + str(datetime.datetime.now().date()) + '\n\n'
            print('Promedio General: ' + str(promedio_general))
            msg += 'Promedio General: ' + str(promedio_general) + '\n'
            print('Cantidad de materias cursando: ' + str(materias_cursando))
            msg += 'Cantidad de materias cursando: ' + str(materias_cursando) + '\n'
            print('Cantidad de materias aprobadas: ' + str(materias_aprobadas) + '    Materias restantes: ' + str(materias_restantes))
            msg += 'Cantidad de materias aprobadas: ' + str(materias_aprobadas) + '    Materias restantes: ' + str(materias_restantes) + '\n'
            print('Cantidad de electivas aprobadas: ' + str(electivas_aprobadas))
            msg += 'Cantidad de electivas aprobadas: ' + str(electivas_aprobadas) + '\n'
            print('Cantidad total de aprobadas (Con electivas): ' + str(electivas_aprobadas + materias_aprobadas))
            msg += 'Cantidad total de aprobadas (Con electivas): ' + str(electivas_aprobadas + materias_aprobadas) + '\n'
            print('Horas totales de electivas: ' + str(horas_electivas) + '    Horas restantes: ' + str(horas_electivas_restantes))
            msg += 'Horas totales de electivas: ' + str(horas_electivas) + '    Horas restantes: ' + str(horas_electivas_restantes) + '\n\n'
            print('')


            print(
                tabulate(lista[1], headers=['ID ', 'Año', 'Nombre' + ' ' * 44, 'Abreviacion', 'Estado' + ' ' * 24, 'NF'], tablefmt='grid'))
            print(' ' * 114 + 'Promedio: ' + promedios[1])
            print(
                tabulate(lista[2], headers=['ID ', 'Año', 'Nombre' + ' ' * 44, 'Abreviacion', 'Estado' + ' ' * 24, 'NF'], tablefmt='grid'))
            print(' ' * 114 + 'Promedio: ' + promedios[2])
            print(
                tabulate(lista[3], headers=['ID ', 'Año', 'Nombre' + ' ' * 44, 'Abreviacion', 'Estado' + ' ' * 24, 'NF'], tablefmt='grid'))
            print(' ' * 114 + 'Promedio: ' + promedios[3])
            print(
                tabulate(lista[4], headers=['ID ', 'Año', 'Nombre' + ' ' * 44, 'Abreviacion', 'Estado' + ' ' * 24, 'NF'], tablefmt='grid'))
            print(' ' * 114 + 'Promedio: ' + promedios[4])
            print(
                tabulate(lista[5], headers=['ID ', 'Año', 'Nombre' + ' ' * 44, 'Abreviacion', 'Estado' + ' ' * 24, 'NF'], tablefmt='grid'))
            print(' ' * 114 + 'Promedio: ' + promedios[5])
            print(
                tabulate(lista[0], headers=['ID ', 'Año', 'Nombre' + ' ' * 44, 'Abreviacion', 'Estado' + ' ' * 24, 'NF'], tablefmt='grid'))
            print(' ' * 114 + 'Promedio: ' + promedios[0])
            input('Pulse enter para volver al menu anterior...')

            msg += tabulate(lista[1],
                            headers=['ID ', 'Año', 'Nombre' + ' ' * 44, 'Abreviacion', 'Estado' + ' ' * 24, 'NF'],
                            tablefmt='grid') + '\n' + ' ' * 114 + 'Promedio: ' + promedios[1] + '\n'
            msg += tabulate(lista[2],
                            headers=['ID ', 'Año', 'Nombre' + ' ' * 44, 'Abreviacion', 'Estado' + ' ' * 24, 'NF'],
                            tablefmt='grid') + '\n' + ' ' * 114 + 'Promedio: ' + promedios[2] + '\n'
            msg += tabulate(lista[3],
                            headers=['ID ', 'Año', 'Nombre' + ' ' * 44, 'Abreviacion', 'Estado' + ' ' * 24, 'NF'],
                            tablefmt='grid') + '\n' + ' ' * 114 + 'Promedio: ' + promedios[3] + '\n'
            msg += tabulate(lista[4],
                            headers=['ID ', 'Año', 'Nombre' + ' ' * 44, 'Abreviacion', 'Estado' + ' ' * 24, 'NF'],
                            tablefmt='grid') + '\n' + ' ' * 114 + 'Promedio: ' + promedios[4] + '\n'
            msg += tabulate(lista[5],
                            headers=['ID ', 'Año', 'Nombre' + ' ' * 44, 'Abreviacion', 'Estado' + ' ' * 24, 'NF'],
                            tablefmt='grid') + '\n' + ' ' * 114 + 'Promedio: ' + promedios[5] + '\n'
            msg += tabulate(lista[0],
                            headers=['ID ', 'Año', 'Nombre' + ' ' * 44, 'Abreviacion', 'Estado' + ' ' * 24, 'NF'],
                            tablefmt='grid') + '\n' + ' ' * 114 + 'Promedio: ' + promedios[0] + '\n'
            archivo = open('Informe.txt', 'w')
            archivo.write(msg)
            archivo.close()

        elif opc == 2:
            id_materia = int(input('Ingrese la id de la materia: '))
            materia = base_datos.traer_materia(id_materia)
            estado = materia.get_estado(base_datos)
            if  estado == 'Aprobada' or estado == 'Regular' or estado == 'Cursado':
                print('Ya se ha cargado la regularidad de la materia, pulse una tecla para continuar')
            else:
                print('Materia: ' + materia.nombre + ' (' + materia.abreviacion + ')')
                start_year = int(input('Ingrese el año de cursado: '))
                start_cuatrimestre = int(input('Ingrese el cuatrimestre de cursado: '))
                curso = input('Ingrese el curso de cursado: ')
                base_datos.lista[1].append(Regularidad(id_materia, start_year, start_cuatrimestre, curso))
                input('Pulse enter para volver al menu anterior...')

        elif opc == 3:
            id_materia = int(input('Ingrese la id de la materia: '))
            materia = base_datos.traer_materia(id_materia)
            if materia.es_rendible(base_datos) == ' (Rendible)' or materia.get_estado(base_datos) == 'Cursando':
                print('Materia: ' + materia.nombre + ' (' + materia.abreviacion + ')')
                fecha = input('Ingrese la fecha de aprobacion: ')
                nota = int(input('Ingrese la nota final: '))
                base_datos.lista[2].append(Aprobacion(id_materia, fecha, nota))
            else:
                print('Aun no se ha cargado la regularidad de "' + materia.nombre +
                      '", no cumple con las correlativas necesarias o ya esta aprobada')
            input('Pulse enter para volver al menu anterior...')

        elif opc == 4:
            id_eliminar = int(input('Ingrese el id de la materia a eliminar su cursado: '))
            for a in range(len(base_datos.lista[1])):
                if base_datos.lista[1][a].id_materia == id_eliminar:
                    base_datos.lista[1].pop(a)
                    break

        elif opc == 5:
            id_eliminar = int(input('Ingrese el id de la materia a eliminar su aprobacion: '))
            for a in range(len(base_datos.lista[2])):
                if base_datos.lista[2][a].id_materia == id_eliminar:
                    base_datos.lista[2].pop(a)
                    break

        elif opc == 6:
            id_visualizar = int(input('Ingrese el id de la materia que desea visualizar: '))
            materia = base_datos.traer_materia(id_visualizar)
            regularidad = base_datos.traer_regularidad(id_visualizar)
            aprobacion = base_datos.traer_aprobacion(id_visualizar)
            os.system('cls')
            lista = [[materia.id, materia.nivel, materia.nombre + ' (' + materia.abreviacion + ')', materia.get_estado(base_datos), materia.duracion, materia.horas, materia.correlativas[0][0], materia.correlativas[0][1], materia.correlativas[1]]]
            print(
                tabulate(lista, headers=['ID ', 'Año', 'Nombre', 'Estado', 'Duracion', 'Horas cátedra semanales',
                                         'Regulares para cursar', 'Aprobadas para cursar', 'Aprobadas para rendir'], tablefmt='grid'))
            if not regularidad is None:
                lista = [[regularidad.year_inicio, regularidad.cuatrimestre_inicio, regularidad.curso]]
                print(
                    tabulate(lista, headers=['Año de cursado', 'Cuatrimestre', 'Curso'], tablefmt='grid'))
            if not aprobacion is None:
                lista = [[aprobacion.fecha, aprobacion.nota]]
                print(
                    tabulate(lista, headers=['Fecha de aprobacion', 'Nota final'], tablefmt='grid'))
            input('Pulse enter para volver al menu anterior...')

        elif opc == 7:
            os.system('cls')
            opc2 = int(input('1- Agregar una materia\n2- Eliminar una materia\n\nSeleccione una opcion: '))
            if opc2 == 1:
                os.system('cls')
                mid = int(input('Ingrese la id: '))
                mnombre = input('Ingrese el nombre: ')
                mabreviacion = input('Ingrese la abreviacion: ')
                mhoras = input('Ingrese la cantidad de horas semanales: ')
                mcorrelativascursar1 = eval('[' + input(
                    'Ingrese las materias regulares necesarias para cursar (separadas por coma): ') + ']')
                mcorrelativascursar2 = eval('[' + input(
                    'Ingrese las materias aprobadas necesarias para cursar (separadas por coma): ') + ']')
                mcorrelativascursar3 = eval('[' + input(
                    'Ingrese las materias aprobadas necesarias para rendir (separadas por coma): ') + ']')
                mcorrelativas = [[mcorrelativascursar1, mcorrelativascursar2], mcorrelativascursar3]
                mduracion = input('Ingrese si la materia es "Anual" o "Cuatrimestral": ')
                mnivel = int(input('Ingrese el nivel (año) de la materia (0 para electivas): '))
                nueva_instancia = Materia(mid, mnombre, mabreviacion, mhoras, mcorrelativas, mduracion, mnivel)
                base_datos.lista[0].append(nueva_instancia)
            elif opc2 == 2:
                os.system('cls')
                mid = int(input('Que materia desea eliminar (ingrese la id)?: '))

                for a in range(len(base_datos.lista[0])):
                    if base_datos.lista[0][a].id == mid:
                        base_datos.lista[0].pop(a)
                        break
                for a in range(len(base_datos.lista[1])):
                    if base_datos.lista[1][a].id_materia == mid:
                        base_datos.lista[1].pop(a)
                        break
                for a in range(len(base_datos.lista[2])):
                    if base_datos.lista[2][a].id_materia == mid:
                        base_datos.lista[2].pop(a)
                        break


        elif opc == 8:
            menu_desarrollo(base_datos)
            input('Pulse enter para volver al menu principal...')

        elif opc == 9:
            archivo = open('data.db', 'wb')
            pickle.dump(base_datos, archivo)
            archivo.close()
            input('Datos guardados con exito, pulse enter para volver al menu anterior...')

        else:
            print('No se encuentra la opcion seleccionada...')
        os.system('cls')


def menu_desarrollo(base):
    os.system('cls')
    opc = int(input('1- Ver todas las materias\n'
                     '2- Ver todas las regularidades\n'
                     '3- Ver todas las aprobaciones\n'
                     '4- Listado extendido de materias\n'))
    if opc == 1:
        os.system('cls')
        lista = []
        for a in base.lista[0]:
            lista.append([a.id, a.nombre, a.abreviacion, a.horas, a.correlativas, a.duracion, a.nivel])
        print(tabulate(lista, headers=['ID', 'Nombre', 'Abreviacion', 'Horas semanales', 'Correlativas',
                                       'Duracion', 'Nivel'], tablefmt='grid'))

    if opc == 2:
        os.system('cls')
        lista = []
        for a in base.lista[1]:
            lista.append([a.id_materia, a.year_inicio, a.cuatrimestre_inicio, a.curso])
        print(tabulate(lista, headers=['ID materia', 'Año', 'Cuatrimestre', 'Curso'], tablefmt='grid'))

    if opc == 3:
        os.system('cls')
        lista = []
        for a in base.lista[2]:
            lista.append([a.id_materia, a.fecha, a.nota])
        print(tabulate(lista, headers=['ID materia', 'Fecha', 'Nota final'], tablefmt='grid'))

    if opc == 4:
        os.system('cls')
        lista = [[], [], [], [], [], []]
        materias_cursando = 0
        materias_aprobadas = 0
        electivas_aprobadas = 0
        horas_electivas = 0
        for a in base.lista[0]:
            estado = a.get_estado(base)
            es_rendible = a.es_rendible(base)
            tiene_regularidad = 'No'
            tiene_aprobacion = 'No'
            if not base.traer_regularidad(a.id) is None:
                tiene_regularidad = 'Si'
            if not base.traer_aprobacion(a.id) is None:
                tiene_aprobacion = 'Si'
            lista[a.nivel].append(
                [a.id, a.nivel, a.nombre, a.abreviacion, estado + es_rendible, base.obtener_nota(a.id), tiene_regularidad, tiene_aprobacion])
            if estado == 'Cursando':
                materias_cursando += 1
            elif estado == 'Aprobada' and a.nivel != 0:
                materias_aprobadas += 1
            if a.nivel == 0 and estado == 'Aprobada':
                electivas_aprobadas += 1
                horas_electivas += a.horas
        materias_restantes = 35 - materias_aprobadas
        horas_electivas_restantes = 46 - horas_electivas

        rendidas_totales = 0
        suma_total = 0
        promedios = []
        for a in range(6):
            c = 0
            t = 0
            for b in lista[a]:
                if b[5] != '-':
                    t += b[5]
                    c += 1
            if c > 0:
                promedios.append(str(round(t / c, 2)))
            else:
                promedios.append('-')
            rendidas_totales += c
            suma_total += t
        promedio_general = round(suma_total / rendidas_totales, 2)

        print('Promedio General: ' + str(promedio_general))
        print('Cantidad de materias cursando: ' + str(materias_cursando))
        print('Cantidad de materias aprobadas: ' + str(materias_aprobadas) + '    Materias restantes: ' + str(
            materias_restantes))
        print('Cantidad de electivas aprobadas: ' + str(electivas_aprobadas))
        print('Cantidad total de aprobadas (Con electivas): ' + str(electivas_aprobadas + materias_aprobadas))
        print('Horas totales de electivas: ' + str(horas_electivas) + '    Horas restantes: ' + str(
            horas_electivas_restantes))
        print('')

        print(
            tabulate(lista[1], headers=['ID ', 'Año', 'Nombre' + ' ' * 44, 'Abreviacion', 'Estado' + ' ' * 24, 'NF', 'Regular', 'Aprobada'],
                     tablefmt='grid'))
        print(' ' * 114 + 'Promedio: ' + promedios[1])
        print(
            tabulate(lista[2], headers=['ID ', 'Año', 'Nombre' + ' ' * 44, 'Abreviacion', 'Estado' + ' ' * 24, 'NF', 'Regular', 'Aprobada'],
                     tablefmt='grid'))
        print(' ' * 114 + 'Promedio: ' + promedios[2])
        print(
            tabulate(lista[3], headers=['ID ', 'Año', 'Nombre' + ' ' * 44, 'Abreviacion', 'Estado' + ' ' * 24, 'NF', 'Regular', 'Aprobada'],
                     tablefmt='grid'))
        print(' ' * 114 + 'Promedio: ' + promedios[3])
        print(
            tabulate(lista[4], headers=['ID ', 'Año', 'Nombre' + ' ' * 44, 'Abreviacion', 'Estado' + ' ' * 24, 'NF', 'Regular', 'Aprobada'],
                     tablefmt='grid'))
        print(' ' * 114 + 'Promedio: ' + promedios[4])
        print(
            tabulate(lista[5], headers=['ID ', 'Año', 'Nombre' + ' ' * 44, 'Abreviacion', 'Estado' + ' ' * 24, 'NF', 'Regular', 'Aprobada'],
                     tablefmt='grid'))
        print(' ' * 114 + 'Promedio: ' + promedios[5])
        print(
            tabulate(lista[0], headers=['ID ', 'Año', 'Nombre' + ' ' * 44, 'Abreviacion', 'Estado' + ' ' * 24, 'NF', 'Regular', 'Aprobada'],
                     tablefmt='grid'))
        print(' ' * 114 + 'Promedio: ' + promedios[0])


if __name__ == '__main__':
    menu()