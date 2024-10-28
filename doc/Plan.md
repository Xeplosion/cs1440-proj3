# Software Development Plan

Phase 0: Requirements Analysis (tag name `analyzed`)
----------------------------------------------------

Working to create a program to summarize data from the Bureau of the Division of Labor Statistics. The data to be processed is in .csv files.
The program needs to be reasonably fast. To test its speed you can use the benchmark tool as time is relative to your system.
The solution should EXACTLY match the output.txt files in each data directory. The report should include correct factual data.
I already know how to process data from .csv files using Python.
I think that processing all of the data in a fast way might be somewhat challenging.
The data used by this program comes from the Bureau of the Division of Labor Statistics. There are several data sets of various sizes in the
form of .csv files.
The programs output should be printed in the console using STDOUT. The output should match the provided examples exactly.


Phase 1: Design (tag name `designed`)
-------------------------------------

### util.py

record_matches_fips(record, areas):
    fip = record index of fip
    return areas contains fip

record_is_all_industries(record):
    extract industry and ownership codes from record
    check if they match the code that indicates all industries or all ownership types

record_is_software_industry(record):
    extract industry type code and return True if software company

get_fips(record):
    returns the index of the QCEW containing the FIP code

get_estabs(record):
    returns the index of the QCEW containing the establishment counts

get emplvl(record):
    returns the index of the QCEW containing the employment levels

get_wages(record):
    get the index for all 4 quarters wages
    returns the sum of these 4 numbers
    
### area_titles.py

area_titles_to_dict(dirname)
    load dirname + area-title.csv
    for each line in area-title add new dictionary fip / name key pair

### industry_data.py

__init__():
    initialize the necessary values in the constructor.

add_record(self, record, areas):
    increment processed areas
    find annual wages, establishments, and employment levels for the current record
    if any of these are larger (and not equal) to the existing maximums replace that data


Phase 2: Implementation (tag name `implemented`)
------------------------------------------------

The record parameter for the add_record method was not formatted the way that I expected. I had to cast it to an int.
The index for the QCEW data in the provided CSV files was not the same as described in the bls.gov website.
I wasn't paying close enough attention to realize that the area_titles had to sort out certain unwanted regions.
I ended up creating a separate method is_valid_fips to excluded unwanted and duplicate FIP areas.

I went back and changed the industry_data.py file to use the methods defined in util.py.
It was somewhat annoying trying to figure out what ownership and industry codes were the software and all industries in the QWEC records.
Again these codes did not match the bls.gov website :/

Filled out the big_data.py file. Was pretty straightforward and all went as planned.

Phase 3: Testing and Debugging (tag name `tested`)
--------------------------------------------------

Ran python src/big_data.py > test_output.txt then confirmed that the test_output.txt file matched the provided output.txt file.
Repeated the above step on several other files to ensure consistency.
Passed all unit tests after running.

Phase 4: Deploying (tag name `deployed`)
-----------------------------------------

Checked for the correct repository URL.
Made sure all the tags got pushed to gitlab.
Project structure is correct and matches that of the existing repository.
Validated that the correct code was in the gitlab repository.
Cloned and reran the code to make sure it still worked.
Ran the project in the command line to test the console output.
Added final touches to documentation.

Phase 5: Maintenance
--------------------

I think for the most part my code was well written and easy to understand.
However, I could have probably done a better job commenting the big_data.py file and the documentation is somewhat lacking and confusing.

If a bug was reported in a few months I think I would need around an hour or so to fix it.
The first 45 minutes would be spent relearning the code, then 15 minutes to find and identify the issue.
Of course, it all depends on what the issue is.

I think that adding a new feature should be pretty easy. Since the outline was created before I even started the project and seems pretty sound.
Most of what I coded was really low level and honestly doesn't really effect the project structure much.

Theoretically it should still run regardless of my computers hardware and operating system. All of the code written only uses python and has nothing to do
with the hardware or OS. Any langauge update has the potential to break code and since I'm not a developer for Python I couldn't say for sure whether or not
and update to Python would break this code.