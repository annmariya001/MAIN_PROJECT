
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
'''from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)'''

urlpatterns = [
    path('',views.home,name='home'),
    path('admin/', admin.site.urls),
    path('login',views.login, name='login'),
    path('log',views.log, name='log'),
    path('home', views.home, name='home'),
    path('ureg',views.ureg ,name='ureg'),
    path('reg',views.reg ,name='reg'),
    path('uhome',views.uhome,name='uhome'),
    path('add',views.add ,name='add'),
    path('show',views.show ,name='show'),
    path('report',views.report,name='report'),
    path('addfood',views.addfood,name='addfood'),
    path('afood',views.afood,name='afood'),
    path('price',views.price ,name='price'),
    path('description',views.description ,name='description'),
    path('category',views.category,name='category'),
    path('category1',views.category1,name='category1'),
    path('fcategories',views.fcategories,name='fcategories'),
    path('foodview',views.foodview,name='foodview'),
    path('categoryview', views.categoryview, name='categoryview'),
    path('edit',views.edit,name='edit'),
    path('update', views.update, name='update'),
    path('addchef',views.addchef,name='addchef'),
    path('achef',views.achef,name='achef'),
    path('foodlist', views.foodlist, name='foodlist'),
    path('tableset',views.tableset,name='tableset'),
    path('tset',views.tset,name='tset'),
    path('reservations',views.reservation,name='reservations'),
    path('fooddetails',views.fooddetails,name='fooddetails'),
    path('reservationreport',views.reservationreport,name='reservationreport'),
    path('about',views.about,name='about'),
    path('ser',views.ser,name='search'),
    path('det',views.det,name='det'),
    path('tablereservation',views.tablereservation,name='tablereservation'),
    path('ntablereservation',views.ntablereservation,name='ntablereservation'),


]

