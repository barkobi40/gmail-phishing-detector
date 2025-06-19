import re
from urllib.parse import urlparse

def check_link_for_keywords(link):
    # Checks if a link contains common phishing keywords.
    keywords = ["login", "verify", "update", "secure", "account", "password", "reset", "billing", "suspicious", "pay", "payment", "invoice", "bank", "credit", "alert", "security"]
    for word in keywords:
        if word in link.lower():
            return True
    return False

def contains_urgent_phrases(text):
    # Checks if email content contains urgent or common phishing phrases.
    phrases = [
        "urgent", "immediately", "verify your account", "limited time",
        "action required", "account suspended", "security alert",
        "unusual activity", "click here", "update your information",
        "prize", "won", "winner", "congratulations", "claim now", "free money",
        "confidential", "secret", "private", "access now", "expire", "deactivated"
    ]
    for phrase in phrases:
        if phrase in text.lower():
            return True
    return False

def is_shortened_url(url):
    # Checks if the URL is a common shortened link.
    shortened_domains = [
        "bit.ly", "tinyurl.com", "ow.ly", "goo.gl", "t.co", "rebrand.ly", "cutt.ly", "rb.gy"
    ]
    try:
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname
        if hostname:
            hostname = hostname.lower()
            if hostname.startswith('www.'):
                hostname = hostname[4:]
            return hostname in shortened_domains
    except ValueError:
        pass # Not a valid URL
    return False

def analyze_email(subject, body, sender, links, is_sender_trusted=False):
    # Analyzes email content for potential phishing attempts.
    result = "Safe"
    reasons = []
    phishing_score = 0

    # Extract sender's domain
    sender_email_match = re.search(r"@([^>]+)", sender)
    sender_domain = None
    if sender_email_match:
        sender_domain = sender_email_match.group(1).lower().strip()
        if ':' in sender_domain:
            sender_domain = sender_domain.split(':')[0]

    # Rule 1: Urgent or suspicious language
    if contains_urgent_phrases(subject + " " + body):
        reasons.append("Urgent or suspicious language detected")
        phishing_score += 2

    # Rule 2: Unusual sender address (not @gmail.com and not explicitly trusted)
    is_sender_unusual = not sender.lower().endswith("@gmail.com") and not is_sender_trusted
    # This rule doesn't add points directly; trusted sender impact is handled in final classification.

    # Rule 3: Check links for suspicious keywords and domain mismatches
    for url in links:
        if check_link_for_keywords(url):
            reasons.append(f"Link contains suspicious keywords: {url}")
            phishing_score += 2
        
        if sender_domain:
            try:
                parsed_url = urlparse(url)
                url_hostname = parsed_url.hostname
                if url_hostname:
                    url_hostname = url_hostname.lower()
                    if url_hostname.startswith('www.'):
                        url_hostname = url_hostname[4:]

                    if url_hostname != sender_domain:
                        reasons.append(f"Domain mismatch in link: {url_hostname} is not {sender_domain} ({url})")
                        phishing_score += 3
            except ValueError:
                # Log invalid URL, but continue scanning
                print(f"Invalid URL found: {url}")

        if is_shortened_url(url):
            reasons.append(f"Shortened URL detected: {url}")
            phishing_score += 1

    # Determine final result based on phishing score and trusted sender status
    if is_sender_trusted:
        if phishing_score >= 3:
            result = "Phishing (from trusted sender, but critical issues found)"
        elif phishing_score >= 1:
            result = "Suspicious (from trusted sender, but other issues found)"
        else:
            result = "Safe (Sender trusted)"
    else:
        if phishing_score >= 3:
            result = "Phishing"
        elif phishing_score >= 1:
            result = "Suspicious"
        else:
            result = "Safe"

    # Add 'Unusual sender address' reason only if the email is not 'Safe'
    if is_sender_unusual and result != "Safe" and \
       "Unusual sender address (not from Gmail and not marked as trusted)" not in reasons:
        reasons.insert(0, "Unusual sender address (not from Gmail and not marked as trusted)") # Add to beginning for prominence

    return result, reasons
