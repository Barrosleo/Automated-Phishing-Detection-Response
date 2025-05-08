import pandas as pd

def correlate_incidents(emails_df, threshold=50):
    """
    Correlate incidents by filtering out emails with a phishing score above the threshold.
    In a real-world scenario, additional correlation based on sender patterns or metadata could be added.
    """
    suspicious = emails_df[emails_df['phishing_score'] >= threshold].copy()
    return suspicious

if __name__ == '__main__':
    # Test with a sample dataframe
    df = pd.DataFrame({
        'email_id': [1, 2, 3],
        'phishing_score': [80, 10, 70]
    })
    correlated = correlate_incidents(df)
    print(correlated)
