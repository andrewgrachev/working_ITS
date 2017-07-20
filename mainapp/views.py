from django.shortcuts import render
from django.http import JsonResponse
from mainapp.models import Installs
from mainapp.models import crashes


class DailyInstalls(object):
    def Insta(self):
        res = []
        for i in Installs.objects.filter(DailyDeviceUninstalls=5).all():
            installs_i = {
                'id': i.ID,
                'Date': i.Date,
                'AppVersionCode': i.AppVersionCode,
                'CurrentDeviceInstalls': i.CurrentDeviceInstalls,
                'DailyDeviceInstalls': i.DailyDeviceInstalls,
                'DailyDeviceUninstalls': i.DailyDeviceUninstalls,
                'DailyDeviceUpgrades': i.DailyDeviceUpgrades,
                'CurrentUserInstalls': i.CurrentUserInstalls,
                'TotalUserInstalls': i.TotalUserInstalls,
                'DailyUserInstalls': i.DailyUserInstalls,
                'DailyUserUninstalls': i.DailyUserUninstalls
            }

            res.append(installs_i)
        return JsonResponse(res, safe=False)


class DailyCrashes(object):
    def Crash(self):
        res = []
        for n in crashes.objects.filter().all():
            crashes_n = {
                'id': n.ID,
                'DailyCrashes': n.DailyCrashes,
                'Date': n.Date,
                'AppVersionCode': n.AppVersionCode,
                'DailyANRs': n.DailyANRs
            }

            res.append(crashes_n)
        return JsonResponse(res, safe=False)
