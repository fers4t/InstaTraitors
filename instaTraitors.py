from LevPasha.InstagramAPI import InstagramAPI

USERNAME = ""
PASSWORD = ""
followers = []
traitors  = []
api = InstagramAPI(USERNAME, PASSWORD)

def main():
	api.login()

	for i in api.getTotalSelfFollowers():
		followers.append(i.get("username"))
	
	for i in api.getTotalSelfFollowings():
		if i.get("username") not in followers:
			traitors.append(i.get("username"))
	
	print(len(traitors)," traitors found!")
	print(traitors)
	
if __name__ == "__main__":
    main()
