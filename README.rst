Squirrel Tracker
================

By: Project Group 32 | Members: Shijia Zhang, Xiaohang He | UNIs: sz2868, xh2441 | From Tools for Analytics section 1

.. contents::

Project description
-------------------

The project get the 2018 Central Park Squirrel Census data and can keep track of all the known squirrels on the map.

A command could be used to import the data into the project:: $ python manage.py import_squirrel_data /path/to/file.csv
The 2018 Central Park Squirrel Census data has already been imported into the project.
A command could be used to export the data out of the project:: 
$ python manage.py export_squirrel_data /path/to/file.csv

A file named exportfile.csv has been exported out of the project.

The project has several features:

- A view that shows a map that displays the location of the squirrel sightings on an map. Located at: /map
- A view that lists all squirrel sightings with link to edit each. Located at: /sightings
- A view to update a particular sighting. Located at: /sightings/<unique_squirrel_id>
- A view to create a new sighting. Located at: /sightings/add
- A view with general stats about the sightings. We analyze the number of "True", the number of "False", the percenatge of "True" of five fields: Running, Chasing, Climbing, Eating and Foraging. Located at: /sightings/stats

Group Information
-----------------

Project Group 32, Tools for Analytics Section 1

Members: Shijia Zhang, Xiaohang He

UNIs: [sz2868, xh2441]

Links to the project
--------------------

- Link to the repository for the project source code: https://github.com/Shijia-Zhang/project
- Public git clone URL: https://github.com/Shijia-Zhang/project.git
- Link to the server running the application: https://profound-jet-259601.appspot.com/
