import getpass
from arcgis.gis import *

password = getpass.getpass("Please enter password: ")
dev_gis = GIS('https://www.arcgis.com', 'username', password)
print("Successfully logged in to {} as {}".format(dev_gis.properties.urlKey + '.' + dev_gis.properties.customBaseUrl,
                                                 dev_gis.users.me.username))