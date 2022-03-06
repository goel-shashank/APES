import os
from . import config

def load_domains(domain_dir_path: str = os.path.join(config.root, "data", "domains")):
    domains = {}
    for domain_file_name in os.listdir(domain_dir_path):
        domain_file_path = os.path.join(domain_dir_path, domain_file_name)
        with open(domain_file_path, "r") as domain_file:
            domains[os.path.splitext(domain_file_name)[0]] = list(map(lambda x: {"name": x.split(",")[0].strip(), "class": x.split(",")[1].strip()}, domain_file.readlines()))
    return domains