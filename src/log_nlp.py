import spacy

nlp = spacy.load("en_core_web_sm")

def describe_http_event(row):
    return f"HTTP {row['method']} to {row['host']} at URI {row['uri']}"

# Can add more like conn.log, dns.log...
