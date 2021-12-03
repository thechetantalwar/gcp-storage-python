- Creating Cloud Storage Bucket programatically
    * Prereq.
        * Your VM should have service associated with access to your Cloud Storage service.
    * Steps
        * Install python package manager
        
            ```
            apt-get update
            apt-get install python-pip
            ```
        * Install the cloud storage library

            ```pip install google-cloud-storage```
        * Get the code
            
            ```
            git clone https://github.com/thechetantalwar/gcp-storage-python
            cd gcp-storage-python
            ```
        * Update the storage bucket name in the create_bucket.py file
            
            ```vi create_bucket.py```
        * Once done, just execute the code
            
            ```python3 create_bucket.py```
        * Now, if you go to Google Cloud Console, you will see your new bucket over there
