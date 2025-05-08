import re
import nltk
from nltk.tokenize import word_tokenize

# If running for the first time, uncomment the following line to download NLTK resources
# nltk.download('punkt')

def analyze_email(subject, body):
    """
    Simple rule-based phishing detection:
    - Checks for phishing keywords in the subject and body.
    - Uses regex to detect URLs and flags suspicious ones.
    Returns a phishing score between 0 and 100.
    """
    phishing_keywords = ["urgent", "verify", "update", "click", "compromised", "account"]
    score = 0

    # Combine subject and body for analysis
    content = f"{subject} {body}".lower()
    tokens = word_tokenize(content)

    # Increase score for each phishing keyword found
    for keyword in phishing_keywords:
        if keyword in tokens:
            score += 20

    # Check for suspicious URLs (example: URLs not from known domains)
    urls = re.findall(r'http[s]?://\S+', content)
    for url in urls:
        if "phishy-link" in url or "fake-update" in url:
            score += 30

    # Cap the score at 100
    return min(score, 100)

if __name__ == '__main__':
    # Example test
    test_subject = "Urgent: Verify Your Account"
    test_body = "Click the link: http://phishy-link.com to update your information."
    score = analyze_email(test_subject, test_body)
    print("Phishing Score:", score)
