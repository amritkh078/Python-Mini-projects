# To download datasets directly into your notebook without needing to download locally

# First create your api token from kaggle, upload it to the notebook directory( a json file)

# We use opendatasets library to download dataset 

import opendatasets as od
dataset_url = 'url of the dataset you want to download'
od.download(dataset_url)