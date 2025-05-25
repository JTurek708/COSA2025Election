"""
San Antonio Mayoral Election
=============================

This script cleans and processes the raw election CSV data, focusing on 
the mayoral race between Rolando Pablos and Gina Ortiz Jones.

Usage:
    python parse_election.py

Output:
    - cleaned_sa_election_data.csv: Clean election results by precinct
    - Console output with basic analysis
"""

import pandas as pd
import numpy as np
from pathlib import Path
import sys
