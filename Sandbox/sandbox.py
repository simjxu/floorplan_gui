#!/usr/bin/env python3

import yaml

with open("./Sandbox/example.yaml", "r") as stream:
    try:
        print(yaml.safe_load(stream))
    except yaml.YAMLError as exc:
        print(exc)