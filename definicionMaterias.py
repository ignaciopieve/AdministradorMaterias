import pickle
import datetime


class ListaMaterias:
    def __init__(self, lista):
        self.lista = lista

    def traer_materia(self, id):
        for a in self.lista[0]:
            if a.id == id:
                return a

    def traer_regularidad(self, id):
        for a in self.lista[1]:
            if a.id_materia == id:
                return a
        return None

    def traer_aprobacion(self, id):
        for a in self.lista[2]:
            if a.id_materia == id:
                return a
        return None

    def obtener_nota(self, id):
        for a in self.lista[2]:
            if a.id_materia == id:
                return a.nota
        return '-'


class Materia:
    # id   Nombre   Abreviacion   Horas   Correlativas   Duracion
    def __init__(self, id, nombre, abreviacion, horas, correlativas, duracion, nivel):
        self.id = id
        self.nombre = nombre
        self.abreviacion = abreviacion
        self.horas = horas
        self.correlativas = correlativas
        self.duracion = duracion
        self.nivel = nivel

    def get_estado(self, lista_mayor):
        for a in lista_mayor.lista[2]:
            if a.id_materia == self.id:
                return 'Aprobada'
        for a in lista_mayor.lista[1]:
            if a.id_materia == self.id:
                if a.year_inicio == datetime.datetime.now().year:
                    if self.duracion == 'Anual':
                        return 'Cursando'
                    else:
                        if datetime.datetime.now().month < 7:
                            return 'Cursando'
                        elif a.cuatrimestre_inicio == 2:
                            return 'Cursando'
                        else:
                            return 'Regular'
                else:
                    return 'Regular'
        for a in self.correlativas[0][0]:
            if (lista_mayor.traer_materia(a).get_estado(lista_mayor) != 'Regular') and (lista_mayor.traer_materia(a).get_estado(lista_mayor) != 'Aprobada'):
                return 'No cursable'
        for a in self.correlativas[0][1]:
            if lista_mayor.traer_materia(a).get_estado(lista_mayor) != 'Aprobada':
                return 'No cursable'
        return 'Cursable'

    def es_rendible(self, lista_mayor):
        if self.get_estado(lista_mayor) != 'Regular':
            return ''
        for a in self.correlativas[0][0]:
            if lista_mayor.traer_materia(a).get_estado(lista_mayor) != 'Aprobada':
                return ' (No se puede rendir)'
        return ' (Rendible)'


class Aprobacion:
    def __init__(self, id_materia, fecha, nota):
        self.id_materia = id_materia
        self.fecha = fecha
        self.nota = nota


class Regularidad:
    def __init__(self, id_materia, year_inicio, cuatrimestre_inicio, curso):
        self.id_materia = id_materia
        self.year_inicio = year_inicio
        self.cuatrimestre_inicio = cuatrimestre_inicio
        self.curso = curso


def crear_archivo_base():
    pf = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35]
    lista_base = [[
                  # PRIMER AÑO
                  Materia(1, 'Analisis Matemático I',                   'AMI',      5, [[[], []], []],  'Anual', 1),
                  Materia(2, 'Algebra y Geometría Analítica',           'AGA',      5, [[[], []], []],  'Anual', 1),
                  Materia(3, 'Matemática Discreta',                     'MAD',      6, [[[], []], []],  'Cuatrimestral', 1),
                  Materia(4, 'Sistemas y Organizaciones',               'SOR',      6, [[[], []], []],  'Cuatrimestral', 1),
                  Materia(5, 'Algoritmos y Estructuras de Datos',       'AED',      5, [[[], []], []],  'Anual', 1),
                  Materia(6, 'Arquitectura de Computadoras',            'ACO',      8, [[[], []], []],  'Cuatrimestral', 1),
                  Materia(7, 'Física I',                                'FIS',      5, [[[], []], []],  'Anual', 1),
                  Materia(8, 'Inglés',                                  'ING',      2, [[[], []], []],  'Anual', 1),
                  Materia(22, 'Ingeniería y Sociedad',                  'ISI',      4, [[[], []], []],  'Cuatrimestral', 1),
                  # SEGUNDO AÑO
                  Materia(9, 'Química',                                 'QUI',      6, [[[],        []], []],               'Cuatrimestral', 2),
                  Materia(10, 'Analisis Matemático II',                 'AMII',     5, [[[1, 2],    []], [1, 2]],           'Anual', 2),
                  Materia(11, 'Física II',                              'FISII',    5, [[[1, 7],    []], [1, 7]],           'Anual', 2),
                  Materia(12, 'Análisis de Sistemas',                   'ASI',      6, [[[4, 5],    []], [4, 5]],           'Anual', 2),
                  Materia(13, 'Sintaxis y Semántica de los Lenguajes',  'SSL',      8, [[[3, 5],    []], [3, 5]],           'Cuatrimestral', 2),
                  Materia(14, 'Paradigmas de Programación',             'PPR',      8, [[[3, 5],    []], [3, 5]],           'Cuatrimestral', 2),
                  Materia(15, 'Sistemas Operativos',                    'SOP',      4, [[[3, 5, 6], []], [3, 5, 6]],        'Anual', 2),
                  Materia(17, 'Probabilidad y Estadística',             'PYE',      6, [[[1, 2],    []], [1, 2]],           'Cuatrimestral', 2),
                  # TERCER AÑO
                  Materia(16, 'Sistemas de Representación',             'SSR',      3, [[[],            []],        []],            'Anual', 3),
                  Materia(18, 'Diseño de Sistemas',                     'DSI',      6, [[[12, 14],      [3, 4, 5]], [12, 14]],      'Anual', 3),
                  Materia(19, 'Comunicaciones',                         'COM',      4, [[[6, 10, 11],   [1, 2, 7]], [6, 10, 11]],   'Anual', 3),
                  Materia(20, 'Matemática Superior',                    'MAS',      8, [[[10],          [1, 2]],    [10]],          'Cuatrimestral', 3),
                  Materia(21, 'Gestión de Datos',                       'GDA',      8, [[[12, 13, 14],  [3, 4, 5]], [12]],          'Cuatrimestral', 3),
                  Materia(23, 'Economía',                               'ECO',      6, [[[12],          [4, 5]],    [12]],          'Cuatrimestral', 3),
                  Materia(24, 'Inglés II',                              'INGII',    2, [[[],            [8]],       []],            'Anual', 3),
                  # CUARTO AÑO
                  Materia(25, 'Redes de Información',                   'RIN',      4, [[[15, 19],      [3, 5, 6, 10, 11]], [15, 19]],      'Anual', 4),
                  Materia(26, 'Administración de Recursos',             'ARE',      6, [[[15, 18, 23],  [6, 8, 12, 14]],    [15, 18, 23]],  'Anual', 4),
                  Materia(27, 'Investigación Operativa',                'IOP',      5, [[[17, 20],      [10]],              [17, 20]],      'Anual', 4),
                  Materia(28, 'Simulación',                             'SIM',      8, [[[17, 20],      [10]],              [17, 20]],      'Cuatrimestral', 4),
                  Materia(29, 'Ingeniería de Software',                 'ISW',      6, [[[17, 18, 21],  [12, 13, 14]],      [17, 18, 21]],  'Cuatrimestral', 4),
                  Materia(30, 'Teoría de Control',                      'TCO',      6, [[[9, 20],       [10, 11]],          [9, 20]],       'Cuatrimestral', 4),
                  Materia(31, 'Legislación',                            'LEG',      4, [[[12, 22],      [4, 5]],            [12, 22]],      'Cuatrimestral', 4),
                  # QUINTO AÑO
                  Materia(32, 'Proyecto Final',                         'PF',       6, [[[25, 26, 29, 31],  [15, 16, 17, 18, 19, 21, 22, 23, 24]],  pf],            'Anual', 5),
                  Materia(33, 'Inteligencia Artificial',                'IA',       3, [[[27, 28],          [17, 18, 20]],                          [27, 28]],      'Anual', 5),
                  Materia(34, 'Administración General',                 'AGE',      6, [[[26, 27],          [15, 17, 18, 20, 23]],                  [26, 27]],      'Cuatrimestral', 5),
                  Materia(35, 'Sistemas de Gestión',                    'SGO',      4, [[[26, 27, 28],      [15, 17, 18, 20, 23]],                  [26, 27, 28]],  'Anual', 5),
                  # ELECTIVAS
                  Materia(101, 'Programación de Aplicaciones Visuales I', 'PAVI',   8, [[[14, 5],   []],    [14, 5]],   'Electiva', 0),
                  Materia(102, 'Programación de Aplicaciones Visuales II', 'PAVII', 8, [[[101],     [14]],  []],        'Electiva', 0),
                  Materia(103, 'Tecnología de Software de Base',        'TSB',      8, [[[14],      [5]],   [14]],      'Electiva', 0),
                  Materia(104, 'Diseño de Lenguaje de Consulta',        'DLC',      8, [[[103],     []],    [103]],     'Electiva', 0),
                  Materia(105, 'Gestión de la Mejora de los Procesos',  'GMP',      6, [[[4, 12],   []],    [12]],      'Electiva', 0),
                  Materia(106, 'Tecnología Educativa',                  'TED',      6, [[[12],      [4]],   []],        'Electiva', 0),
                  Materia(107, 'Gestión Industrial de la Producción',   'GIP',      6, [[[12],      [4]],   []],        'Electiva', 0),

                  ], [], []]        # Lista base = [materias, cursados, aprobaciones]
    lista_base_objeto = ListaMaterias(lista_base)
    archivo = open('data.db', 'wb')
    pickle.dump(lista_base_objeto, archivo)
    archivo.close()


def leef_base():
    archivo = open('data.db', 'rb')
    return pickle.load(archivo)
