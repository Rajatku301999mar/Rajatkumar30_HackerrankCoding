#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter, OrderedDict



class OrderedCounter(Counter):
    pass

[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]
