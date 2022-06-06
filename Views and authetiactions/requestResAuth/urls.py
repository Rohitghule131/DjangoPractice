from django.urls import path
import requestResAuth.views  as view
urlpatterns = [
    path('mxlist/',view.Personlist.as_view(),name="mxlist"),
    # path('mxcr/',view.PersonCreate.as_view(),name="mxcr"),
    path('mxrt/<int:pk>/',view.PersonRetrive.as_view(),name="mxrt"),
    path('auth/',view.AuthView.as_view(),name="auth"),
    path('mxcr/',view.PersonCreate.as_view(),name = 'mxcr'),
    path('mxcar/',view.CarView.as_view(),name='mxcar'),
    path('update/<int:pk>',view.updataPerson.as_view(),name = 'update'),
    path('prView/',view.PermitView.as_view(),name = 'prView'),
    path('prViewonlyRead/<int:id>',view.ReadOnly.as_view(),name = 'prViewRead'),

]