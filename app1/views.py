from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from app1.models import tbl_login
from app1.models import tbl_staff
from app1.models import tbl_idgen
from app1.models import tbl_category
from app1.models import tbl_product
from app1.models import tbl_customer
from app1.models import tbl_review
from app1.models import tbl_cart
from app1.models import tbl_order
from app1.models import tbl_orderdtls
from app1.models import tbl_delvrydtls
from app1.models import tbl_complaint
from app1.models import tbl_purchaseorder
from app1.models import tbl_payment
from app1.models import tbl_return
from django.db.models import F
from django.conf import settings
import datetime
from datetime import date
from django.db.models import Q
from django.contrib import messages
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
    cat=tbl_category.objects.all()
    return render(request,'index.html',{'ca':cat})

def login(request):  
    if request.method=='POST':
        data=tbl_login.objects.all()
        Username=request.POST.get('user_id')
        Password=request.POST.get('password')
        flag=0
        for da in data:
            if Username==da.user_id and Password==da.password:
                ty=da.category
                flag=1
                request.session['uid']=Username
                if ty=="admin":
                    return redirect('/adminhome')    
                elif ty=="staff":
                    return redirect('/staffhome')
                elif ty=="customer":
                    return redirect('/custhome')
                else:
                    return HttpResponse("Invalid acct type")
        if flag==0:
            return HttpResponse("User doesn't exist")

def adminhome(request):
    return render(request,'adminhome.html')


def staffhome(request):
    return render(request,'staffhome.html')

def appointstaff(request):
    data=tbl_idgen.objects.get(id=1)
    f=data.stfid
    f=f+1
    f1="STAFF"+str(f)
    request.session['STAF_ID']=f
    return render (request,'appoint_staff.html',{'ff':f1})

def savestaff(request):
    if request.method == 'POST':
        data1 = tbl_staff()
        data1.staff_id=request.POST.get('staffid')
        data1.staff_name=request.POST.get('name')
        data1.staff_address=request.POST.get('address')
        data1.join_date=date.today()
        data1.staff_phno=request.POST.get('phno')
        data1.staff_email=request.POST.get('email')
        data1.id_type=request.POST.get('idtype')
        data1.id_num=request.POST.get('idnum')
        data1.staff_status='active'
        data1.save()
        data2 = tbl_login()
        data2.user_id=data1.staff_id
        data2.password=request.POST.get('phno')
        data2.category='staff'
        data2.save()
        f=request.session['STAF_ID']
        data3 = tbl_idgen.objects.get(id=1)
        data3.stfid=f
        data3.save()
        return redirect('/adminhome')
    else:
         return HttpResponse("Invalid data type")

def viewstaff(request):
    staf=tbl_staff.objects.all()
    return render(request,'viewstaff.html',{'st':staf})
def editstaff(request,id):
    staf=tbl_staff.objects.get(id=id)
    return render(request,'editstaff.html',{'st':staf})

def updatestaff(request,id):
    staf=tbl_staff.objects.get(id=id)
    if request.method=="POST":
        staf.staff_name=request.POST.get('name')
        staf.staff_address=request.POST.get('address')
        staf.join_date=request.POST.get('dateofjoin')
        staf.staff_phno=request.POST.get('phno')
        staf.staff_email=request.POST.get('email')
        staf.staff_status=request.POST.get('status')
        staf.save()
        return redirect('/viewstaff')
    else:
         return HttpResponse("Error")

def removestaff(request,id):
    staf=tbl_staff.objects.get(id=id)
    staffid=staf.staff_id
    log=tbl_login.objects.get(user_id = staffid)
    log.delete()
    staf.delete()
    return redirect('/viewstaff')

def savecust(request):
    if request.method == 'POST':
        data=tbl_idgen.objects.get(id=1)
        f=data.ctrid
        f=f+1
        f1="CUST"+str(f)
        request.session['CU_ID']=f
        cmail=request.POST.get('custemail')
        cust = tbl_customer.objects.all()
        flag=0
        for cu in cust:
            if(cu.cust_email == cmail):
                flag=1
                break
        if(flag == 0):
            data1 = tbl_customer()
            data1.cust_id=f1
            data1.cust_name=request.POST.get('custname')
            data1.cust_address=request.POST.get('custaddress')
            data1.cust_phno=request.POST.get('custphno')
            data1.cust_email=request.POST.get('custemail')
            data1.save()
            data2 = tbl_login()
            data2.user_id=request.POST.get('custemail')
            data2.password=request.POST.get('password')
            data2.category="customer"
            data2.save()
            data.ctrid=f
            data.save()
            # mailid = request.POST.get('custemail')
            # message = 'Greetings, Successfully Redistered. Start shopping!!. Use registered mail ID for login : '+ mailid
            # send_mail('Freshwagon Online Shopping',message,settings.EMAIL_HOST_USER,[data1.cust_email])
            return redirect('/')
        else:
            return HttpResponse("Existing Email ID, Try Login")
    else:
         return HttpResponse("Invalid data type")

def custhome(request):
    cat=tbl_category.objects.all()
    custemail=request.session['uid']
    cust=tbl_customer.objects.get(cust_email=custemail)
    return render(request,'custhome.html',{'ca':cat, 'cu':cust})

def addcategory(request):
    data=tbl_idgen.objects.get(id=1)
    f=data.ctyid
    f=f+1
    f1="CATEGORY"+str(f)
    request.session['C_ID']=f
    return render (request,'addcategory.html',{'ff':f1})

def categoryadd(request):
    if request.method == 'POST':
        cat_img = request.FILES['catimg']
        fs = FileSystemStorage()
        filename = fs.save(cat_img.name, cat_img)
        uploaded_file_url = fs.url(filename)
        data = tbl_category()
        data.cat_id=request.POST.get('catid')
        data.cat_name=request.POST.get('catname')
        data.cat_desc=request.POST.get('catdesc')
        data.cat_img=uploaded_file_url
        data.save()
        f=request.session['C_ID']
        data1 = tbl_idgen.objects.get(id=1)
        data1.ctyid=f
        data1.save()
        return redirect('/adminhome')
    else:
         return HttpResponse("Invalid data type")






def viewcategory(request):
    cate=tbl_category.objects.all()
    return render(request,'viewcategory.html',{'ct':cate})


def removecat(request,id):
    cat=tbl_category.objects.get(id=id)
    cat.delete()
    return redirect('/viewcategory')

def addproduct(request):
    data=tbl_idgen.objects.get(id=1)
    f=data.pdtid
    f=f+1
    f1="PRODUCT"+str(f)
    request.session['P_ID']=f
    cate=tbl_category.objects.all()
    return render(request,'addproduct.html',{'ff':f1 , 'ct':cate})
    
def productadd(request):
    if request.method == 'POST':
        prod_img = request.FILES['prodimg']
        fs = FileSystemStorage()
        filename = fs.save(prod_img.name, prod_img)
        uploaded_file_url = fs.url(filename)
        data = tbl_product()
        data.prod_id=request.POST.get('prodid')
        data.cat_id=request.POST.get('catid')
        data.prod_name=request.POST.get('prodname')
        data.prod_desc=request.POST.get('proddesc')
        data.prod_unit=request.POST.get('produnit')
        data.prod_price=request.POST.get('prodprice')
        data.prod_img=uploaded_file_url
        data.prod_stkqty=request.POST.get('prodstkqty')
        data.prod_rol=request.POST.get('prodrol')
        data.prod_status="on stock"
        data.save()
        f=request.session['P_ID']
        data1 = tbl_idgen.objects.get(id=1)
        data1.pdtid=f
        data1.save()
        return redirect('/adminhome')
    else:
         return HttpResponse("Invalid data type")



def viewproducts(request,id):
    cat=tbl_category.objects.get(id=id)
    catid=cat.cat_id
    prod=tbl_product.objects.filter(cat_id=catid)
    return render(request,'viewproducts.html',{'pd':prod})


def removeprod(request,id):
    prod=tbl_product.objects.get(id=id)
    prod.delete()
    return redirect('/viewcategory')

def custviewprods(request,id1,id2):
    catt=tbl_category.objects.all()
    cat=tbl_category.objects.get(id=id1)
    catid=cat.cat_id
    cust=tbl_customer.objects.get(id=id2)
    prod=tbl_product.objects.filter(cat_id=catid)
    return render(request,'custviewprods.html',{'pd':prod, 'cu':cust, 'ca':catt})

def generateporder(request):
    prod=tbl_product.objects.filter(prod_status='reorder')
    prod1=tbl_product.objects.filter(prod_status='ordered')
    return render(request,'generateporder.html',{'pro':prod, 'pro1':prod1})

def pordergenform(request,id):
    prod=tbl_product.objects.get(id=id)
    data=tbl_idgen.objects.get(id=1)
    f=data.podrid
    f=f+1
    f1="PORDER"+str(f)
    request.session['POD_ID']=f
    return render(request,'pordergenform.html',{'pro':prod, 'ff':f1})

def pordergen(request):
    if request.method == 'POST':
        data=tbl_purchaseorder()
        data.porder_id=request.POST.get('porderid')
        data.prod_id=request.POST.get('prodid')
        data.prod_name=request.POST.get('prodname')
        data.req_qty=request.POST.get('reqqty')
        data.porder_dt=request.POST.get('orddate')
        data.save()
        prodid=data.prod_id
        prod=tbl_product.objects.get(prod_id=prodid)
        prod.prod_status="ordered"
        prod.save()
        data1=tbl_idgen.objects.get(id=1)
        f=request.session['POD_ID']
        data1.podrid=f
        data1.save()
        return redirect('/generateporder')
    else:
        return HttpResponse("Error")

def stockupdate(request,id):
    prod=tbl_product.objects.get(id=id)
    return render(request,'stockupdate.html',{'pr':prod})

def updatestock(request,id):
    prod=tbl_product.objects.get(id=id)
    if request.method=="POST":
        prod.prod_price=request.POST.get('prodprice')
        prod.prod_stkqty=request.POST.get('prodstkqty')
        prod.prod_status=request.POST.get('prodstatus')
        stk = float(prod.prod_stkqty)
        if(stk > prod.prod_rol):
            prod.prod_status = "onstock"
        prod.save()
        return redirect('/staffcategoryview')
    else:
         return HttpResponse("Error")

def staffcategoryview(request):
    cate=tbl_category.objects.all()
    return render(request,'staffcategoryview.html',{'ct':cate})

def staffviewprods(request,id):
    cat=tbl_category.objects.get(id=id)
    catid=cat.cat_id
    prod=tbl_product.objects.filter(cat_id=catid)
    return render(request,'staffviewprods.html',{'pd':prod})

def custprodview(request,id1,id2):
    catt = tbl_category.objects.all()
    prod=tbl_product.objects.get(id=id1)
    prodid=prod.prod_id
    cust=tbl_customer.objects.get(id=id2)
    rev=tbl_review.objects.filter(prod_id=prodid)
    data=tbl_idgen.objects.get(id=1)
    f=data.ctid
    f=f+1
    f1="CART"+str(f)
    request.session['CAR_ID']=f
    
    z=data.revwid
    z=z+1
    z1="REVIEW"+str(z)
    request.session['RW_ID']=z
    
    c=data.comid
    c=c+1
    c1="COMPLAINT"+str(c)
    request.session['CO_ID']=c
    if prod.prod_stkqty < 1:
        return render(request,'custoutofstkprodview.html',{'pr':prod, 're':rev, 'ff':f1, 'cu':cust, 'zz':z1, 'cc':c1,'ca':catt})
    elif prod.prod_unit=='Kg':
        return render(request,'custprodviewkg.html',{'pr':prod, 're':rev, 'ff':f1, 'cu':cust, 'zz':z1, 'cc':c1,'ca':catt})
    elif prod.prod_unit=='L':
        return render(request,'custprodviewl.html',{'pr':prod, 're':rev, 'ff':f1, 'cu':cust, 'zz':z1, 'cc':c1,'ca':catt})
    else:
        return render(request,'custprodviewnos.html',{'pr':prod, 're':rev, 'ff':f1, 'cu':cust, 'zz':z1, 'cc':c1,'ca':catt})

    

def addcart(request,id):
    if request.method == 'POST':
        custemail=request.session['uid']
        cust=tbl_customer.objects.get(cust_email=custemail)
        prod=tbl_product.objects.get(id=id)
        data=tbl_cart()
        data.cart_id=request.POST.get('cartid')
        data.cust_id=cust.cust_id
        data.prod_id=prod.prod_id
        data.prod_name=prod.prod_name
        data.order_qty=request.POST.get('radio')
        data.prod_price=float(data.order_qty)*prod.prod_price
        data.save()
        f=request.session['CAR_ID']
        data1 = tbl_idgen.objects.get(id=1)
        data1.ctid=f
        data1.save()
        return redirect('/custhome')
    else:
         return HttpResponse("Error")

def givereview(request):
    if request.method == 'POST':
        data=tbl_review()
        data.rev_id=request.POST.get('revid')
        data.prod_id=request.POST.get('prodid')
        data.cust_id=request.POST.get('custid')
        data2=tbl_customer.objects.get(cust_id=data.cust_id)
        data.cust_name=data2.cust_name
        data.review=request.POST.get('reviews')
        data.save()
        z=request.session['RW_ID']
        data1 = tbl_idgen.objects.get(id=1)
        data1.revwid=z
        data1.save()
        return redirect('/custhome')
    else:
        return HttpResponse("Error")


def complaintreg(request):
    if request.method == 'POST':
        data=tbl_complaint()
        data.comp_id=request.POST.get('compid')
        data.cust_id=request.POST.get('custid')
        data2=tbl_customer.objects.get(cust_id=data.cust_id)
        data.cust_name=data2.cust_name
        data.prod_id=request.POST.get('prodid')
        data.complaint=request.POST.get('comp')
        data.comp_date=datetime.datetime.now()
        data.save()
        c=request.session['CO_ID']
        data1=tbl_idgen.objects.get(id=1)
        data1.comid=c
        data1.save()
        return redirect('/custhome')
    else:
        return HttpResponse("Error")

def shopcart(request,id):
    cust=tbl_customer.objects.get(id=id)
    custid=cust.cust_id
    cart=tbl_cart.objects.filter(cust_id=custid)
    tot=0
    for ca in cart:
        tot=tot+ca.prod_price
    data=tbl_idgen.objects.get(id=1)
    f=data.odtlsid
    f=f+1
    f1="ORDTLS"+str(f)
    request.session['ODTL_ID']=f
    data1=tbl_idgen.objects.get(id=1)
    z=data.odrid
    z=z+1
    z1="ORDER"+str(z)
    request.session['ORD_ID']=z
    return render(request,'shoppingcart.html',{'ca':cart, 'cu':cust, 'ff':f1, 'zz':z1, 'tt':tot})

def removefromcart(request,id):
    cart=tbl_cart.objects.get(id=id)
    custid=cart.cust_id
    cust=tbl_customer.objects.get(cust_id=custid)
    id1=cust.id
    cart.delete()
    return redirect('/custhome')

    
def checkout(request,id):
    if request.method == 'POST':
        cust=tbl_customer.objects.get(id=id)
        custid=cust.cust_id
        cart=tbl_cart.objects.filter(cust_id=custid)
        tot=0
        for ca in cart:
            data2=tbl_orderdtls()
            data2.orderdtls_id=request.POST.get('ordtlsid')
            data2.order_id=request.POST.get('orderid')
            data2.prod_id=ca.prod_id
            data2.prod_name=ca.prod_name
            data2.order_qty=ca.order_qty
            data2.prod_amt=ca.prod_price
            data2.order_status="not processed"
            data2.save()
            f=request.session['ODTL_ID']
            data3 = tbl_idgen.objects.get(id=1)
            data3.odtlsid=f
            data3.save()
            tot=tot+data2.prod_amt
            data5=tbl_product.objects.filter(prod_id=ca.prod_id)
            for pd in data5:
                pd.prod_stkqty=pd.prod_stkqty-ca.order_qty
                if pd.prod_stkqty<=pd.prod_rol:
                    pd.prod_status="reorder"
                elif pd.prod_stkqty>=pd.prod_rol:
                    pd.prod_status="onstock"
                elif pd.prod_stkqty<1:
                    pd.prod_status="outofstock"
                pd.save()    
        data1=tbl_order()
        data1.order_id=request.POST.get('orderid')
        data1.order_dt=datetime.datetime.now().date()
        data1.cust_id=custid
        data1.order_amt=tot
        data1.order_paymode = 'Bank'
        data1.order_status="not processed"
        data1.save()
        z=request.session['ORD_ID']
        data4 = tbl_idgen.objects.get(id=1)
        data4.odrid=z
        data4.save()
        for ca in cart:
            ca.delete()
        p=data3.pmntid
        p=p+1
        p1="PAYMENT"+str(p)
        request.session['PAY_ID']=p
        return render(request,'payment.html',{'odd':data1, 'cu':cust, 'tt':tot, 'pp':p1})
    else:
         return HttpResponse("Error")


def payamt(request):
    if request.method == 'POST':
        data=tbl_payment()
        data.payment_id=request.POST.get('paymentid')
        data.order_id=request.POST.get('orderid')
        data.payment_amt=request.POST.get('orderamt')
        data.cust_id=request.POST.get('custid')
        data.bank_name=request.POST.get('bankname')
        data.ifsc_code=request.POST.get('ifsc')
        data.acc_no=request.POST.get('accno')
        data.payment_dt=datetime.datetime.now()
        data.payment_status="not processed"
        p=request.session['PAY_ID']
        data1 = tbl_idgen.objects.get(id=1)
        data1.pmntid = p
        data1.save()
        data.save()
        return redirect('/custhome')
    else:
        return HttpResponse("Error")

def about(request):
    return render(request,'about.html')

def custsearchprod(request,id):
    if request.method == 'POST':
        catt = tbl_category.objects.all()
        cust=tbl_customer.objects.get(id=id)
        val=request.POST.get('search')
        prod=tbl_product.objects.filter(prod_name__icontains=val)
        return render(request,'custsearchview.html',{'pd':prod, 'cu':cust, 'ca':catt})
def searchprod(request):
    if request.method == 'POST':
        catt = tbl_category.objects.all()
        val=request.POST.get('search')
        prod=tbl_product.objects.filter(prod_name__icontains=val)
        return render(request,'searchview.html',{'pd':prod, 'ca':catt})
def adminsearchprod(request):
    if request.method == 'POST':
        val=request.POST.get('search')
        prod=tbl_product.objects.filter(prod_name__icontains=val)
        return render(request,'viewproducts.html',{'pd':prod})
def staffsearchprod(request):
    if request.method == 'POST':
        val=request.POST.get('search')
        prod=tbl_product.objects.filter(prod_name__icontains=val)
        return render(request,'staffviewprods.html',{'pd':prod})

def vieworders(request):
    orders=tbl_order.objects.filter(order_status='not processed').filter(~Q(order_status='return'))
    return render(request,'vieworders.html',{'or':orders})


def orderdtl(request,id):
    order=tbl_order.objects.get(id=id)
    custid=order.cust_id
    cust=tbl_customer.objects.get(cust_id=custid)
    ordtls=tbl_orderdtls.objects.filter(order_id=order.order_id)
    if order.order_paymode == 'Bank':
        pay=tbl_payment.objects.get(order_id=order.order_id)
        return render(request,'orderdtl.html',{'or':ordtls, 'orr':order, 'cu':cust, 'pa':pay})
    else:
        codd="Cash On Delivery"
        return render(request,'orderdtl.html',{'or':ordtls, 'orr':order, 'cu':cust, 'cod':codd})


def deliver(request,id):
    order=tbl_order.objects.get(id=id)
    data=tbl_idgen.objects.get(id=1)
    f=data.dvryid
    f=f+1
    f1="DELIVERY"+str(f)
    request.session['DL_ID']=f
    return render(request,'delvrydtls.html',{'ff':f1,'or':order})

def delvrysubmit(request,id):
    if request.method == 'POST':
        order=tbl_order.objects.get(id=id)
        ordtls=tbl_orderdtls.objects.filter(order_id=order.order_id)
        data=tbl_delvrydtls()
        data.delvry_id=request.POST.get('delid')
        data.order_id=request.POST.get('orderid')
        data.delvry_dt=request.POST.get('deldt')
        data.courier_name=request.POST.get('Couriername')
        data.delvry_remark=request.POST.get('delremark')
        data.save()
        f=request.session['DL_ID']
        data1 = tbl_idgen.objects.get(id=1)
        data1.dvryid=f
        data1.save()
        order.order_status="delivered"
        order.save()
        for ordt in ordtls:
            ordt.order_status="delivered"
            ordt.save()
        return redirect('/vieworders')
    else:
        return HttpResponse("Error")
        

def stockreport(request):
    cat=tbl_category.objects.all()
    prod=tbl_product.objects.all()
    return render(request,'stockreport.html',{'ca':cat, 'pro':prod})

def salesreport(request):
    odr=tbl_order.objects.all()
    return render(request,'salesreport.html',{'od':odr})

def catstockreport(request,id):
    caty=tbl_category.objects.all()
    cat=tbl_category.objects.get(id=id)
    prod=tbl_product.objects.filter(cat_id=cat.cat_id)
    return render(request,'catstockreport.html',{'pro':prod, 'ca':cat, 'cy':caty})

def searchprodstock(request):
    if request.method == 'POST':
        val=request.POST.get('searchstock')
        prod=tbl_product.objects.filter(prod_name__icontains=val)
        cat=tbl_category.objects.all()
        return render(request,'stockreport.html',{'pro':prod, 'ca':cat})
    else:
        return HttpResponse("Error")

def getsalesreport(request):
    if request.method == 'POST':
        monthsale=request.POST.get('monthsales')
        yearsale=request.POST.get('yearsales')
        odr=tbl_order.objects.filter(order_dt__month=monthsale).filter(order_dt__year=yearsale)
        tot=0
        sret = 0
        for odd in odr:
            tot=tot+odd.order_amt
            if(odd.order_status == 'returned'):
                sret = sret + odd.order_amt
        reve = tot - sret
        return render(request,'salesreport.html',{'od':odr, 'tt':tot, 'ret':sret, 'rev':reve})
    else:
         return HttpResponse("Error")

def checkpay(request):
    npay=tbl_payment.objects.filter(payment_status='not processed')
    opay=tbl_payment.objects.filter(payment_status='approved')
    return render(request,'checkpayment.html',{'n':npay, 'o':opay})

def approvepay(request,id):
    pay=tbl_payment.objects.get(id=id)
    pay.payment_status="approved"
    pay.save()
    return redirect('/checkpay')

def custvieworders(request,id):
    cust=tbl_customer.objects.get(id=id)
    custid=cust.cust_id
    order=tbl_order.objects.filter(cust_id=custid).filter(Q(order_status ='not processed') | Q(order_status = 'cash on delivery')).filter(~Q(order_status='return'))
    porder=tbl_order.objects.filter(cust_id=custid).filter(order_status ='delivered')
    returns=tbl_order.objects.filter(cust_id=custid).filter(order_status='returned')
    return render(request,'custvieworders.html',{'or':order, 'por':porder, 'cu':cust, 'ret':returns})

def custorderdtl(request,id1,id2):
    order=tbl_order.objects.get(id=id1)
    cust=tbl_customer.objects.get(id=id2)
    ordtls=tbl_orderdtls.objects.filter(order_id=order.order_id)
    return render(request,'custorderdtl.html',{'or':ordtls, 'orr':order, 'cu':cust})


def viewprod(request,id):
    prod=tbl_product.objects.get(id=id)
    return render(request,'viewprod.html',{'pr':prod})

def editprod(request,id):
    prod=tbl_product.objects.get(id=id)
    return render(request,'editprod.html',{'pr':prod})

def prodedit(request,id):
    if request.method == 'POST':
        data=tbl_product.objects.get(id=id)
        data.prod_name=request.POST.get('prodname')
        data.prod_desc=request.POST.get('proddesc')
        data.prod_unit=request.POST.get('produnit')
        data.prod_price=request.POST.get('prodprice')
        data.prod_stkqty=request.POST.get('stkqty')
        data.prod_rol=request.POST.get('prodrol')
        data.save()
        return render(request,'viewprod.html',{'pr':data})
    else:
        return HttpResponse("Error")

def custedit(request,id):
    if request.method == 'POST':
        cust=tbl_customer.objects.get(id=id)
        cust.cust_name=request.POST.get('custname')
        cust.cust_phno=request.POST.get('custphno')
        cust.cust_address=request.POST.get('custaddress')
        cust.save()
        cat=tbl_category.objects.all()
        return render(request,'custhome.html',{'ca':cat, 'cu':cust})
    else:
        return HttpResponse("Error")

def viewcomplaints(request):
    comp=tbl_complaint.objects.all()
    return render(request,'viewcomplaints.html',{'co':comp})

def intervalsales(request):
    return render(request,'intervalsales.html')

def getintervalsales(request):
    if request.method == 'POST':
        date1=request.POST.get('initial_dt')
        date2=request.POST.get('final_dt')
        odr=tbl_order.objects.filter(order_dt__range=(date1,date2))
        tot = 0
        sret = 0
        for od in odr:
            tot=tot+od.order_amt
            if (od.order_status == "returned"):
                sret = sret + od.order_amt
        reve = tot - sret
        return render(request,'intervalsales.html',{'od':odr,'tt':tot, 'ret':sret, 'rev':reve})
    else:
         return HttpResponse("Error")

def catllist(request):
    catid=request.POST.get('agileinfo_search')
    prod=tbl_product.objects.filter(cat_id=catid)
    user_email=request.session['uid']
    cust=tbl_customer.objects.get(cust_email=user_email)
    catt=tbl_category.objects.all()
    return render(request,'custviewprods.html',{'pd':prod, 'cu':cust, 'ca':catt})

def freshsale(request):
    catt = tbl_category.objects.all()
    cat=tbl_category.objects.get(cat_name='Vegetables')
    catid=cat.cat_id
    prod=tbl_product.objects.filter(cat_id=catid)
    return render(request,'publicviewprods.html',{'pd':prod, 'ca':catt})

def publicviewprods(request,id):
    catt = tbl_category.objects.all()
    cat=tbl_category.objects.get(id=id)
    catid=cat.cat_id
    prod=tbl_product.objects.filter(cat_id=catid)
    return render(request,'publicviewprods.html',{'pd':prod,'ca':catt})

def publicprodview(request,id):
    catt = tbl_category.objects.all()
    prod=tbl_product.objects.get(id=id)
    return render(request,'publicprodview.html',{'pd':prod,'ca':catt})

def dailysales(request):
    return render(request,'dailysales.html')

def getdailysales(request):
    if request.method == 'POST':
        date=request.POST.get('sales_dt')
        odr=tbl_order.objects.filter(order_dt=date)
        tot=0
        sret=0
        for od in odr:
            tot = tot+od.order_amt
            if(od.order_status == 'returned'):
                sret=sret+od.order_amt
        reve = tot - sret
        return render(request,'dailysales.html',{'od':odr,'tt':tot, 'ret':sret, 'rev':reve})
    else:
         return HttpResponse("Error")


def salesreturnprod(request,id1,id2):
    ordd=tbl_order.objects.get(id=id1)
    cust=tbl_customer.objects.get(id=id2)
    data=tbl_idgen.objects.get(id=1)
    f=data.retrnid
    f=f+1
    f1="RETURN"+str(f)
    request.session['RET_ID']=f
    data1=tbl_return()
    data1.return_id=f1
    data1.cust_id=cust.cust_id
    data1.order_id=ordd.order_id
    data1.order_amt=ordd.order_amt
    data1.return_status="not processed"
    data1.save()
    data.retrnid=f
    data.save()
    ordd.order_status="return"
    ordd.save()
    return redirect('/custhome')

def orderreturn(request):
    ret=tbl_return.objects.filter(return_status='not processed')
    return render(request,'orderreturns.html',{'ord':ret})

def approvereturn(request,id):
    ret=tbl_return.objects.get(id=id)
    ret.return_status="approved"
    orderid=ret.order_id
    order=tbl_order.objects.get(order_id=orderid)
    if order.order_paymode == 'Bank':
        pay=tbl_payment.objects.get(order_id=orderid)
        pay.payment_status="returned"
        pay.save()
    order.order_status="returned"
    orddtl=tbl_orderdtls.objects.filter(order_id = orderid)
    for odtl in orddtl:
        odtl.order_status = "returned"
        odtl.save()
    order.save()
    ret.save()
    return redirect('/orderreturn')

def cancelreturn(request,id):
    ret=tbl_return.objects.get(id=id)
    ordid=ret.order_id
    ordd=tbl_order.objects.get(order_id=ordid)
    ret.return_status="rejected"
    ret.save()
    ordd.order_status="delivered"
    ordd.save()
    return redirect('/orderreturn') 

    



def returnorderdtl(request,id):
    ret=tbl_return.objects.get(id=id)
    ordid = ret.order_id
    order=tbl_order.objects.get(order_id=ordid)
    custid=order.cust_id
    cust=tbl_customer.objects.get(cust_id=custid)
    ordtls=tbl_orderdtls.objects.filter(order_id=order.order_id)
    if order.order_paymode == 'Bank':
        pay=tbl_payment.objects.get(order_id=order.order_id)
        return render(request,'returnorderdtl.html',{'or':ordtls, 'orr':order, 'cu':cust, 'pa':pay, 're':ret})
    else:
        codd="Cash On Delivery"
        return render(request,'returnorderdtl.html',{'or':ordtls, 'orr':order, 'cu':cust,'cod':codd, 're':ret})



def cashondelivery(request,id):
    order=tbl_order.objects.get(id=id)
    order.order_paymode = "cash on delivery"
    order.save()
    return redirect('/custhome')
    
def cancelpayorder(request,id):
    order=tbl_order.objects.get(id=id)
    order.delete()
    orderdtl=tbl_orderdtls.objects.filter(order_id=order.order_id)
    for ordd in orderdtl:
        ordd.delete()
    return redirect('/custhome')
    
def logout(request):
    del request.session['uid']
    return redirect('/')

def fishsale(request):
    catt = tbl_category.objects.all()
    cat=tbl_category.objects.get(cat_name='Fish')
    catid=cat.cat_id
    prod=tbl_product.objects.filter(cat_id=catid)
    return render(request,'publicviewprods.html',{'pd':prod,'ca':catt})

def viewcustinfo(request,id):
    cust= tbl_customer.objects.get(cust_id=id)
    return render(request,'viewcustinfo.html',{'cu':cust})

    







