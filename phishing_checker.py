# This script analyzes email content to detect potential phishing attempts.
def check_link_for_keywords(link):
    keywords = ["login", "verify", "update", "secure"]
    for word in keywords:
        if word in link.lower():
            return True
    return False

# Function to check for urgent phrases in the email content
def contains_urgent_phrases(text):
    phrases = ["urgent", "immediately", "verify your account", "limited time"]
    for phrase in phrases:
        if phrase in text.lower():
            return True
    return False

def sender_is_suspicious(email):
    return not email.lower().endswith("@gmail.com")

def analyze_email(subject, body, sender, links):
    points = 0
    reasons = []

    if contains_urgent_phrases(subject + " " + body):
        points += 1
        reasons.append("Includes urgent language")

    if sender_is_suspicious(sender):
        points += 1
        reasons.append("Sender address looks suspicious")

    # Check links for suspicious keywords
    bad_links = [link for link in links if check_link_for_keywords(link)]
    if bad_links:
        points += 1
        reasons.append("Contains suspicious links")

    if points >= 2:
        return "Phishing", reasons
    elif points == 1:
        return "Suspicious", reasons
    else:
        return "Safe", []
