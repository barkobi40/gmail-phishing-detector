from email_utils import parse_email
from phishing_checker import analyze_email

sample_email = {
    "subject": "URGENT: Verify your account now!",
    "body": '<p>Please <a href="http://login-phish.com">click here</a> to login.</p>',
    "sender": "support@notgmail.biz"
}

subject, body, sender, links = parse_email(sample_email)
result, reasons = analyze_email(subject, body, sender, links)

print("Classification:", result)
print("Reasons:")
for r in reasons:
    print("-", r)
