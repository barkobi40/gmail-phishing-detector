from email_utils import parse_email
from phishing_checker import analyze_email

# Example phishing email
sample_phishing_email = {
    "subject": "URGENT: Verify your account NOW! Action required!",
    "body": '''
        <p>Dear Customer, your account has been suspended due to suspicious activity. 
        Please <a href="http://login.bad-site.com/verify">click here to verify</a> immediately.</p>
        <p>You have also won a prize! Claim it here: <a href="http://bit.ly/prize-claim">bit.ly/prize-claim</a></p>
    ''',
    "sender": "support@bank-alerts.biz"
}

# Example legitimate Gmail email
sample_gmail_email = {
    "subject": "Nitzan's Passport",
    "body": '''
        <p>This is your updated passport file.</p>
        <p>Thank you for completing the request.</p>
    ''',
    "sender": "nitzanaw80@gmail.com"
}

# Example legitimate non-Gmail email (not trusted)
sample_legit_non_gmail_email = {
    "subject": "Meeting Update",
    "body": '''
        <p>Hello, attached is an update regarding the scheduled meeting.</p>
        <p>Regards, The Office</p>
    ''',
    "sender": "office@mycompany.com"
}


def run_example(email_dict, is_trusted=False, label=""):
    print(f"--- Analyzing {label} ---")
    subject, body, sender, links = parse_email(email_dict)
    result, reasons = analyze_email(subject, body, sender, links, is_sender_trusted=is_trusted)
    print("Classification:", result)
    print("Reasons:")
    for r in reasons:
        print("-", r)
    print("\n")


if __name__ == "__main__":
    run_example(sample_phishing_email, is_trusted=False, label="example phishing email")
    run_example(sample_gmail_email, is_trusted=False, label="example Gmail email")
    run_example(sample_legit_non_gmail_email, is_trusted=False, label="legit non-Gmail email (not trusted)")
    run_example(sample_legit_non_gmail_email, is_trusted=True, label="legit non-Gmail email (trusted sender)")
