import json
import datetime

def lambda_handler(event, context):
    timestamp = datetime.datetime.now().isoformat()
    
    print(f"Function executed at: {timestamp}")
    print("DONE")
    
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": "Hello from Python Lambda!",
            "timestamp": timestamp,
            "event": event
        })
    }
