from django import forms
from ..models import Usuarios, Empresas
from .formBase.BaseRutEmpresaForm import BaseRutEmpresaForm
from .formBase.BaseNombreEmpresaForm import BaseNombreEmpresaForm
from .formBase.BaseCategoriaEmpresaForm import BaseCategoriaEmpresaForm
from .formBase.BaseImagenPerfilForm import BaseImagenPerfilForm


class ActualizarEmpresaForm(BaseRutEmpresaForm, BaseNombreEmpresaForm, BaseCategoriaEmpresaForm):
    class Meta:
        model = Empresas
        fields = [
            "rut_empresa",
            "nombre_empresa",
            "categoria_empresa"
        ]
        
class ActualizarImagenForm(BaseImagenPerfilForm):
    class Meta:
        model = Usuarios
        fields = ["imagen_perfil"]