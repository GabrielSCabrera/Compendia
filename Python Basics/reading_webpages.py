'''We can extract data from webpages as follows:'''
import urllib
url = 'http://www.metoffice.gov.uk/climate/uk/stationdata/oxforddata.txt'

webpage = urllib.urlopen(url)
webstring = webpage.readlines()
webpage.close()

'''We can also save the HTML data from the site directly to a file:'''

urllib.urlretrieve(url, filename='webpage.html')

'''We will delete the file for neatness'''

import os
os.remove('webpage.html')
