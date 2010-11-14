from BeautifulSoup import BeautifulSoup
import urllib2, re

#gets the list of shows
shows = ["late_night_with_conan_obrien", "tonight_show_with_jay_leno",  ]



#Gets the number of likes for a show
for show in shows:
	page = urllib2.urlopen("http://getglue.com/tv_shows/" + show)
	soup = BeautifulSoup(page)
	print show.replace("_", " ") + ": " + soup.find('span', {'class':'likes count'}).string
	
	 