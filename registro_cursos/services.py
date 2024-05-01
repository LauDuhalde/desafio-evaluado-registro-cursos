from .models import Curso, Profesor, Estudiante, Direccion

def crear_curso(codigo, nombre, version):
    try:
        # Verificar si ya existe un curso con el mismo código
        if Curso.objects.filter(codigo=codigo).exists():
            print("Ya existe un curso con este código.")
            return None
        
        # Crear un nuevo curso
        curso = Curso(codigo=codigo, nombre=nombre, version=version)
        curso.save()
        
        print("Curso creado exitosamente.")
        return curso
    except Exception as e:
        print(f"Error al crear el curso: {e}")
        return None

def crear_profesor(rut, nombre, apellido, activo=False, creado_por=None):
    try:
        # Verificar si ya existe un profesor con el mismo Rut
        if Profesor.objects.filter(rut=rut).exists():
            print("Ya existe un profesor con este Rut.")
            return None
        
        # Crear un nuevo profesor
        profesor = Profesor(rut=rut, nombre=nombre, apellido=apellido, activo=activo, creado_por=creado_por) 
        profesor.save()
        
        print("Profesor creado exitosamente.")
        return profesor
    except Exception as e:
        print(f"Error al crear el profesor: {e}")
        return None
    
from .models import Estudiante

def crear_estudiante(rut, nombre, apellido, fecha_nac, activo=False, creado_por=None):
    try:
        # Verificar si ya existe un estudiante con el mismo Rut
        if Estudiante.objects.filter(rut=rut).exists():
            print("Ya existe un estudiante con este Rut.")
            return None
        
        # Crear un nuevo estudiante
        estudiante = Estudiante(rut=rut, nombre=nombre, apellido=apellido, fecha_nac=fecha_nac, activo=activo, creado_por=creado_por)
        estudiante.save()
        
        print("Estudiante creado exitosamente.")
        return estudiante
    except Exception as e:
        print(f"Error al crear el estudiante: {e}")
        return None

def crear_direccion(estudiante, calle, numero, dpto, comuna, ciudad, region):
    try:
        # Verificar si el estudiante ya tiene una dirección asociada
        if hasattr(estudiante, 'direccion'):
            print("El estudiante ya tiene una dirección asociada.")
            return estudiante.direccion
        
        # Crear una nueva dirección para el estudiante
        direccion = Direccion(
            estudiante=estudiante,
            calle=calle,
            numero=numero,
            dpto=dpto,
            comuna=comuna,
            ciudad=ciudad,
            region=region
        )
        direccion.save()
        
        print("Dirección creada exitosamente.")
        return direccion
    except Exception as e:
        print(f"Error al crear la dirección: {e}")
        return None


def obtiene_estudiante(rut):
    try:
        estudiante = Estudiante.objects.get(rut=rut)
        print(f"Estudiante encontrado: {estudiante.nombre} {estudiante.apellido}")
        return estudiante
    except Estudiante.DoesNotExist:
        print("No se encontró ningún estudiante con ese Rut.")
        return None
    except Exception as e:
        print(f"Error al obtener el estudiante: {e}")
        return None

def obtiene_profesor(rut):
    try:
        profesor = Profesor.objects.get(rut=rut)
        print(f"Profesor encontrado: {profesor.nombre} {profesor.apellido}")
        return profesor
    except Profesor.DoesNotExist:
        print("No se encontró ningún profesor con ese Rut.")
        return None
    except Exception as e:
        print(f"Error al obtener el profesor: {e}")
        return None

def obtiene_curso(codigo):
    try:
        curso = Curso.objects.get(codigo=codigo)
        print(f"Curso encontrado: {curso.nombre}")
        return curso
    except Curso.DoesNotExist:
        print("No se encontró ningún curso con ese código.")
        return None
    except Exception as e:
        print(f"Error al obtener el curso: {e}")
        return None

def agrega_profesor_a_curso(profesor, curso):
    try:
        curso.profesores.add(profesor)
        print("Profesor agregado al curso correctamente.")
    except Exception as e:
        print(f"Error al agregar profesor al curso: {e}")

def agrega_cursos_a_estudiante(estudiante, curso):
    try:
        estudiante.curso=curso
        estudiante.save()
        print("Curso agregado al estudiante correctamente.")
    except Exception as e:
        print(f"Error al agregar cursos al estudiante: {e}")

def imprime_estudiante_cursos():
    try:
        # Obtener todos los cursos registrados
        cursos = Curso.objects.all()
        
        # Iterar sobre cada curso
        for curso in cursos:
            print(f"Curso: {curso.codigo} - {curso.nombre} (Versión {curso.version})")
            print("Estudiantes:")
            estudiantes_curso = curso.estudiante_set.all()
            if estudiantes_curso.exists():
                for estudiante_curso in estudiantes_curso:
                    print(f"- {estudiante_curso.nombre} {estudiante_curso.apellido} (RUT: {estudiante_curso.rut})")
            else:
                print("- No hay estudiantes asociados a este curso")
            print("------------------------------------------")
    except Exception as e:
        print(f"Error al imprimir los cursos y sus estudiantes: {e}")




#Usados para pruebas
def eliminar_estudiante(rut_estudiante):
    try:
        # Buscar el estudiante por su RUT
        estudiante = Estudiante.objects.get(rut=rut_estudiante)
        
        # Eliminar el estudiante
        estudiante.delete()
        
        print("Estudiante eliminado correctamente.")
    except Estudiante.DoesNotExist:
        print("No se encontró ningún estudiante con ese RUT.")
    except Exception as e:
        print(f"Error al eliminar el estudiante: {e}")

def eliminar_profesor(rut_profesor):
    try:
        # Buscar el profesor por su RUT
        profesor = Profesor.objects.get(rut=rut_profesor)
        
        # Eliminar el profesor
        profesor.delete()
        
        print("Profesor eliminado correctamente.")
    except Profesor.DoesNotExist:
        print("No se encontró ningún profesor con ese RUT.")
    except Exception as e:
        print(f"Error al eliminar el profesor: {e}")

def eliminar_curso(codigo_curso):
    try:
        # Buscar el curso por su código
        curso = Curso.objects.get(codigo=codigo_curso)
        
        # Eliminar el curso
        curso.delete()
        
        print("Curso eliminado correctamente.")
    except Curso.DoesNotExist:
        print("No se encontró ningún curso con ese código.")
    except Exception as e:
        print(f"Error al eliminar el curso: {e}")