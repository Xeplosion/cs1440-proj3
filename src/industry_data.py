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

from util import *


class IndustryData:
    """
    Contains statistics for a single industry.
    """
    def __init__(self):
        # Study the instructions and the unit tests to discover
        # the names and types of the attributes
        self.num_areas = None
        self.num_areas = 0
        self.total_annual_wages = 0
        self.max_annual_wages = ["", 0]
        self.total_estabs = 0
        self.max_estabs = ["", 0]
        self.total_emplvl = 0
        self.max_emplvl = ["", 0]

    def add_record(self, record, areas):
        """
        Adds a record's data to the summary statistics.

        This method does not need to validate its input;
        'record' should already be validated beforehand.

        Parameters:
         - record: A record containing employment and wage data.
         - areas: A dictionary mapping FIPS area codes to human-friendly area titles.

        This method updates the following summary statistics:
         - Adds one to the total number of areas processed.
         - Calculates and accumulates the total annual wages.
         - Keeps track of the area with the maximum annual wages.
         - Calculates and accumulates the total number of establishments.
         - Keeps track of the area with the maximum number of establishments.
         - Calculates and accumulates the total employment level.
         - Keeps track of the area with the maximum employment level.
        """
        # Not a valid area
        if not get_fips(record) in areas:
            return

        # Increment areas processed
        self.num_areas += 1

        area = areas[get_fips(record)]

        # Wages
        total_wages = int(float(record[10]))
        self.total_annual_wages += total_wages
        if total_wages > self.max_annual_wages[1]:
            self.max_annual_wages = [area, total_wages]

        # Establishments
        total_estabs = get_estabs(record)
        self.total_estabs += total_estabs
        if total_estabs > self.max_estabs[1]:
            self.max_estabs = [area, total_estabs]

        # Employment levels
        total_emplvl = get_emplvl(record)
        self.total_emplvl += total_emplvl
        if total_emplvl > self.max_emplvl[1]:
            self.max_emplvl = [area, total_emplvl]
