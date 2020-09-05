##Pharmacy search tool
The project was started to imporve the searching of resources. At my hospital, we have a search tool that finds reources clinicians need inorder to undertake their work. Clinicians often have to know the route and links to click to find a specific resource, or be able to search for that tool exactly how it is spelt on the system. This wastes a lot of time searching for resources, removing important time needed spent looking after patients. 

This project aims to build a search database that will allow the user to search for a resource using a key word. If they cannot find the resource under the keyword, they can access the master list and add or edit keywords to the search term. Overtime, this should mean that you can use many search terms instead of one.

##UX
The website is made for pharmacits to store and look up resources. It is built for pharmacists of multiple diciplines (paediatrics, maternity, anticoagulation, geriatrics, respiratory, cardiology, gastroenterology, surgery etc)

The tool aims to get better over time with more additions to search terms allowing for resources to be searched for quicker.

As a pharmacist of a certain dicipline, I want to be able to serach for a resource that is relivant to my dicipline. 

As a junior pharmacist, I want to be able to search for pharmacy resources wihtout having knowledge of technical terminology.

As a pre registration pharmacist, I want to be able to search for pharmacy resources to appreciate evidence based guidance.

##Wireframe
Click to see the wireframe link for desktop browsers. The mobile version does not contain the PDF document to minimise screen switching.

https://drive.google.com/file/d/1fpjlTmFjG2F_fiG67_HgJ0i6IJcptLUw/view?usp=sharing

##Features
The front page is simple. It contains a navbar with a searchbox, and a main search box.

The nav bar allows for naviagtion and also has a searchbar.

The project has a registration and login system.

If the user is not loggin in, they will only be able to access the "home", "about", "resource list", "register" and "login" pages. 

If the user is logged in, they will be able to access the "add a resource" page and "category list" pages. They will also have access to edit and delete functions.

The CRUD functions are linked to an external MongoDB database and paswords are stored securely.

##Existing Features
The first feature (the search bar) allows the user to serch the database using key words.

The results page shows the results.

Logged in users can search, add, edit and delete resources and categories. Logged out users can search and view the resources.

The "add a resource" page allows the user to fill out a form which will add to the database.



##Features Left to Implement
A function to allow the user to reset their password.

A function allowing the resources to be collated under the same heading in the resource list.

A function allowing the search results to be collated under the search term for easy viewing.

##Technologies Used
The technologies used include:

[Html] The basis of the project was made using HTML

[CSS] CSS was used to add styles on top of Bootstrap

[Materialize] Materialize was used for styling.

[Vanilla Javascript] This project uses javascript to add functionally. Additionally it uses Javascript to calculate ideal body weight, body mass index, creatinine clearance (kidney function), the initial dose of vancomycin, the maintenance dose of vancomycin and the frequency of monitoring of the drug.

[JQuery] The project uses JQuery to simplify DOM manipulation. In this project, it was only used for the bootstrap features.

##Testing
The code was tested using jshint.com. No major issues were identified.

The tool was tested on both mobile and desktop screens.

As the aim is for the tool to be implemented in a clinical setting and for screen switching to be minimised as much as possible.

The the webpage has been tested on windows desktops. Note that it was not tested on 4k resolutions as these were not present in the hospital computers.

The webpage was tested on chrome, internet explorer and firefox.

The webpage was also tested on the following mobile devices: Huawei Mate 20 pro iPhone 7 Samsung Galaxy s8 Samsung Galaxy S10

Testing the tool:

Deployment
To run the project, simply go to http://pharmacy-search.herokuapp.com/

Credits
Content

Acknowledgements
My 