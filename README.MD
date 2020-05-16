##Pharmacy search tool
The project was started to imporve the searching of resources. At my hospital, we have a search tool that finds reources clinicians need inorder to undertake their work. Clinicians often have to know the route and links to click to find a specific resource, or be able to search for that tool exactly how it is spelt on the system. This wastes a lot of time searching for resources, removing important time needed spent looking after patients. 

This project aims to build a search database that will allow the user to search for a resource using a key word. If they cannot find the resource under the keyword, they can access the master list and add or edit keywords to the search term. Overtime, this should mean that you can use many search terms instead of one.

##UX
The website is made for pharmacits to store and look up resources. It is built for pharmacists of multiple diciplines (paediatrics, maternity, anticoagulation, geriatrics, respiratory, cardiology, gastroenterology, surgery etc)

The tool aims to get better over time with more additions to seaarch terms allowing for resources to be searched for quicker.

As a pharmacist of a certain dicipline, I want to be able to serach for a resource that is relivant to my dicipline. 

As a junior pharmacist, I want to be able to search for pharmacy resources wihtout having knowledge of technical terminology.

As a pre registration pharmacist, I want to be able to search for pharmacy resources to appreciate evidence based guidance.

##Wireframe
Click to see the wireframe link for desktop browsers. The mobile version does not contain the PDF document to minimise screen switching.

https://drive.google.com/file/d/1fpjlTmFjG2F_fiG67_HgJ0i6IJcptLUw/view?usp=sharing

##Features
The front page is simple. It contains a navbar and a search box.

The nav bar allows for naviagtion to the homepage,about, resource list and the add a resource page.

##Existing Features
The first feature (the search bar) allows the user to serch the database using key words.

The results page shows the reults.

The "add a resource" page allows the user to fill out a form which will add to the database.

##Features Left to Implement
A login page or function could be added to ensure only those who are registered can alter the data.


##Technologies Used
The technologies used include:

[Html] The basis of the project was made using HTML

[CSS] CSS was used to add styles on top of Bootstrap

[Materialize] Materialize was used for styling.

[Vanilla Javascript] This project uses javascript to add functionally. Additionally it uses Javascript to calculate ideal body weight, body mass index, creatinine clearance (kidney function), the initial dose of vancomycin, the maintenance dose of vancomycin and the frequency of monitoring of the drug.

JQuery The project uses JQuery to simplify DOM manipulation. In this project, it was only used for the bootstrap features.

##Testing
The code was tested using jshint.com. No major issues were identified.

The tool was tested on both mobile and desktop screens.

As the aim is for the tool to be implemented in a clinical setting and for screen switching to be minimised as much as possible.

The the webpage has been tested on windows desktops. Note that it was not tested on 4k resolutions as these were not present in the hospital computers.

The webpage was tested on chrome, internet explorer and firefox.

The webpage was also tested on the following mobile devices: Huawei Mate 20 pro iPhone 7 Samsung Galaxy s8 Samsung Galaxy S10

Testing the tool:
Click the disclaimer
Fill in all the fields
Submit the form and compare the results to the guideline
Click "click to show dosing rationale" to identify how the recommendations were calculated.
Note that the guideline is intentionally hidden on mobile devices. This is to minimise screen switching.

The calendar does not appear on internet explorer.

Deployment
To run the project, simply go to https://mismiles.github.io/project-clinical-calculator/

Credits
Content
The top clickable arrow to show the guideline was adapted from http://code-chunk.com/chunks/543df4c394758/bootstrap-arrow-shaped-buttons
The code for the calendar was obtianed from https://stackoverflow.com/questions/32378590/set-date-input-fields-max-date-to-today . This was then adapted to display the minimum date (30 days prior).
The scrollby function was obtained from https://www.w3schools.com/jsref/met_win_scrollby.asp and then adapted.
Media
PDF from this document was taken from a local hospital guideline, obtained from the Whittington health intranet page
Acknowledgements
My colleague and consultant antimicrobial pharmacist Ai-Nee Lim who was pivotal in the design of the vancomycin antimicrobial guideline.
My colleague Dr Nitzan Lindenberg who took his time to aid in the initiation step of building this tool and providing constructive feedback throughout.
My colleagues Anja Ritchter, Chandini Kanderia, Dr Howell Jones, Ian Man and Patricia McCormick for testing the tool.