from aqvify import (AqvifyAPI, DeviceDataAPI)
import requests_mock

MOCK_DEVICE_DATA_RESPONSE = {
    "dateTime": "2023-08-04T21:13:14+00:00",
    "waterLevel": -10.566849,
    "meterValue": 19.433151,
    "status": None
}

def test_get_latest_value():
    with requests_mock.Mocker() as mock_request:
        base_url = "https://public.aqvify.com"
        device_key = "AQ01337"
        mock_request.get(
            f"{base_url}/api/v1/DeviceData/LatestValue",
            json=MOCK_DEVICE_DATA_RESPONSE,
            status_code=200,
            request_headers={"x-api-key": "secret-api-token"}
        )

        api = AqvifyAPI(base_url, "secret-api-token")

        device_data_api = DeviceDataAPI(api)

        latest_value_data = device_data_api.get_latest_value(device_key)

        assert latest_value_data == MOCK_DEVICE_DATA_RESPONSE
