'''
Created on 17 Nov 2017

@author: Ruwan Perera
'''
import twitter
api = twitter.Api(consumer_key='6DQAErJBT7i9NOysBwQIjSPTH',
                      consumer_secret='B6yMjlOJSE6OBlm9JLQC1w4q7G18bpvn94y4e076ZiDUDSXc6r',
                      access_token_key='849391373958688768-7xMmUPRhlwM20BZ7sAo69MslHFMzNWc',
                      access_token_secret='RrMulWbyPa5yc5OH3uEkrRk10QCHgXnXDNIkVP6k2E1GQ')
#print(api.VerifyCredentials())
#user_profile = api.VerifyCredentials()
#print(user_profile)

# Get your own friend list authenticated above
#users = api.GetFriends()
#print([u.name for u in users])

#user = api.GetUser(screen_name = 'ruwanperera1222')
#print(user)
#print(user.id)
#print(user.name)
#user = api.GetUser(screen_name = 'saimadhup')
#print(user.id)
user = api.GetFollowers(screen_name = 'saimadhup')
#print(user)
print(user[0])
print(user[0].name)
print(user[0].id)
print(user[1].name)
print(user[1].id)
for w in user:
    if w.name == "":
        print("finish")
else:
    print(w.name, w.id)
user = api.GetUser(user_id = 937364378055196672)
print(user.name)
print(user.lang)
print(user.default_profile_image)













# Get a anonymous users friend list
#username = "Andypiper"
#queryone = api.GetFriends(screen_name=username)
#print(len(queryone["ids"]))
#querytwo = api.GetFollowers(screen_name = username, cursor=-1, count=5)

#querytwo = api.GetFollowers(user_id, screen_name, cursor, count, total_count, skip_status, include_user_entities)
#print user_profile['created_at']
#for line in user_profile:
#GET https://api.twitter.com/1.1/followers/ids.json?cursor=-1&screen_name=andypiper&count=5000