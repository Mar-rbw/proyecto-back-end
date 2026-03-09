"""
URL configuration for almaUnion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from almaUnionApp.views import (renderTemplateMenuInicial, renderTemplateRegistroEmpresa,
                                renderTemplateRegistroInfluencer, renderTemplateInicio,
                                renderTemplateHubEmpresa,renderTemplateHubInfluencer,
                                renderTemplateCampanias,renderTemplateConfiguracion,
                                renderTemplateInfluencers, renderTemplateInformes,
                                renderTemplateMensajes,renderTemplatePagos,
                                renderTemplateOportunidades,renderTemplatePerfil,
                                actualizar_influencer, renderTemplateColaboracion,
                                renderTemplateColaboracionCrear,renderTemplateColaboracionCrearOK,
                                renderTemplateModificarColaboracion, renderTemplateModificarColaboracionOK,
                                renderTemplateEliminarColaboracion, renderTemplateEliminarColaboracionOK,
                                renderTemplatePerfil, renderTemplateCrearCampanias,
                                renderTemplateModificarCampanias, renderTemplateEliminarCampanias,
                                renderTemplateCrearCampaniasOK, renderTemplateModificarCampaniasOK,
                                renderTemplateEliminarCampaniaOK, renderTemplateRedesSociales,
                                renderTemplateRedesSocialesCrear, renderTemplateRedesSocialesModificar,
                                renderTemplateRedesSocialesEliminar, renderTemplateCierreSesión,
                                renderTemplateOportunidadesDetalles, seleccionarCampana,
                                actualizar_empresa,
                                )
urlpatterns = [
    # Agrupación path admin 
    path('admin/', admin.site.urls),
    # Agrupación path Menu inicial
    path("", renderTemplateMenuInicial, name='inicio'),
    path("logout", renderTemplateCierreSesión, name='logout'),
    # Agrupación path Registro de usuario
    path("registroEmpresa/", renderTemplateRegistroEmpresa, name='registroEmpresa'),
    path("registroInfluencer/", renderTemplateRegistroInfluencer, name='registroInfluencer'),
    path("login/", renderTemplateInicio, name='login'),
    path("empresa/editar/", actualizar_empresa, name="actualizar_empresa"),
    path("influencer/editar/", actualizar_influencer, name="actualizar_influencer"),
    # Agrupación path redirección al Hub
    path("hubEmpresa/", renderTemplateHubEmpresa, name='hubEmpresa'),
    path("hubInfluencer/", renderTemplateHubInfluencer, name='hubInfluencer'),
    # agrupación path redirección aside común influencer-Empresa
    path("perfil/", renderTemplatePerfil, name='perfil'), 
    path("configuracion/", renderTemplateConfiguracion, name='configuracion'),
    path("redSocial/<int:pk>", renderTemplateRedesSociales, name='redSocial'),
    path("redSocial/<int:pk>/crear", renderTemplateRedesSocialesCrear, name='redSocialCrear'),
    path("redSocial/<int:pk>/modificar", renderTemplateRedesSocialesModificar, name='redSocialModificar'),
    path("redSocial/<int:pk>/eliminar", renderTemplateRedesSocialesEliminar, name='redSocialEliminar'),
    # Agrupación path redirección aside Empresa
    path("influencers/", renderTemplateInfluencers, name='influencers' ),
    path("campanias/", renderTemplateCampanias, name='campanias'),
    path("mensajes/", renderTemplateMensajes, name='mensajes'),
    path("pagos/", renderTemplatePagos, name='pagos'),
    # Agrupación path redirección aside influencers
    path("colaboraciones/", renderTemplateColaboracion, name="colaboracion"),
    path("colaboraciones/crear/", renderTemplateColaboracionCrear, name="crearColaboracion"),
    path("colaboraciones/modificar/", renderTemplateModificarColaboracion, name='modificarColaboracion'),
    path("colaboraciones/eliminar/", renderTemplateEliminarColaboracion, name='eliminarColaboracion'),
    path("colaboraciones/crearOK/", renderTemplateColaboracionCrearOK, name="crearColaboracionOK"),
    path("colaboraciones/modificarOK/", renderTemplateModificarColaboracionOK, name="modificarColaboracionOK"),
    path("colaboraciones/eliminarOK/", renderTemplateEliminarColaboracionOK, name="eliminarColaboracionOK<"),
    # Agrupación path redirección campañias
   path("campanias/crear/", renderTemplateCrearCampanias, name='crearCampanias'),
   path("campanias/modificar/", renderTemplateModificarCampanias, name='modificarCampanias'),
   path("campanias/eliminar/", renderTemplateEliminarCampanias, name='eliminarCampanias'),
   path("campanias/crearOK/", renderTemplateCrearCampaniasOK, name='crearCampaniasOK'),
   path("campanias/modificarOK/", renderTemplateModificarCampaniasOK, name='modificarCampaniasOK'),
   path("campanias/EliminarOK/", renderTemplateEliminarCampaniaOK, name='eliminarCampaniasOK'),
   # Agrupación path redirección oportunidades
   path("oportunidades/", renderTemplateOportunidades, name='oportunidades'),
   path("oportunidades/detalles/", renderTemplateOportunidadesDetalles, name='oportunidadesDetalles'),
   path('oportunidades/seleccionar/', seleccionarCampana, name='seleccionarCampana'),
    path('oportunidades/detalle/', renderTemplateOportunidadesDetalles, name='detalleOportunidad'),
   
   path("informes/", renderTemplateInformes, name='informes'),
   
]
