

import csv

from google.cloud import storage


def list_public_urls(bucket_name, output_csv):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blobs = list(bucket.list_blobs())

    with open(output_csv, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Object Name", "Public URL"])

        for blob in blobs:
            public_url = f"https://storage.googleapis.com/{bucket_name}/{blob.name}"
            csv_writer.writerow([blob.name, public_url])

if __name__ == "__main__":
    bucket_name = "meta_ads_creatives"
    output_csv = "public_urls.csv"

    list_public_urls(bucket_name, output_csv)
