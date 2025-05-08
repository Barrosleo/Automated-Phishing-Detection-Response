from detection_engine import analyze_email
from incident_correlation import correlate_incidents
from response_mitigation import mitigate_response
from report_generator import generate_incident_report
import pandas as pd
import os

def main():
    # Ensure necessary directories exist
    os.makedirs("data", exist_ok=True)
    os.makedirs("docs", exist_ok=True)

    # Load simulated email data
    emails = pd.read_csv("data/sample_emails.csv")
    print("Loaded emails:", len(emails), "records")

    # 1. Detect phishing in each email using the Detection Engine
    emails['phishing_score'] = emails.apply(lambda row: analyze_email(row['subject'], row['body']), axis=1)
    print("Detection complete.")

    # 2. Incident Correlation: Correlate and filter suspicious emails (e.g., score above a threshold)
    suspicious_emails = correlate_incidents(emails)
    print("Suspicious emails identified:", len(suspicious_emails))

    # 3. Automated Response & Mitigation
    responses = mitigate_response(suspicious_emails)
    print("Response actions taken:", responses)

    # 4. Generate Incident Report
    report = generate_incident_report(suspicious_emails, responses)
    with open("docs/incident_report.json", "w") as f:
        f.write(report)
    print("Incident report generated at docs/incident_report.json")

if __name__ == '__main__':
    main()
