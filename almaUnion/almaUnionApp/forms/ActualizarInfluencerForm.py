from ..models import Influencers, Usuarios
from .formBase.BaseRutInfluencerForm import BaseRutInfluencerForm
from .formBase.BaseNombreForm import BaseNombreForm
from .formBase.BaseApellidoPatForm import BaseApellidoPatForm
from .formBase.BaseApellidoMatForm import BaseApellidoMatForm
from .formBase.BaseCategoriaInfluencerForm import BaseCategoriaInfluencerForm
from .formBase.BaseSeguidoresForm import BaseSeguidoresForm
from .formBase.BasePromViewsForm import BasePromViewsForm
from .formBase.BaseImagenPerfilForm import BaseImagenPerfilForm


class ActualizarInfluencerForm(BaseRutInfluencerForm,
                               BaseNombreForm, 
                               BaseApellidoPatForm, 
                               BaseApellidoMatForm, 
                               BaseCategoriaInfluencerForm, 
                               BaseSeguidoresForm, 
                               BasePromViewsForm):
    class Meta:
        model = Influencers
        fields = ['rut_influencer',
                  'nombre',
                  'apellido_pat',
                  'apellido_mat',
                  'categoria_influencer',
                  'seguidores',
                  'prom_views']
        
class ActualizarImagenForm(BaseImagenPerfilForm):
    class Meta:
        model = Usuarios
        fields = ["imagen_perfil"]
        