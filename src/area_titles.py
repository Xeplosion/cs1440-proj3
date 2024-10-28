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

def is_valid_fips(fips):
    if fips.endswith("000"):
        return False
    for key in fips:
        if not key.isdigit():
            return False
    if not len(fips) == 5:
        return False
    return True


def area_titles_to_dict(dirname):
    """
    This function locates a CSV file called `area-titles.csv` in
    the specified directory, and transforms it into a dictionary
    """
    # Dictionary to store the CSV data
    area_dict = {}

    # Process the CSV data
    with open(dirname + '/area-titles.csv', mode='r') as file:
        for line in file:
            if line == 0:
                continue
            # Strip whitespace and split by comma
            parts = line.strip().split(',')

            if len(parts) >= 2:
                key = parts[0].strip('"')
                value = parts[1].strip('"')
                # Exclude certain duplicate and unwanted FIP areas
                if not is_valid_fips(key):
                    continue
                area_dict[key] = value

    return area_dict
