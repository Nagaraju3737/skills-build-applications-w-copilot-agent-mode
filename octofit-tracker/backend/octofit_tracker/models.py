from djongo import models


class User(models.Model):
    _id = models.ObjectIdField()
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    class Meta:
        app_label = 'octofit_tracker'

    def __str__(self):
        return self.username


class Activity(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=100)
    duration = models.FloatField(help_text='Duration in minutes')
    date = models.DateField()

    class Meta:
        app_label = 'octofit_tracker'

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} on {self.date}"


class Team(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField(User, related_name='teams', blank=True)

    class Meta:
        app_label = 'octofit_tracker'

    def __str__(self):
        return self.name


class Leaderboard(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries')
    score = models.FloatField(default=0)

    class Meta:
        app_label = 'octofit_tracker'
        ordering = ['-score']

    def __str__(self):
        return f"{self.user.username}: {self.score}"


class Workout(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.FloatField(help_text='Duration in minutes')

    class Meta:
        app_label = 'octofit_tracker'

    def __str__(self):
        return self.name
