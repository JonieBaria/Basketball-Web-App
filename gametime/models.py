from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Player(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True, blank=True)
	age = models.CharField(max_length=200, null=True, blank=True)
	profile_pic = models.ImageField(null=True, blank=True)
	height = models.CharField(max_length=200, null=True, blank=True)
	phone = models.CharField(max_length=200, null=True, blank=True)
	email = models.CharField(max_length=200, null=True, blank=True)




	
	def __str__(self):
		return str(self.name)



class Schedule(models.Model):
	COURTS = (
		('Eastwood Ph1', 'Eastwood Ph1'),
		('Eastwood Ph2', 'Eastwood Ph2'),
		('Diliman', 'Diliman'),
		('Eastwind', 'Eastwind'),
		('Centella', 'Centella'),

		)

	TIME = (
		('5:00PM-6:00PM', '5:00PM-6:00PM'),
		('6:00PM-7:00PM', '6:00PM-7:00PM'),
		('7:00PM-8:00PM', '7:00PM-8:00PM'),
		('8:00PM-9:00PM', '8:00PM-9:00PM'),

		)


	court = models.CharField(max_length=200, null=True,blank=True, choices=COURTS)
	schedule = models.CharField(max_length=200, null=True, blank=True, choices=TIME)
	statman = models.CharField(max_length=200, blank=True, null=True)
	price = models.FloatField(null=True, blank=True,)
	date = models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return f"{self.court} ({self.date}) ({self.schedule}) "


class Tag(models.Model):
	payment = models.CharField(max_length=200, null=True, blank=True,)
	
	def __str__(self):
		return str(self.payment)



class Booking(models.Model):

	STATUS = (
		('waiting for players...', 'waiting for players...'),
		('Complete Players', 'Complete Players'),
		('Rescheduled', 'Rescheduled'),
		('Now Playing', 'Now Playing'),
		('Game Ended', 'Game Ended'),

		)
 
	
	player = models.ForeignKey(Player, null=True, blank=True, on_delete= models.SET_NULL)
	schedule = models.ForeignKey(Schedule, null=True,blank=True, on_delete= models.SET_NULL)
	date_booked = models.DateTimeField(auto_now_add=True, blank=True)
	status= models.CharField(max_length=200, null=True, blank=True, choices=STATUS)
	payment = models.ForeignKey(Tag, null=True, blank=True, on_delete= models.SET_NULL)


	def __str__(self):
 		return str(self.player)



# class Gametime(models.Model):

# 	book = models.ForeignKey(Player, null=True, on_delete= models.SET_NULL)

# class Games(models.Model):

# 	book = models.ForeignKey(Booking, null=True, on_delete= models.SET_NULL)
# 	teamplayers = models.CharField(max_length=200, blank=True, null=True)
# 	score = models.IntegerField(max_length=200, null=True, blank=True)
# 	gameresult = models.CharField(max_length=200, blank=True, null=True)


# class Gametime(models.Model):

# 	book = models.ForeignKey(Player, null=True, on_delete= models.SET_NULL)




