from email_utils import parse_email
from phishing_checker import analyze_email

# Example phishing email
sample_phishing_email = {
    "subject": "URGENT: Verify your account NOW! Action required!",
    "body": '<p>Dear Customer, your account has been suspended due to suspicious activity. Please <a href="http://login.bad-site.com/verify">click here to verify</a> immediately.</p><p>You have also won a prize! Claim it here: <a href="http://bit.ly/prize-claim">bit.ly/prize-claim</a></p>',
    "sender": "support@bank-alerts.biz"
}

# Example legitimate Gmail email
sample_gmail_email = {
    "subject": "Nitzan's Passport",
    "body": '<p>This is your updated passport file.</p><p>Thank you for completing the request.</p>',
    "sender": "nitzanaw80@gmail.com"
}

# Example legitimate non-Gmail email (not marked as trusted)
sample_legit_non_gmail_email = {
    "subject": "Meeting Update",
    "body": '<p>Hello, attached is an update regarding the scheduled meeting.</p><p>Regards, The Office</p>',
    "sender": "office@mycompany.com"
}

# example phishing email ---
print("--- Analyzing example phishing email ---")
subject_p, body_p, sender_p, links_p = parse_email(sample_phishing_email)
# Assume this sender is not trusted (False)
result_p, reasons_p = analyze_email(subject_p, body_p, sender_p, links_p, is_sender_trusted=False)
print("Classification:", result_p)
print("Reasons:")
for r in reasons_p:
    print("-", r)
print("\n")

#example Gmail email ---
print("--- Analyzing example Gmail email ---")
subject_g, body_g, sender_g, links_g = parse_email(sample_gmail_email)
# Gmail sender is usually not 'Unusual sender', and even if so, assume not yet explicitly trusted
result_g, reasons_g = analyze_email(subject_g, body_g, sender_g, links_g, is_sender_trusted=False)
print("Classification:", result_g)
print("Reasons:")
for r in reasons_g:
    print("-", r)
print("\n")

# example legitimate non-Gmail email (not marked as trusted) ---
print("--- Analyzing example legitimate non-Gmail email (not marked as trusted) ---")
subject_n, body_n, sender_n, links_n = parse_email(sample_legit_non_gmail_email)
# Non-Gmail sender, not marked as trusted
result_n, reasons_n = analyze_email(subject_n, body_n, sender_n, links_n, is_sender_trusted=False)
print("Classification:", result_n)
print("Reasons:")
for r in reasons_n:
    print("-", r)
print("\n")

# example legitimate non-Gmail email (marked as trusted) ---
print("--- Analyzing example legitimate non-Gmail email (marked as trusted) ---")
# Assume office@mycompany.com is marked as trusted
result_t, reasons_t = analyze_email(subject_n, body_n, sender_n, links_n, is_sender_trusted=True)
print("Classification:", result_t)
print("Reasons:")
for r in reasons_t:
    print("-", r)
print("\n")
