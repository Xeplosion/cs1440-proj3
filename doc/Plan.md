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
*(15% of your effort)*

**Finally, you can write code!**

Deliver:

*   [ ] Working code in the `src/` folder.
*   [ ] Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. what you learned, what didn't go according to plan.
*   [ ] **Tag** the last commit in this phase `implemented` and push it to GitLab.

The record parameter for the add_record method was not formatted the way that I expected. I had to cast it to an int.
The index for the QCEW data in the provided CSV files was not the same as described in the bls.gov website.
I wasn't paying close enough attention to realize that the area_titles had to sort out certain unwanted regions.
I ended up creating a separate method is_valid_fips to excluded unwanted and duplicate FIP areas.

I went back and changed the industry_data.py file to use the methods defined in util.py.

Phase 3: Testing and Debugging (tag name `tested`)
--------------------------------------------------
*(30% of your effort)*

Your grade depends on how your program performs when run from the command line.  We don't use PyCharm to grade, so ensure your program runs correctly from the shell.

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    *   Write your test cases in plain language such that a non-coder could run them and replicate your experience.
    *   Include a description of what happened for *each test case*.
    *   For any bugs discovered, describe their cause and remedy.
*   [ ] **Tag** the last commit in this phase `tested` and push it to GitLab.


Phase 4: Deployment (tag name `deployed`)

-----------------------------------------
*(5% of your effort)*

Deliver:

*   [ ] **Tag** the last commit in this phase `deployed` and push it to GitLab.
*   [ ] Your repository is pushed to GitLab.
*   [ ] **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Look for all of the tags in the **Tags** tab.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   [ ] **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


Phase 5: Maintenance
--------------------

Spend a few minutes writing thoughtful answers to these questions.  They are meant to make you think about the long-term consequences of choices you made in this project.

Deliver:

*   [ ] Write brief and honest answers to these questions:
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   [ ] Make one final commit and push your **completed** Software Development Plan to GitLab.
*   [ ] Respond to the **Project Reflection Survey** on Canvas.
