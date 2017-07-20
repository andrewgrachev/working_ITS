from django.db import models


class Installs(models.Model):
    ID = models.IntegerField(primary_key=True)
    Date = models.TextField()
    PackageName = models.TextField()
    AppVersionCode = models.IntegerField()
    CurrentDeviceInstalls = models.IntegerField()
    DailyDeviceInstalls = models.IntegerField()
    DailyDeviceUninstalls = models.IntegerField()
    DailyDeviceUpgrades = models.IntegerField()
    CurrentUserInstalls = models.IntegerField()
    TotalUserInstalls = models.IntegerField()
    DailyUserInstalls = models.IntegerField()
    DailyUserUninstalls = models.IntegerField()


class crashes(models.Model):
    ID = models.IntegerField(primary_key=True)
    Date = models.TextField()
    PackageName = models.TextField()
    AppVersionCode = models.IntegerField()
    DailyCrashes = models.IntegerField()
    DailyANRs = models.IntegerField()
