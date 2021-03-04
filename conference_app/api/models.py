from django.db import models

# Create your models here.
class User(models.Model):
    """docstring foruser_property."""
    user_id=models.IntegerField(primary_key=True,unique=True)
    username=models.CharField(max_length=264,unique=True)

    class Meta:
        db_table = 'user'

class Rooms(models.Model):
    """docstring for Rooms."""
    room_id=models.CharField(max_length=8,unique=True)
    link=models.CharField(max_length=264,default='no_link')
    owner=models.ForeignKey(User,on_delete=models.CASCADE,default=0)

    class Meta:
        db_table = 'room'
class RoomProperty(models.Model):
    """docstring foruser_property."""
    rp_id=models.IntegerField(primary_key=True,unique=True)
    rp_rid=models.ForeignKey(Rooms,on_delete=models.CASCADE)
    room_key=models.CharField(max_length=264)
    value=models.CharField(max_length=264)

    class Meta:
        db_table = 'room_property'


class UserProperty(models.Model):
    """docstring for User_property."""
    up_id=models.IntegerField(primary_key=True,unique=True)
    up_uid=models.ForeignKey(User,on_delete=models.CASCADE)
    user_key=models.CharField(max_length=264)
    value=models.CharField(max_length=264)

    class Meta:
        db_table = 'user_property'
