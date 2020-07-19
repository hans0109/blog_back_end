from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=255, verbose_name="用户名", blank=True, null=True)
    password = models.CharField(max_length=255, verbose_name="密码", blank=True, null=True)
    email = models.EmailField(verbose_name="邮箱")

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'apps_user'
        ordering = ["username"]
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name
