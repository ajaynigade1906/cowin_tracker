# Cowin Tracker

Python API wrapper for CoWin, India's digital platform launched by the government to help citizens register themselves
for the vaccination drive by booking an appointment at the nearby vaccination centres.This wrapper is meant to enable folks to build their own versions of a system to lookup for vaccine availablity either
in a district or in a particular pin code.

Example:

```python
from CowinApi import ClientAPI

cowin = ClientAPI()

states = cowin.get_states()
print(states)
```

# Install

`pip install cowin-tracker`

# Usage

The wrapper currently covers four endpoints used by the CoWin portal specified below.

## Initialize

```python
from CowinApi import ClientAPI

cowin = ClientAPI()
```

## Get all the available states

Returns the list of states in which vaccine drive is being conducted. This also returns the `state_id` which would be
required in the subsequent requests.

```python
from cowin_api import CoWinAPI

cowin = CoWinAPI()
states = cowin.get_states()
print(states)
```


---

## Get all the available districts

Returns the list of districts in a particular states in which vaccine drive is being conducted. This also returns
the `district_id` which would be required in the subsequent requests.

In this method, you would need to pass the `state_id` retrieved from the previous method.

```python
from CowinApi import ClientAPI

cowin = ClientAPI()

state_id = '21'
districts = cowin.get_districts(state_id)
print(districts)

```



## Get all the centers available in a district

Use this method to lookup for centers based on a `district_id`. This method is broader than
searching by pin code as it covers the whole district.

In this method, you would need to pass the `district_id` retrieved from the previous methods. By default, the method
looks-up for slots with today's date. For any other dates pass the date in DD-MM-YYYY format.

```python
from CowinApi import ClientAPI

cowin = ClientAPI()

district_id = '367'
date = '12-05-2021'  # Optional. Takes today's date by default
min_age_limit = 18  # Optional. By default returns centers without filtering by min_age_limit

available_centers = cowin.get_availability_by_district_id(district_id, date, min_age_limit)
print(available_centers)
```


---

## Get all the available centers in a pin code

Use this method to lookup for centers based on a `pin_code` or a list of `pin_codes`. By default, the method looks-up
for slots with today's date. For any other dates pass the date in DD-MM-YYYY format.

```python
from CowinApi import ClientAPI

cowin = ClientAPI()

pin_code = "400080"
date = '03-05-2021'  # Optional. Default value is today's date
min_age_limit = 18  # Optional. By default returns centers without filtering by min_age_limit

available_centers = cowin.get_availability_by_pincode(pin_code, date, min_age_limit)
print(available_centers)
```

## Get all the available centers in a city name

Use this method to lookup for centers based on a `city_name`. By default, the method looks-up
for slots with today's date. For any other dates pass the date in DD-MM-YYYY format.

```python
from CowinApi import ClientAPI

cowin = ClientAPI()

city_name = "Pune"
date = '03-05-2021'  # Optional. Default value is today's date
min_age_limit = 18  # Optional. By default returns centers without filtering by min_age_limit

available_centers = cowin.get_availability_by_pincode(city_name, date, min_age_limit)
print(available_centers)
```


# Notes:

The API's of CoWin may at times return a 403 response. To mitigate this we are passing user agents in the
request. Still, if the issue persists please wait for a few minutes before trying again.




# License:

MIT License
