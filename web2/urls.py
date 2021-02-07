"""web2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('adminhome/',views.adminhome),
    path('login/',views.login),
    path('appointstaff/',views.appointstaff),
    path('savestaff/',views.savestaff),
    path('viewstaff/',views.viewstaff),
    path('editstaff/<int:id>',views.editstaff),
    path('updatestaff/<int:id>',views.updatestaff),
    path('removestaff/<int:id>',views.removestaff),
    path('savecust/',views.savecust),
    path('custhome/',views.custhome),
    path('addcategory/',views.addcategory),
    path('categoryadd/',views.categoryadd),
    path('viewcategory/',views.viewcategory),
    path('removecat/<int:id>',views.removecat),
    path('addproduct/',views.addproduct),
    path('productadd/',views.productadd),
    path('viewproducts/<int:id>',views.viewproducts),
    path('removeprod/<int:id>',views.removeprod),
    path('staffhome/',views.staffhome),
    path('custviewprods/<int:id1>/<int:id2>',views.custviewprods),
    path('generateporder/',views.generateporder),
    path('pordergenform/<int:id>',views.pordergenform),
    path('pordergen/',views.pordergen),
    path('stockupdate/<int:id>',views.stockupdate),
    path('updatestock/<int:id>',views.updatestock),
    path('staffcategoryview/',views.staffcategoryview),
    path('staffviewprods/<int:id>',views.staffviewprods),
    path('custprodview/<int:id1>/<int:id2>',views.custprodview),
    path('addcart/<int:id>',views.addcart),
    path('shopcart/<int:id>',views.shopcart),
    path('givereview/',views.givereview),
    path('complaintreg/',views.complaintreg),
    path('shopcart/<int:id>',views.shopcart),
    path('checkout/<int:id>',views.checkout),
    path('payamt/',views.payamt),
    path('about/',views.about),
    path('custsearchprod/<int:id>',views.custsearchprod),
    path('searchprod/',views.searchprod),
    path('vieworders/',views.vieworders),
    path('orderdtl/<int:id>',views.orderdtl),
    path('deliver/<int:id>',views.deliver),
    path('delvrysubmit/<int:id>',views.delvrysubmit),
    path('stockreport/',views.stockreport),
    path('salesreport/',views.salesreport),
    path('catstockreport/<int:id>',views.catstockreport),
    path('searchprodstock/',views.searchprodstock),
    path('getsalesreport/',views.getsalesreport),
    path('checkpay/',views.checkpay),
    path('approvepay/<int:id>',views.approvepay),
    path('custvieworders/<int:id>',views.custvieworders),
    path('custorderdtl/<int:id1>/<int:id2>',views.custorderdtl),
    path('viewprod/<int:id>',views.viewprod),
    path('editprod/<int:id>',views.editprod),
    path('prodedit/<int:id>',views.prodedit),
    path('custedit/<int:id>',views.custedit),
    path('viewcomplaints/',views.viewcomplaints),
    path('adminsearchprod/',views.adminsearchprod),
    path('staffsearchprod/',views.staffsearchprod),
    path('intervalsales/',views.intervalsales),
    path('getintervalsales/',views.getintervalsales),
    path('dailysales/',views.dailysales),
    path('getdailysales/',views.getdailysales),
    path('catlist/',views.catllist),
    path('freshsale/',views.freshsale),
    path('fishsale/',views.fishsale),
    path('publicprodview/<int:id>',views.publicprodview),
    path('salesreturnprod/<int:id1>/<int:id2>',views.salesreturnprod),
    path('orderreturn/',views.orderreturn),
    path('approvereturn/<int:id>',views.approvereturn),
    path('cancelreturn/<int:id>',views.cancelreturn),
    path('returnorderdtl/<int:id>',views.returnorderdtl),
    path('cashondelivery/<int:id>',views.cashondelivery),
    path('cancelpayorder/<int:id>',views.cancelpayorder),
    path('logout/',views.logout),
    path('publicviewprods/<int:id>',views.publicviewprods),
    path('viewcustinfo/<str:id>',views.viewcustinfo),
    path('removefromcart/<int:id>',views.removefromcart),

    

    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)