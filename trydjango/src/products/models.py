from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120) #max_length is required
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(max_digits=1000 ,decimal_places=2)
    summary     = models.TextField(blank=False, null=False)
    featured    = models.BooleanField(default=True) #I can set null=True default=True

    def get_absolute_url(self):
        # return (f"/productdetail/{self.id}/") This was a standard way
        return reverse("productDetail", kwargs={"my_id": self.id})
    
    def get_deleteing_url(self):
        # return (f"/productdelete/{self.id}") I just did same here
        return reverse("productdelete", kwargs={"my_id": self.id})

