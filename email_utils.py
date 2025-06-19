# llibrary that helps extract links and elements from email HTML content
from bs4 import BeautifulSoup


def get_links_from_html(html):
    soup = BeautifulSoup(html, "html.parser")
    links = []

    for a in soup.find_all('a', href=True):
        links.append(a['href'])

    return links

# Email parsing and link extraction
def parse_email(email_data):
    subject = email_data.get("subject", "")
    body = email_data.get("body", "")
    sender = email_data.get("sender", "")

    links = get_links_from_html(body)

    return subject, body, sender, links
