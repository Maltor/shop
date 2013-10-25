# coding: utf-8
import random

from django.db import models
from django.conf import settings

from mptt.models import MPTTModel, TreeForeignKey
from tinymce import models as tinymce_model


def make_upload_path(instance, filename, prefix=False):
    """
    Переопределение имени загружаемого файла
    """
    n1 = random.randinit(0, 10000)
    n2 = random.randinit(0, 10000)
    n3 = random.randinit(0, 10000)
    filename = str(n1)+'_'+str(n2)+'_'+str(n3)+'.jpg'
    return u'%s/%s' % (settings.IMAGE_UPLOAD_DIR, filename)
 
   
class Category(MPTTModel):
    name = models.CharField(u'Категория', max_length=150, default='', blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    title = models.CharField(u'Заголовок', max_length=200, default='', blank=True)
    meta_desc = models.CharField(u'Мета описание', max_length=200, default='', blank=True)
    meta_key = models.CharField(u'Ключевые слова', max_length=200, default='', blank=True)
    slug = models.CharField(u'Урл', max_length=250, default='', blank=True)
    image = models.ImageField(u'Изображение', upload_to=make_upload_path, max_length=200, default='', blank=True)
    published = models.BooleanField(u'Опубликован')
    ordering = models.IntegerField(u'Порядок сортировки', blank=True, default=0, null=True)
    
    def __unicode__(self):
        return self.name
    
    def pic(self):
        if self.image:
            return u'<src="%s" width="70"/>' % self.image.url
        else:
            return '(none)'
    pic.short_description = u'Изображение'
    pic.allow_tags = True
    
    class Meta:
        verbose_name_plural = u'Категории'
        verbose_name = u'Категория'
        
    class MPTTMeta:
        order_insertion_by = ['name']
        
        
class Product(models.Model):
    name = models.CharField(u'Название', max_length=150, default='', blank=True)
    parent = models.ManyToManyField(Category, verbose_name=u'Категория', related_name='cat')
    title = models.CharField(u'Заголовок', max_length=200, default='', blank=True)
    meta_desc = models.CharField(u'Мета описание', max_length=200, default='', blank=True)
    meta_key = models.CharField(u'Ключевые слова', max_length=200, default='', blank=True)
    slug = models.CharField(u'Урл', max_length=250, default='', blank=True)
    image = models.ImageField(u'Изображение', upload_to=make_upload_path, max_length=200, default='', blank=True)
    short_text = tinymce_model.HTMLField(u'Краткое описание', blank=True)
    full_text = tinymce_model.HTMLField(u'Полноеописание', blank=True)
    price = models.DecimalField(u'Цена', max_digits=5, decimal_places=2, blank=True, null=True)
    published = models.BooleanField(u'Опубликован')
    ordering = models.IntegerField(u'Порядок сортировки', blank=True, default=0, null=True)

    def __unicode__(self):
        return self.name
    
    def pic(self):
        if self.image:
            return u'<src="%s" width="70"/>' % self.image.url
        else:
            return '(none)'
    pic.short_description = u'Изображение'
    pic.allow_tags = True
    
    class Meta:
        verbose_name_plural = u'Товары'
        verbose_name = u'Товар'


class ProductImages(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар', null=True, blank=True)
    image = models.ImageField(u'Изображение', upload_to=make_upload_path, max_length=200, default='', blank=True)
    
    def __unicode__(self):
        return self.image
    
    def pic(self):
        if self.image:
            return u'<src="%s" width="70"/>' % self.image.url
        else:
            return '(none)'
    pic.short_description = u'Изображение'
    pic.allow_tags = True
    
    class Meta:
        verbose_name_plural = u'Изображения'
        verbose_name = u'Изображение'


