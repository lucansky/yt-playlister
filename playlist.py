import pafy

from sys import version_info

py3 = version_info[0] > 2 #creates boolean value for test that Python major version > 2

if py3:
  url = input("Enter playlist URL: ")
else:
  url = raw_input("Enter playlist URL: ")


playlist = pafy.get_playlist(url)

for video in playlist["items"]:
	video["pafy"].getbestaudio().download()
	print video["pafy"].title + "               "

print "\n"
