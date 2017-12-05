'''
Created on 17 Nov 2017

@author: Ruwan Perera
'''
import twitter
#try:
 #    import jason
#except ImportError:
#    import simplejson as json
    
api = twitter.Api(consumer_key='6DQAErJBT7i9NOysBwQIjSPTH',
                      consumer_secret='B6yMjlOJSE6OBlm9JLQC1w4q7G18bpvn94y4e076ZiDUDSXc6r',
                      access_token_key='849391373958688768-7xMmUPRhlwM20BZ7sAo69MslHFMzNWc',
                      access_token_secret='RrMulWbyPa5yc5OH3uEkrRk10QCHgXnXDNIkVP6k2E1GQ')
print(api.VerifyCredentials())
user_profile = api.VerifyCredentials()
print(user_profile)

# Get your own friend list authenticated abov
users = api.GetFriends()
print([u.name for u in users])

# Get a anonymous users friend list
username = "Andypiper"
query = api.GetFriends(screen_name=username)
print(len(query["ids"]))

#print user_profile['created_at']
#for line in user_profile:
#GET https://api.twitter.com/1.1/followers/ids.json?cursor=-1&screen_name=andypiper&count=5000