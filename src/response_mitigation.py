def mitigate_response(suspicious_emails):
    """
    Simulate automated response actions for detected phishing attempts.
    For each suspicious email, simulate isolating the affected account and alerting security.
    Returns a dictionary mapping email_id to simulated response actions.
    """
    responses = {}
    for index, row in suspicious_emails.iterrows():
        email_id = row.get('email_id', 'unknown')
        responses[email_id] = {
            "action": "Isolate account",
            "alert": "Security notified",
            "details": f"Email with phishing score {row.get('phishing_score')}"
        }
    return responses

if __name__ == '__main__':
    # Sample test output
    import pandas as pd
    sample_df = pd.DataFrame({
        'email_id': [1, 3],
        'phishing_score': [80, 70]
    })
    actions = mitigate_response(sample_df)
    print(actions)
