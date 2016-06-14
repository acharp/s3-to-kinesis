"""Parse S3 data and upload them to GA via its API."""

import

def lambda_handler(event, context):
    # Parser new-bookings data (1 csv file dumped daily dans s3 par un etl job) provenant du s3 (csv -> ? cf ga api)
    for record in event['Records']:
        # Parse the record

        # Append to ga_formatted_records

    # pusher ga_formatted_records a l'api ga


def s3_to_GA(record):

    # return GA formatted record
