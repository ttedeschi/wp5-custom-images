#!/bin/bash

/usr/bin/tini -s /opt/conda/bin/python3.12 -- /usr/local/bin/jupyterhub-singleuser "$@" --debug & python3 /opt/conda/lib/python3.12/site-packages/dask_labextension/refresh-manifest.py
