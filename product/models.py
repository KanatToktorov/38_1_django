'''
models.py - это файл, в котором мы будем создавать наши модели.

ORM - Object-Relational Mapping (Объектно-реляционное отображение)
это программная технология, которая связывает базы данных с 
концепциями объектно-ориентированных языков программирования, 
создавая "виртуальную объектную базу данных". 
Это позволяет программистам работать с базами данных, 
используя объектно-ориентированный подход, а не язык SQL.

CREATE TABLE product_product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) DEFAULT NULL,
    description TEXT,
    price FLOAT,
    created_at DATETIME,
    updated_at DATETIME
);
'''

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField("Картинка", upload_to='product_images/%Y/%m/%d/', null=True, blank=True)
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    tags = models.ManyToManyField(
        Tag,
        related_name='products',
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        default=None,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.price}"

class Meta:
    db_table = 'product'
    verbose_name = 'Продукт'
    verbose_name_plural = 'Продукты'
    ordering = ['-created_at']

class Review(models.Model):
    product = models.ForeignKey(
        Product, # К какой модели относится
        on_delete=models.CASCADE, # Что делать с комментарием, если пост удален
        related_name='reviews' # default: review_set. Позволяет обращаться к отзывам через product.reviews
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.title} - {self.text}"