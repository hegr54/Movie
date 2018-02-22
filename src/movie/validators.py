from django.core.exceptions import ValidationError


# def validacion_companias(value):

def validacion_studio(value):
    if not len(value) >10:
        raise ValidationError('Mínimo 10 caracteres')


def validacion_studio1(value):
    Studio=('Hollywood','Sony Pictures Entertainment','Warder Bros','New Century Films','Century Fox Animation')
    for i in Studio:
        if value == Studio:
            return value
        else:
            raise ValidationError('No existe dicho estudio')   # array.append("Hollywood","Warner Bros","New Century Films")
    # if value == array:
    #     return value
    # else:
    #     raise ValidationError('no existe dicho estudio')
    # if value == "Hollywood":
    #     return value
    # else:
    #     raise ValidationError('no existe dicho estudio')
