import json
import boto3
import os


def lambda_handler(event, context):
    """Respond To Auth Challenge
    
    """
    print(event, "-------Start------------")
    challenge = event.get('challenge')
    username = event.get('username')
    session = event.get('session')
    answer = event.get('answer')
    
    response = cognito_client.respond_to_auth_challenge(
        ClientId=client_id,
        ChallengeName=challenge,
        Session=session,    
        ChallengeResponses='CUSTOM_CHALLENGE',
    )

    return response
