Quick notes from Dillon around setting up Open CTI via Docker. 

## Installation

Install your favorite container management software. 

Official Open CTI guide is [here](https://docs.opencti.io/latest/deployment/installation/#using-docker1)

Unofficial Notes:

Create a folder for this project, then use Powershell to CD to that folder 

Run the command git clone https://github.com/OpenCTI-Platform/docker.git

![image](https://github.com/24SP-UNO-Capstone/Milestone1/assets/51690971/3e70211f-3a79-480d-8a46-81050d73ca03)

CD to the newly created folder named docker

Edit the sample environment file and after editing, rename to .env   (no text should be in front of the file extension, your docker software will handle this just fine)

In the sample file, make sure to edit these fields

- In the sample file, make sure to edit these fields
  - OPENCTI_ADMIN_EMAIL
  - OPENCTI_ADMIN_TOKEN
    - Use something like https://www.uuidgenerator.net/version4 to generate a uuid v4 token.
   

When ready, run the "docker compose up" command from Powershell 
- Note: the very first run will take multiple minutes. 
![image](https://github.com/24SP-UNO-Capstone/Milestone1/assets/51690971/bf909081-7152-4fdc-9291-2a3d7281b3f3)

If no errors occured, Give http://localhost:8080/dashboard a try 

## Add a Connector example

## Add a RSS feed example

## Add a TAXII feed example

