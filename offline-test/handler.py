import json

import numpy as np
import pandas as pd


def hello(event, context):
    body = {
        "message": f'{pd.date_range("20130101", periods=6)}',
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
