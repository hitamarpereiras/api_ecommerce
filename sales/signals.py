from django.db.models.signals import pre_save
from django.dispatch import receiver
from sales.models import Sale
from products.models import Product
import json


@receiver(pre_save, sender=Sale)
def update_product_stock(sender, instance, **kwargs):

    # Se não esxistir no banco ignora
    if not instance.pk:
        return
    
    try:
        old_sale = Sale.objects.get(pk=instance.pk)
    except Sale.DoesNotExist:
        return
    
    # só dispara quando status for de false para true
    if old_sale.status is False and instance.status is True:
        
        order = instance.order
        itens = order.itens

        if not itens:
            return
        
        if isinstance(itens, str):
            itens = json.loads(itens)

        if isinstance(itens, dict):
            itens = [itens]

        for item in itens:
            product_id = item.get('id')
            quantity = item.get('quantity', 0)

            try:
                product = Product.objects.get(id=product_id)
                new_stock = product.stock - quantity

                # Não deixar estoque negativo
                product.stock = max(new_stock, 0)
                product.save()

            except Product.DoesNotExist:
                continue