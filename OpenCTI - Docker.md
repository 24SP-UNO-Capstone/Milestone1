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

View pre-built connectors here https://github.com/OpenCTI-Platform/connectors/tree/master/external-import 

This example will setup alienvault. 

Cope this exact text from the connector's docker-compose file. 

![image](https://github.com/24SP-UNO-Capstone/Milestone1/assets/51690971/d5bdafee-55d0-4778-8460-ddedb9dcfce8)

Paste it into the bottom of your project's docker-compose, make sure to fill in the required fields. 
  - Required fields are:
    - OPENCTI_TOKEN
    - ALIENVAULT_API_KEY
    - ALIENVAULT_PULSE_START_TIMESTAMP (Use today's date or you will get a lot of results)

Run the "Docker compose down" and "Docker compose up" commands to restart the stack. A new container will exist and will automatically pull feeds into your dashboards. 

You can check the connector's status by visitng the **Data** - **Ingestion** - **Connectors** page. 

![image](https://github.com/24SP-UNO-Capstone/Milestone1/assets/51690971/eace5448-dc6b-437a-82ad-271129c5f572)

Example of results in your dashboard. 

![image](https://github.com/24SP-UNO-Capstone/Milestone1/assets/51690971/b4dec165-3c33-4dc4-b889-ae2d056694a4)


## Add a RSS feed example

In GUI, go to **data**, **ingestion**

![image](https://github.com/24SP-UNO-Capstone/Milestone1/assets/51690971/22e75353-af93-4b8a-8903-0f766b30b82d)

Click **RSS feeds**

![image](https://github.com/24SP-UNO-Capstone/Milestone1/assets/51690971/8b4b8762-9689-4f5c-9898-dd4294e4fe04)

Click the **plus** button

![image](https://github.com/24SP-UNO-Capstone/Milestone1/assets/51690971/e653abe4-3b0f-4f98-8f6e-efb086184f96)

Enter **Name, Description, feed url**

![image](https://github.com/24SP-UNO-Capstone/Milestone1/assets/51690971/dc037b7c-13a2-42b9-9955-170e1f49e06c)

Click 3 dots, **start** 

![image](https://github.com/24SP-UNO-Capstone/Milestone1/assets/51690971/6c327cb4-7018-4091-b2e7-195f8751dc90)

Click **start**

![image](https://github.com/24SP-UNO-Capstone/Milestone1/assets/51690971/f1809aa9-926d-4072-9802-cd35e89033ec)

On your **home** dashboard, details will start flowing

![image](https://github.com/24SP-UNO-Capstone/Milestone1/assets/51690971/b79ecd0a-5d07-4f09-810e-004d07b3eebd)

## Add a TAXII feed example

This example will setup MITRE TAXII feed, below is some required information from MITRE's guide. 

![image](https://github.com/24SP-UNO-Capstone/Milestone1/assets/51690971/1a741765-c1da-4f9f-83b8-fb26079fa3eb)

In your Open CTI, go to **data** then **ingestion**

![image](https://github.com/24SP-UNO-Capstone/Milestone1/assets/51690971/52e803f4-7492-4c38-b0f3-e75234b6411e)

Go to **TAXII Feeds** 

![image](https://github.com/24SP-UNO-Capstone/Milestone1/assets/51690971/cf23280b-c20b-4185-a01a-675c85147809)

Click the **plus** button

![image](https://github.com/24SP-UNO-Capstone/Milestone1/assets/51690971/8c68eaaa-3614-486b-9708-9eeb3ea5a994)

Fill in the required information 
  - Required fields are:
    - Name
    - Description
    - TAXII Server URL
    - TAXII Collection
    - Import Date (Use today's date)
   
Click Create when finished.

![image](https://github.com/24SP-UNO-Capstone/Milestone1/assets/51690971/ee0dc431-8c94-4bc6-965f-29b2009d22a6)

Information will start flowing into your dashboards. 
