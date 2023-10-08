from django.db import models

class ErrorCode(models.Model):
    error_code = models.CharField(max_length=20, unique=True)
    error_name = models.CharField(max_length=255)
    error_first = models.CharField(max_length=255, blank=True, null=True)
    error_second = models.CharField(max_length=255, blank=True, null=True)
    error_third = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.error_name


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_image = models.ImageField(upload_to='products/images/')
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_vendor = models.CharField(max_length=255)

    error_code = models.ForeignKey(
        ErrorCode,
        on_delete=models.CASCADE,
        related_name='products',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.product_name