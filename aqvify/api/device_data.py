class DeviceDataAPI:
    def __init__(self, api):
        self.api = api

    def get_latest_value(self, device_key):
        endpoint = '/api/v1/DeviceData/LatestValue'
        params = {'deviceKey': device_key}
        return self.api.get(endpoint, params=params)
