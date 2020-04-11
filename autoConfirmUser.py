import json

def lambda_handler(event, context):
    """Auto Confirm User
    
    """
    
    event.get('response').update({
        'autoConfirmUser': True
        })
    
    
    return event
