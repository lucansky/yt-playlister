import pafy

playlist = pafy.get_playlist(input("Enter playlist URL: "))

for video in playlist["items"]:
	print video["pafy"].title, "\n"
	video["pafy"].getbestaudio().download()
