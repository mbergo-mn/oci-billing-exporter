# tests/test_send_billing_to_s3.py

import json
import pytest
from unittest.mock import Mock
from send_billing_to_s3_directory import send_billing_to_s3  # Replace with the actual path to your send_billing_to_s3.py

def test_handler():
    # Mock the context and the data to be passed to the handler
    ctx = Mock()
    data = Mock()
    data.getvalue.return_value = json.dumps({"name": "OCI User"})

    # Call the handler
    resp = send_billing_to_s3.handler(ctx, data)
    
    # Convert the response data into a Python dictionary
    resp_data = json.loads(resp.body())

    # Check if the response data contains the expected values
    assert resp_data['message'] == "Hello OCI User"
    assert resp.status == "200 OK"

