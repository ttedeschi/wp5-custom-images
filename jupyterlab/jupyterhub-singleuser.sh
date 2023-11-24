#!/bin/bash

/usr/bin/tini -s /usr/local/bin/python3 -- /usr/local/bin/jupyterhub-singleuser "$@"
