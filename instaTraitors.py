from LevPasha.InstagramAPI import InstagramAPI

USERNAME = ""
PASSWORD = ""
followers  = []
followings = []
api = InstagramAPI(USERNAME, PASSWORD)

def read_from_file(file):
	arr = []
	with open(file, "r") as f:
		arr = f.read().splitlines()
	return arr

def main():
	api.login()
	
	followers_temp  = read_from_file("followers.txt")
	open("followers.txt", 'w').close()
	followings_temp = read_from_file("followings.txt")
	open("followings.txt", 'w').close()
	
	f_followers  = open("followers.txt", 'w')	
	for i in api.getTotalSelfFollowers():
		followers.append(i.get("username"))
		f_followers.write(str(i.get("username"))+'\n')
	f_followers.close()
	
	f_followings = open("followings.txt", 'w')
	for i in api.getTotalSelfFollowings():
		followings.append(i.get("username"))
		f_followings.write(str(i.get("username"))+'\n')
	f_followings.close()

	traitors = set(followings)-set(followers)
	print(len(traitors)," traitors found!")
	for t in traitors:
		print(t)
	
	print("\nFollowers -> OLD: " + str(len(followers_temp)) + ", NEW: " + str(len(followers)))
	if len(followers_temp) > len(followers):
		change = set(followers_temp)-set(followers)
	else:
		change = set(followers)-set(followers_temp)
	print("Followers Changes: ")
	for c in change:
		print(str(c))

	print("\nFollowings -> OLD: " + str(len(followings_temp)) + ", NEW: " + str(len(followings)))
	if len(followings_temp) > len(followings):
		change = set(followings_temp)-set(followings)
	else:
		change = set(followings)-set(followings_temp)
	print("Followings Changes: ")
	for c in change:
		print(str(c))

	
if __name__ == "__main__":
    main()
	