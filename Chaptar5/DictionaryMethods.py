profile = {
    "username": "Kunal Thakur",
    "details": {
        "followers": 1200,
        "verified": True
    }
}

# to get all the keys of dictionary

print(profile.keys())  # (['username', 'details'])

# to get all the values of dictionary
print(profile.values())# (['Kunal Thakur', {'followers': 1200, 'verified': True}])
print(profile["details"].values()) # ([1200, True])

# to get all the items of dictionary

print(profile.items()) #([('username', 'Kunal Thakur'), ('details', {'followers': 1200, 'verified': True})])

#  to get single key 
print(profile.get("username")) # Kunal Thakur

# update value

print(profile.update({"username": "Kunal",}))


print(profile) #{'username': 'Kunal', 'details': {'followers': 1200, 'verified': True}}