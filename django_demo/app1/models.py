from django.db import models

# Create your models here.
class CreateUpdate(models.Model):  # 创建抽象数据模型，同样要继承于models.Model
    # 创建时间，使用models.DataTimeField
    created_at = models.DateTimeField(auto_now_add=True)
    # 修改时间，使用models.DateTimeField
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:  # 元数据，除了字段意外的所有属性
        # 设置model为抽象类。指定该表不应该在数据库中创建
        abstract = True

class Person(CreateUpdate):  # 继承CreateUpdate基类
    """
    编写Person模型类，数据模型应该继承于models.Model或其子类
    """
    # 第一个字段使用models.CharField类型
    first_name = models.CharField(max_length=30)
    # 第二个字段使用models.CharField类型
    last_name = models.CharField(max_length=30)

class Order(CreateUpdate):  # 继承CreateUpdate基类
    """
    编写Order模型类，数据模型应该继承于models.Model或其子类
    """
    order_id = models.CharField(max_length=30, db_index=True)
    order_desc = models.CharField(max_length=30)

