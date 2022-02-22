# dataak_task
this is a crwaler with frst page for this [url](https://api.digikala.com/v1/categories/mobile-phone/search/?sort=4&page=1) and save to mysql DB.
## how to run:
1. create .env file:
* The first step use sample.env and create a .env file for config(you must fill DB config)
2. run Mysql with docker-compose:
* before running the service, we must set the config for docker-compose from .env for it after step one uses this command ``` docker-compose config ```
* up docker-compose with this command ``` docker-compose up -d ```
3. create virtualenv the root dirtcory of project with command ``` virtualenv .venv ``` and install requrment.txt file packeg with this command ` pip install -r requrment.txt`
4. use `pwd` command in project dirctory and copy output.
5. fill `<PWD-output>` with step 4 ` * * * * * <PWD-output>/bash.sh '<PWD-output>' >> <PWD-output>/log.txt `
6. open terminal and write `crontab -e` add step 5 output to end of this file. save file and enjoy it.:)

----- 

