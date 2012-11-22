from django.db import models

class Figurina(models.Model):
	numero = models.CharField(max_length = 3)

	def __unicode__(self):
		return self.numero

class Persona(models.Model):
	nome = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.nome

class Scambio(models.Model):
	CELOMANCA = (('M', 'M'), ('D', 'D'))
	figurina = models.ForeignKey(Figurina)
	celo = models.CharField(max_length = 3, choices = CELOMANCA)
	persona = models.ForeignKey(Persona)

	def __unicode__(self):
		return self.celo
