from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    Q = [
        (1, '나의 보물 1호는?'),
        (2, '나의 고향은?'),
        (3, '붕어빵 먹을 때 가장 먼저 먹는 부위는?'),
        (4, '나의 MBTI는?'),
        (5, '돌잡이 때 잡은 것은?')
    ]

    def __str__(self):
        return self.username

    u_id = models.IntegerField(unique=True, null=True)
    username = models.CharField(max_length=20, null=True)
    phone = models.CharField(default="010", max_length=11)
    answer = models.CharField(max_length=200, blank=True)
    question_id = models.IntegerField(default=1, choices=Q)
    USERNAME_FIELD = 'u_id'
    REQUIRED_FIELDS = ['username']

class Menu(models.Model):
    def __str__(self):
        return self.m_name

    C = [
        (1, '도서,필기구'),
        (2, '생활용품'),
        (3, '식료품'),
        (4, '욕실용품'),
        (5, '주방용품'),
        (6, '침구류')
    ]
    
    c_id = models.IntegerField(default=1, choices=C)

    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_id')
    m_name = models.CharField(max_length=200)
    m_info = models.TextField()
    m_price = models.IntegerField()
    m_img = models.ImageField(blank=True, upload_to="images/", null=True)
    m_takeout = models.BooleanField(default=False) # 사장님이 포장가능여부 표시

class Basket(models.Model):
    ototal_price = models.IntegerField()
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='selected_menu')
    takeout = models.BooleanField(default=False)    # 소비자가 포장할지 안할지 선택
    count = models.IntegerField()

class Pay(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user')
    date = models.DateTimeField()
    total = models.IntegerField()
    order_num = models.IntegerField()
    orders = models.ManyToManyField('Order', blank=True)

class Order(models.Model):
    def __str__(self):
        return str(self.or_num)

    or_name = models.CharField(max_length=200)
    or_num = models.IntegerField()
    or_count = models.IntegerField()
    or_takeout = models.BooleanField(default=False)
    