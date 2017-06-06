import whois
import requests
from datetime import datetime, timedelta
from urllib.parse import urlparse
import argparse


def load_urls4check(path, min_days_for_expiration):
    delta_expiration = timedelta(days=min_days_for_expiration)
    parsed_url = urlparse(path)
    return {
        'URL': path,
        'IS 200 OK': is_server_respond_with_200(path),
        'IS NOT EXPIRED FOR MONTH': get_domain_expiration_date(parsed_url.hostname) - datetime.now() > delta_expiration,
    }


def is_server_respond_with_200(url):
    return requests.get(url).status_code == 200


def get_domain_expiration_date(domain_name):
    expiration_date = whois.whois(domain_name).expiration_date
    if isinstance(expiration_date, list):
        return expiration_date[0]
    else:
        return expiration_date


def get_args():
    parser = argparse.ArgumentParser(description='Check site health')
    parser.add_argument('input', type=str, help='path where to find list of urls')
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    for line in open(args.input):
        url = line.strip()
        if not url:
            continue
        print(load_urls4check(url, 30))
