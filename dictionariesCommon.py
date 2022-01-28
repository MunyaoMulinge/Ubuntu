sammy = {
    "user_name": "Sammy Shark",
    "online_status": True,
    "followers": 7584
}
jessy = {
    "user_name": "J Octopus",
    "online_status": True,
    "points": 5654
}
for common_key in sammy.keys() & jessy.keys():
    print(sammy[common_key], jessy[common_key])
