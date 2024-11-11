import yaml
import random
import string
import os
from time import sleep

def generate_random_suffix(length=5):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


while(True):
    with open("/opt/conda/lib/python3.12/site-packages/dask_labextension/DaskCluster.yaml") as f:
        manifest = yaml.safe_load(f)

    random_suffix = generate_random_suffix()
    manifest["metadata"]["name"] =  "dask-" + os.environ.get("USERNAME") + "-" + random_suffix
    manifest["spec"]["scheduler"]["service"]["selector"]["dask.org/cluster-name"] = "dask-" + os.environ.get("USERNAME") + "-" + random_suffix

    with open("/opt/conda/lib/python3.12/site-packages/dask_labextension/DaskCluster.yaml", "w") as f:
        yaml.dump(manifest, f)

    sleep(10)

