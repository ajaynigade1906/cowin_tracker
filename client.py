
from .call_api import CallApi
from .parser import Parser

url = "https://cdn-api.co-vin.in/api/v2"
states_url = f"{url}/admin/location/states"
districts_url = f"{url}/admin/location/districts"

parser = Parser()

class ClientAPI(CallApi):

    def get_states(self):
        final_url = states_url
        return self._api_call(final_url)

    def get_districts(self, state_id: str):
        final_url = f"{districts_url}/{state_id}"
        return self._api_call(final_url)

    def get_availability_by_district_id(self, district_id, date, min_age_limt):
        return parser.get_availability('district', district_id,
                                             date=date, min_age_limt=min_age_limt)

    def get_availability_by_pincode(self, pin_code,
                                    date: str = Parser.today(),
                                    min_age_limt: int = None):
        return parser.get_availability('pincode', pin_code,
                                             date=date, min_age_limt=min_age_limt)
                                             
    def get_availability_by_district_name(self, district_name,
                                     date: str = Parser.today(),
                                     min_age_limt: int = None):
        return parser.get_availability_by_name('district', district_name.lower(),
                                             date=date, min_age_limt=min_age_limt)