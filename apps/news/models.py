from django.urls import reverse
from django.db import models
from django.utils import timezone
from apps.users.models import CustomUser,MainPoint
from django.utils.translation import gettext_lazy as _


def thumbnail_upload_path(instance, filename):
    now = timezone.now()
    return f"blog/posts/thumbnails/year-{now.year}/month-{now.month}/day-{now.day}/{filename}"


class Post(models.Model):
    """Post model"""
    title = models.CharField(verbose_name=_("موضوع"),max_length=110)
    thumbnail = models.ImageField(verbose_name=_("تصویر شاخص"),upload_to=thumbnail_upload_path,blank=True,null=True)
    short_description = models.CharField(verbose_name=_("توضیحات کوتاه"),max_length=110,blank=True,null=True)
    description = models.TextField(verbose_name=_("محتوا"),blank=True,null=True)
    write_date = models.DateTimeField(verbose_name=_("نوشته شده در تاریخ"),auto_now_add=True)
    update_date = models.DateTimeField(verbose_name=_("اخرین به روز رسانی"),auto_now=True) 
    author = models.ForeignKey(CustomUser,verbose_name=_("نویسنده"),on_delete=models.CASCADE,blank=True,null=True)
    is_active = models.BooleanField(verbose_name=_("فعال بودن"))
    is_pin = models.BooleanField(verbose_name=_("پین بودن"))
    is_verify = models.BooleanField(verbose_name=_("تایید شده"))
    meta_name = models.CharField(verbose_name=_("نام سئو"),blank=True,null=True)
    meta_description = models.CharField(verbose_name=_("توضیح سئو"),blank=True,null=True)
    meta_keywords = models.CharField(verbose_name=_("کلمات کلیدی"),blank=True,null=True,help_text="بین کلمات باید (,) بگذارید")
    post_mainpoint = models.ForeignKey(MainPoint,on_delete=models.CASCADE,verbose_name=_("درس مربوطه"),blank=True,null=True)

    class Meta:
        verbose_name = _("پست")
        verbose_name_plural = _("پست ها")
        ordering = ["is_pin","-write_date","update_date","title","is_active","is_verify"]

    def __str__(self):
        return f"{self.title}"
    

    def get_absolute_url(self):
        return reverse('post-detail-page', kwargs={'pk': self.pk})

