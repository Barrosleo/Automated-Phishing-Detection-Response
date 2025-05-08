import json
from datetime import datetime

def generate_incident_report(suspicious_emails, responses):
    """
    Generate a JSON report including:
    - Timestamp of report generation.
    - Total number of suspicious emails.
    - List of each suspicious email with its response actions.
    """
    report_data = {
        "report_generated": datetime.now().isoformat(),
        "total_suspicious_emails": int(len(suspicious_emails)),
        "details": []
    }
    
    for index, row in suspicious_emails.iterrows():
        email_id = row.get('email_id', 'unknown')
        detail = {
            "email_id": email_id,
            "subject": row.get('subject', ''),
            "phishing_score": row.get('phishing_score'),
            "response": responses.get(email_id, {})
        }
        report_data["details"].append(detail)
    
    return json.dumps(report_data, indent=4)

if __name__ == '__main__':
    # Sample test: create a dummy report
    import pandas as pd
    sample_df = pd.DataFrame({
        'email_id': [1, 3],
        'subject': ["Urgent: Verify", "Action Required: Update"],
        'phishing_score': [80, 70]
    })
    sample_responses = {
        1: {"action": "Isolate account", "alert": "Security notified"},
        3: {"action": "Isolate account", "alert": "Security notified"}
    }
    report = generate_incident_report(sample_df, sample_responses)
    print(report)
