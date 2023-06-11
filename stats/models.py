from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Action(models.Model):
    ACTION_TYPES = (
        ('visit', 'Visit'),
        ('purchase', 'Purchase'),
    )

    action_id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField()
    user_id = models.IntegerField()
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=10, choices=ACTION_TYPES)
    page_id = models.IntegerField(null=True)
    purchased_items = models.TextField(null=True)

