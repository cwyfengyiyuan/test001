from django.db import models


# Create your models here.

class Author(models.Model):
    gender_choices = (
        (1, '男'),
        (2, '女'),
    )
    name = models.CharField(verbose_name="姓名", max_length=12)
    gender = models.IntegerField(choices=gender_choices)
    born_date = models.DateField(verbose_name="出生日期")

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ManyToManyField(to='Author', db_constraint=False, related_name='books')
    name = models.CharField(max_length=32, verbose_name='书名')
    publish_date = models.DateField(verbose_name="出版日期")
    country = models.CharField(verbose_name="国家", max_length=24)

    @property
    def author_list(self):
        author_list = self.author.all()
        return [
            {
                'name': author.name,
                'sex': author.get_gender_display(),
                'born_date': author.born_date
            } for author in author_list]
