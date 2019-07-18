import pandas as pd
from PeopleAPI import PeopleAPI


topDF = pd.DataFrame(PeopleAPI().get_people_festest_vehicle())
topDF.speed = topDF.speed.astype(float)
topDF.sort_values(by='speed')

print(topDF)
print(BaseAPI.i)