#!/usr/bin/env python3

import os
import requests

"""
Example JSON
{"name": "Watermelon", "weight": 500,
 "description": "Watermelon is good for relieving heat, eliminating annoyance and quenching thirst. It contains a lot of water, which is good for relieving the symptoms of acute fever immediately. The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation. Watermelon also contains substances that can lower blood pressure.",
 "image_name": "010.jpeg"}

Iterate over all the fruits and use post method from Python requests library 
to upload all the data to the URL http://[external-IP-address]/fruits
"""