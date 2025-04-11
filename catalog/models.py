from django.db import models

import users.models


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование",
        help_text="Введите название продукта",
    )
    description = models.CharField(max_length=250, verbose_name="Описание", help_text="Введите описание продукта")
    photo = models.ImageField(
        upload_to="catalog/photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изоброжение продукта",
    )
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Категория"
    )
    price = models.IntegerField(verbose_name="Цена за покупку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")
    publish = models.BooleanField(default=False, verbose_name="Статус публикации", help_text="Статус публикации")
    owner = models.ForeignKey(
        users.models.CustomUser, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Автор продукта"
    )

    def __str__(self):
        return f"{self.name} {self.description} {self.price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
            ("can_delete_product", "Can delete product"),
        ]


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование",
        help_text="Введите название категории",
    )
    description = models.TextField(verbose_name="Описание", help_text="Опишите категорию", blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.description}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]
