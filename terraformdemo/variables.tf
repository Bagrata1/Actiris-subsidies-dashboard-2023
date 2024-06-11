variable "location" {
    description = "Location"
    default = "europe-west1"
}


variable "bq_dataset_name" {
    description = "My BigQuery Dataset Name"
    default = "demo_dataset"
}

variable "gcs_storage_class" {
    description = "Bucket Storage Class"
    default = "STANDARD"
}

variable "gcs_bucket_name" {
    description = "My Storage Bucket Name"
    default = "terraform-demo-424211-terra-bucket"
}

variable "project" {
    description = "Project"
    default = "terraform-demo-424211"
}

variable "region" {
    description = "Project region"
    default = "europe-west1"
}

variable "credentials" {
    description = "Google Credentials path"
    default = "./keys/my-creds.json"
}