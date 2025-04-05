from django.db import models

import catalog.models


class Blogs(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Заголовок",
        help_text="Введите заголок статьи",
    )
    contents = models.TextField(verbose_name="Содержимое", help_text="Введите ваш тект публикации")
    preview = models.ImageField(
        upload_to="blogs/photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_activ = models.BooleanField(default=True, verbose_name="Признак публикации", help_text="Признак публикации")
    count_views = models.IntegerField(blank=True, null=True, verbose_name="Количество просмотров", help_text="Количество просмотров")
    product = models.ForeignKey(
        catalog.models.Product, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Продукт"
    )

    def __str__(self):
        return f"{self.title} {self.contents}"

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
        ordering = ["title", "created_at"]
