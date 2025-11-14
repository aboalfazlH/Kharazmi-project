from django.contrib import admin
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta


@admin.action(description="حذف خبر‌های غیرفعال و قدیمی‌تر از ۱ سال")
def delete_old_inactive_posts(modeladmin, request, queryset):
    """Delete all inactive posts older than one year."""
    one_year_ago = timezone.now() - timedelta(days=365)
    old_posts = queryset.filter(is_active=False, write_date__lt=one_year_ago)
    count = old_posts.count()
    old_posts.delete()
    modeladmin.message_user(request, f"{count} خبر قدیمی حذف شد ")

@admin.action(description="تائید کردن خبر")
def accept_post(modeladmin, request, queryset):
    count = queryset.count()
    queryset.update(is_active=True, is_verify=True)
    messages.success(request, f"{count} خبر انتخاب شده تائید شدند ")


@admin.action(description="رد کردن خبر")
def reject_post(modeladmin, request, queryset):
    count = queryset.count()
    queryset.update(is_active=False, is_verify=True)
    messages.success(request, f"{count} خبر انتخاب شده رد شدند ")


@admin.action(description="سنجاق کردن خبر")
def pin_post(modeladmin, request, queryset):
    count = queryset.count()
    queryset.update(is_active=True, is_pin=True, is_verify=True)
    messages.success(request, f"{count} خبر انتخاب شده سنجاق شدند ")

actions = (accept_post,reject_post,delete_old_inactive_posts,pin_post)