from django.db import models

# candidates = [('one', 'one'), ('two', 'two'), ('three', 'three'),
# ('four', 'four'), ('five', 'five'), ('six', 'six'), ('seven', 'seven'), ('eight', 'eight'), ('nine', 'nine')]


class User(models.Model):
    firstname = models.CharField(max_length=15)
    secondname = models.CharField(max_length=15)
    thirdname = models.CharField(max_length=15, blank=True, null=True)
    birth_date = models.DateField()                                   
    date_created = models.DateTimeField(auto_now_add=True)
    identification = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.firstname} {self.secondname}'


class Vote(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # voted_candidate = models.CharField(max_length=10,choices=candidates,default='one')
    voted_candidate = models.IntegerField()
    voted_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.firstname} {self.user.secondname} {self.voted_candidate}'

