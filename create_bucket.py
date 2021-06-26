from google.cloud import storage

client = storage.Client()
str_name = "YOUR_BUCKET_NAME"
# Set properties on a plain resource object.
bucket = storage.Bucket(str_name)
bucket.name = str_name
bucket.location = "us-central1"
bucket.storage_class = "STANDARD"
bucket = client.create_bucket(bucket)