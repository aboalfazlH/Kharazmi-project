from django.db import models
from django.utils import timezone

def get_upload_path(instance,filename):
    now = timezone.now()
    return f"qa/questions/{now.year}/{now.month}/{now.day}/{instance.id}/{filename}"
    

class Question(models.Model):
    title = models.CharField(max_length=110,verbose_name="موضوع")
    photo = models.ImageField(upload_to=get_upload_path,blank=True,null=True,verbose_name="تصویر کمکی",help_text="یک تصویر میتواند به رفع مشکلتان کمک میکند")
    description = models.TextField(verbose_name="توضیحات",blank=True,null=True)
    is_pin = models.BooleanField(verbose_name="ویژه",default=False)
    is_active = models.BooleanField(verbose_name="فعال",default=True)
    is_verify = models.BooleanField(verbose_name="ویژه",default=False)
    write_date = models.DateTimeField(verbose_name="تاریخ نوشتن",auto_now_add=True)
    update_date = models.DateTimeField(verbose_name="تاریخ نوشتن",auto_now=True)
    class Meta:
        """Meta definition for Question."""

        verbose_name = 'سوال'
        verbose_name_plural = 'سوال ها'

    def __str__(self):
        return f"{self.title}"