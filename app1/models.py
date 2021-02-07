from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class tbl_login(models.Model):
    user_id = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    category = models.CharField(max_length=30)

    class Meta:
        db_table = "tbl_login"

class tbl_staff(models.Model):
    staff_id = models.CharField(max_length=30)
    staff_name = models.CharField(max_length=30)
    staff_address = models.CharField(max_length=100)
    join_date = models.CharField(max_length=30)
    staff_phno = models.BigIntegerField()
    staff_email = models.CharField(max_length=50)
    id_type = models.CharField(max_length=30)
    id_num = models.CharField(max_length=30)
    staff_status = models.CharField(max_length=30)

    class Meta:
        db_table = "tbl_staff"









class tbl_category(models.Model):
    cat_id = models.CharField(max_length=30)
    cat_name = models.CharField(max_length=30)
    cat_desc = models.CharField(max_length=100)
    cat_img = models.CharField(max_length=300)

    class Meta:
        db_table="tbl_category"



class tbl_product(models.Model):
    prod_id = models.CharField(max_length=30)
    cat_id = models.CharField(max_length=30)
    prod_name = models.CharField(max_length=30)
    prod_desc = models.CharField(max_length=100)
    prod_unit = models.CharField(max_length=30)
    prod_price = models.FloatField()
    prod_img = models.CharField(max_length=300)
    prod_stkqty = models.FloatField()
    prod_rol = models.FloatField()
    prod_status = models.CharField(max_length=30)

    class Meta:
        db_table="tbl_product"


    

class tbl_customer(models.Model):
    cust_id = models.CharField(max_length=30)
    cust_name = models.CharField(max_length=30)
    cust_address = models.CharField(max_length=100)
    cust_phno = models.BigIntegerField()
    cust_email = models.CharField(max_length=50)

    class Meta:
        db_table="tbl_customer"

class tbl_review(models.Model):
    rev_id = models.CharField(max_length=30)
    prod_id = models.CharField(max_length=30)
    cust_id = models.CharField(max_length=30)
    cust_name = models.CharField(max_length=30)
    review = models.CharField(max_length=500)


    class Meta:
        db_table="tbl_review"

class tbl_cart(models.Model):
    cart_id = models.CharField(max_length=30)
    cust_id = models.CharField(max_length=30)
    prod_id = models.CharField(max_length=30)
    prod_name = models.CharField(max_length=30)
    order_qty = models.FloatField()
    prod_price = models.FloatField()

    class Meta:
        db_table="tbl_cart"



class tbl_order(models.Model):
    order_id = models.CharField(max_length=30)
    order_dt = models.DateField()
    order_amt = models.FloatField()
    order_paymode = models.CharField(max_length=30)
    cust_id = models.CharField(max_length=30)
    order_status = models.CharField(max_length=30)

    class Meta:
        db_table="tbl_order"


class tbl_orderdtls(models.Model):
    orderdtls_id = models.CharField(max_length=30)
    order_id = models.CharField(max_length=30)
    prod_id = models.CharField(max_length=30)
    prod_name = models.CharField(max_length=30)
    order_qty = models.FloatField()
    prod_amt = models.FloatField()
    order_status = models.CharField(max_length=30)

    class Meta:
        db_table="tbl_orderdtls"
        


class tbl_delvrydtls(models.Model):
    delvry_id = models.CharField(max_length=30)
    order_id = models.CharField(max_length=30)
    delvry_dt = models.CharField(max_length=30)
    courier_name = models.CharField(max_length=30)
    delvry_remark = models.CharField(max_length=30)

    class Meta:
        db_table="tbl_delvrydtls"




class tbl_idgen(models.Model):
    stfid=models.IntegerField()
    ctyid=models.IntegerField()
    pdtid=models.IntegerField()
    ctrid=models.IntegerField()
    ctid=models.IntegerField()
    odrid=models.IntegerField()
    odtlsid=models.IntegerField()
    dvryid=models.IntegerField()
    revwid=models.IntegerField()
    comid=models.IntegerField()
    podrid=models.IntegerField()
    pmntid=models.IntegerField()
    retrnid=models.IntegerField()

    class Meta:
        db_table="tbl_idgen"

class tbl_complaint(models.Model):
    comp_id=models.CharField(max_length=30)
    cust_id=models.CharField(max_length=30)
    cust_name=models.CharField(max_length=30)
    prod_id=models.CharField(max_length=30)
    complaint=models.CharField(max_length=500)
    comp_date=models.CharField(max_length=30)
    class Meta:
        db_table="tbl_compalint"

class tbl_purchaseorder(models.Model):
    porder_id=models.CharField(max_length=30)
    prod_id=models.CharField(max_length=30)
    prod_name=models.CharField(max_length=30)
    req_qty=models.FloatField()
    porder_dt=models.DateField()
    class Meta:
        db_table="tbl_purchaseorder"

class tbl_payment(models.Model):
    payment_id=models.CharField(max_length=30)
    order_id=models.CharField(max_length=30)
    cust_id=models.CharField(max_length=30)
    payment_amt=models.FloatField()
    bank_name=models.CharField(max_length=30)
    ifsc_code=models.CharField(max_length=50)
    acc_no=models.CharField(max_length=30)
    payment_dt=models.DateTimeField()
    payment_status=models.CharField(max_length=30)
    class Meta:
        db_table="tbl_payment"

class tbl_return(models.Model):
    return_id=models.CharField(max_length=30)
    cust_id=models.CharField(max_length=30)
    order_id=models.CharField(max_length=30)
    order_amt=models.FloatField()
    return_status=models.CharField(max_length=30)
    class Meta:
        db_table="tbl_return"


