from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=31)
    description=models.TextField(
        null=True,blank=True
    )

    class Author(models.Model)
        name=models.CharField(max_length=63)

class Product(models.Model):
    LANGUAGE_CHOICES={
        ("EN","English"),
        ("NP","Nepali"),
    }
    name=models.CharField(max_length=127)
    isbn_number = models.CharField(max_length=127,unique=True)
    description=models.Textfield(null=True,blank=True)
    author =models.ForeignKey(
        "Author",on_delete=models.PROTECT,related_name="products"
    )
    price= models.FloatField()
    image=models.URLField(blank=True,niull=True)
    category= models.foreignKey(
    "Category", related_name="products",on_delete=models.PRODUCT
    )
    rating=models.FloatField(default=0)
    page_count= models.IntegerField()
    languagfe=models.charfield(choices=LANGUAGE_CHOICCES,max_length=2)
    published_date=models.DataField()

    class ProductCart(Models.Models)


