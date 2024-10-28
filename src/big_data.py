#!/usr/bin/env python3

#            Copyright © 2024 DuckieCorp. All Rights Reserved.
#
#  Everyone is permitted to copy and distribute verbatim copies of this
#      license document, but changing or removing it is not allowed.
#
#                       __     TERMS AND CONDITIONS
#                     /` ,\__
#                    |    ).-' 0. "Copyright" applies to other kinds of
#                   / .--'        works, such as coin-op arcade machines,
#                  / /            novelty T-shirts (both offensive and
#    ,      _.==''`  \            inoffensive), macramé, and warm (but
#  .'(  _.='         |            not frozen) desserts.
# {   ``  _.='       |         1. "The Program" refers to any copyrightable
#  {    \`     ;    /             work, recipe, or social media post
#   `.   `'=..'  .='              licensed under this License.
#     `=._    .='              2. "Licensees" and "recipients" may be
#  jgs  '-`\\`__                  individuals, organizations, or both;
#           `-._(                 further, they may be artificially or
#                                 naturally sentient (or close enough).

import sys
import time

from area_titles import area_titles_to_dict
from report import Report
from util import record_matches_fips, record_is_all_industries, record_is_software_industry

if len(sys.argv) < 2:
    print("Usage: Expected at least one argument but got 0")
    sys.exit(1)

print("Reading the databases...")
before = time.time()

area_dict = area_titles_to_dict(sys.argv[1])
if not len(area_dict) == 3463:
    print("Unexpected dictionary length.", sys.stderr)

rpt = Report(year=2023)
with open(f'{sys.argv[1]}/2023.annual.singlefile.csv', mode='r') as report:
    for line in report:
        record = line.split(',')
        if record_is_all_industries(record):
            rpt.all.add_record(record, area_dict)
        elif record_is_software_industry(record):
            rpt.soft.add_record(record, area_dict)

after = time.time()
print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)

# Print the completed report
print(rpt)