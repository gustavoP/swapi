import BaseAPI

class PeopleAPI:
    __endpoint = 'people'

    def get_people_festest_vehicle(self):
        """
        Return a non sorted dictionary with the keys 'person', 'vehicle' and 'speed' and a list with the values.
        Return a dictionary with empty list in caso there is no result.

        """

        people_dict = {'person':[], 'vehicle':[], 'speed':[]}

        url = BaseAPI.get_api_root()+self.__endpoint
        response = BaseAPI.return_api_json(url)

        while True: #for each page

            characters = response['results']

            for character in characters:
                vehicle = self.get_festest_vehicle(character['vehicles'])
                if vehicle:
                    people_dict['person'].append(character['name'])
                    people_dict['vehicle'].append(vehicle['vehicle'])
                    people_dict['speed'].append(vehicle['speed'])
     
            next_page = response['next']

            if next_page == None:
                break
            
            response = BaseAPI.return_api_json(next_page)

        return people_dict




    def get_festest_vehicle(self,vehicle_url_list):
        """
        vehicle_url_list is a list of vehicle urls. \n
        Return a dictionary with keys = 'vehicle' and 'speed'. \n
        Return empty dictionary is vehicle_url_list is a empty list. \n
        raise exception if vehicle_url_list is not a list.
        """
        if not isinstance(vehicle_url_list,list):
            raise Exception('vehicle_url_list should be a list')

        fastest = {}

        for vehicle_url in vehicle_url_list:
            vehicle = BaseAPI.return_api_json(vehicle_url)

            if not fastest:
                fastest['vehicle'] = vehicle['name']
                fastest['speed'] = vehicle['max_atmosphering_speed']
            else:
                if vehicle['max_atmosphering_speed'] > fastest['speed']:
                    fastest['vehicle'] = vehicle['name']
                    fastest['speed'] = float(vehicle['max_atmosphering_speed'])
        return fastest
            
