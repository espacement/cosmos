from django.db import models
from users.models import User


# участки
class plots(models.Model):
    price = models.DecimalField(default=0, max_digits=7, decimal_places=2, verbose_name="Цена")
    size = models.CharField(max_length=50)
    image = models.ImageField(upload_to='assets', blank=True, null=True, verbose_name="Изображение")
    
    class Meta:
        db_table = "plot"
        verbose_name = "Участок"
        verbose_name_plural = "Участки"


# корзина
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def get_total_cost(self):
        return sum(item.plot.price * item.quantity for item in self.cartitem_set.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    plot = models.ForeignKey(plots, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.plot.size} ({self.quantity})'
    

# заказы
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
    class Meta:
        db_table = "order"
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    plot = models.ForeignKey(plots, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    

    def __str__(self):
        return f"{self.quantity} of {self.plot.size}"
    class Meta:
        db_table = "order_item"
        verbose_name = "Товар в заказе"
        verbose_name_plural = "Товары в заказе"