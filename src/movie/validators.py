from django.core.exceptions import ValidationError


# def validacion_companias(value):

def validacion_studio(value):
    if not len(value) >8:
        raise ValidationError('Mínimo 12 caracteres')


def validacion_studio1(value):
    a=["Hollywood"]
    for i in range (len(a)):
        if value == a[i]:
             return value
        else:
             raise ValidationError('no existe dicho estudio')
    # array.append("Hollywood","Warner Bros","New Century Films")
    # if value == array:
    #     return value
    # else:
    #     raise ValidationError('no existe dicho estudio')
    # if value == "Hollywood":
    #     return value
    # else:
    #     raise ValidationError('no existe dicho estudio')
