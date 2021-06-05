from arcgis.gis import GIS
from datetime import datetime

# establish connection
gis = GIS(url=None, username='username', password='xxxx')

# current date and time
locale = datetime.today().strftime('%c')

# data file to upload
zip = r'C:\path_to_file\updated_shapefile.zip'

# name of item in AGOL
item_name = 'AOI polygons'

# delete content if already exists within organisation
item_search = gis.content.search(query=f"title:{item_name}", outside_org=False)
print("Items found matching search query:", len(item_search))

for i in item_search:
    try:
        i.delete()
        print("item deleted: " + str(i))
    except Exception as err:
        print(err)

# upload file to AGOL
item_prop = {'title': item_name,
             'description': 'Area of interest boundaries. This layer updated: ' + locale,
             'tags': 'gis, test'}
new_item = gis.content.add(item_properties=item_prop, data=zip)
print("zip file uploaded")

# publish item and share with organisation
layer_item = new_item.publish()
share = layer_item.share(org=True)
print(f"'{item_name}' published")
