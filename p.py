import django
import os
import json
from InstagramAPI import InstagramAPI
import random
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "instaman.settings")
django.setup()

from account.models import Account

def getFollowersSet(api,ids):
    m = set()
    #print(ids)
    for k in ids:
        #print(k)
        x = api.getTotalFollowers(k)
        for i in random.sample(x, 1000):
            m.add(i['pk'])

    x = api.getTotalSelfFollowers()
    for i in x:
        m.add(i['pk'])

    x = api.getTotalSelfFollowings()
    for i in x:
        m.add(i['pk'])

    return m



for acc in Account.objects.all():

    api = InstagramAPI(acc.username, acc.password)
    api.login()
    pth = "images/"+acc.username+'/'
    if ( (acc.timer%acc.postsPerDay == 0) and os.listdir(pth) ):
        photo_path = str(pth+random.choice(os.listdir(pth))) #change dir name to whatever
        api.uploadPhoto(photo_path, caption=acc.photoDescription)
        os.remove(photo_path)



    if (acc.timer%24 == 0):
        jsTarget = json.loads(acc.target)
        targetAccs = list()
        for l in jsTarget:
            targetAccs.append(jsTarget[l])
        target = getFollowersSet(api,targetAccs)
        fpd = acc.followPerDay
        for x, tg in zip(range(fpd), target):
            api.follow(tg)
    api.logout()
