#command line utility

# cloud storage bucket metadata
gcloud storage buckets describe gs://<bucket_name> --format=json

#cloud vm
gcloud compute instances describe <instance_name> --zone=<zone> --format=json

#cloud storage object
gcloud storage objects describe gs://<bucket>/<object> --format=json