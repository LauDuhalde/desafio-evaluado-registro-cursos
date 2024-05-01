from registro_cursos.services import *

curso=crear_curso("C001", "Curso de Python", 1)
curso2=crear_curso("C002", "Curso de JavaScript", 2)
curso_existente=crear_curso("C001", "Curso de Python", 1)

profesor=crear_profesor("123456789", "Juan", "Pérez", True)
profesor2=crear_profesor("987654321", "María", "Gómez", False, "Administrador")
profesor_existente=crear_profesor("987654321", "María", "Gómez", False, "Administrador")

estudiante=crear_estudiante("123456789", "Juan", "Pérez", "2000-01-01", True)
estudiante2=crear_estudiante("987654321", "María", "Gómez", "1999-12-31", False, "Administrador")
estudiante_existente=crear_estudiante("987654321", "María", "Gómez", "1999-12-31", False, "Administrador")

direccion=crear_direccion(estudiante, "Calle Principal", "123", "A", "Santiago", "Santiago", "RM")
direccion_exisxtente=crear_direccion(estudiante, "Calle Principal", "123", "A", "Santiago", "Santiago", "RM")

estudiante=obtiene_estudiante('123456789')
estudiante_inexistente=obtiene_estudiante('123456799')

profesor=obtiene_profesor('123456789')
profesor_inexistente=obtiene_profesor('123456799')

curso=obtiene_curso('C001')
curso_inexistente=obtiene_curso('C002')

agrega_profesor_a_curso(profesor,curso)

agrega_cursos_a_estudiante(estudiante,curso)
agrega_cursos_a_estudiante(estudiante2,curso)

imprime_estudiante_cursos()

eliminar_estudiante('123456789')