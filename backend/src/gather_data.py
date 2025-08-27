"""
Cleared building permits 
https://open.toronto.ca/dataset/building-permits-cleared-permits/ 
- Since 2017, refreshed daily
- 2000-2016, should be similar?
- Package ID: "building-permits-cleared-permits"

Active building permits
https://open.toronto.ca/dataset/building-permits-active-permits/
- Refreshed daily
- Package ID: "building-permits-active-permits"

Using the Toronto Open Data API
- Base URL: https://ckan0.cf.opendata.inter.prod-toronto.ca
- Datasets called "packages", each package can contaim many "resources"
- Using the package name in the page's URL will provide metadata

Libraries used
- requests: Make HTTP Get requests
- urllib: Save file
"""

import requests as req
from urllib.request import urlretrieve # can look for better libraries
from datetime import datetime

BASE_URL = "https://ckan0.cf.opendata.inter.prod-toronto.ca"

ACTIVE_PERMITS_PACKAGE = "building-permits-active-permits"
CLEARED_PERMITS_PACKAGE = "building-permits-cleared-permits" # since 2017

def retrieve_metadata(package_id):
    url = BASE_URL + "/api/3/action/package_show"
    params = {"id": package_id}

    package = req.get(url, params=params).json()

    for i, resource in enumerate(package["result"]["resources"]):

        # only get metadata for non datastore_active resources
        if resource["datastore_active"]: continue

        url = BASE_URL + "/api/3/action/resource_show?id=" + resource["id"]
        resource_metadata = req.get(url).json()

        return resource_metadata["result"] # only care about the result of the query

def download_data(url, filename):
    results = urlretrieve(url, filename)

    print(f"HTTP DETAILS:\n{results[1]}") # could print some stats on the file
    return results[0]
def import_data(packages):

    # 1. Gather the metadata and extract the download URL
    # 2. Download the data
    # 3. Return the data paths
    for package in packages:
        current_date = datetime.now().strftime("%A, %d. %B %Y")
        # check if already imported today
        if package["data_last_updated"] == str(current_date):
            print(f"{package["name"]} is already up to date")
            continue

        package_name = package["name"]
        package_data_file = package["data_file_name"]

        metadata = retrieve_metadata(package_name)
        download_url = metadata["url"]

        print(f"Downloading data from:\n\t{download_url}")
        
        data_path = download_data(download_url, package_data_file)

        # update details
        package["data_path"] = data_path
        package["data_last_updated"] = str(datetime.now().strftime("%A, %d. %B %Y"))
        
    print("Import data complete")
    return packages



