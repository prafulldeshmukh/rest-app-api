# rest-app-api
Mac Address APP API Source Code

#Instruction for use application rest-api-app for showing MAC address with associated details with company name

The follow below step for install application & run 
1.Get the clone of below repository
  https://github.com/prafulldeshmukh/rest-app-api.git

 2.Install docker on your system 
   # use the below url for installation
     https://docs.docker.com/install/linux/docker-ce/ubuntu/

    
    I) Update the apt package index:

      $ sudo apt-get update

    Install packages to allow apt to use a repository over HTTPS:

      $ sudo apt-get install \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg-agent \
        software-properties-common
   $ sudo docker -v
   $ sudo docker run hello-world
   $ sudo docker images
   $ sudo docker ps -a
     
3. Install docker-compose for up and running aplication
   # https://docs.docker.com/compose/install/

   $ sudo pip install docker-compose

4.first build application with docker
  $ sudo docker build
  #It deploy & build all apllication which u mentioned in dockerfile 
  # Python, Djnago & djnago restframework

 5. After successfully build you have to run the command for .yml file
    $ sudo docker-compose build
 6.Make service up and running in docker-container
    $ sudo docker-compose up 
 7.Use the below API on command prompt
   $ curl http://localhost:8000/getMacDetails/44:38:39:ff:ef:57
   #user will get the output of mac address & company name with json resposne
       OR
   # On Web browser
     $http://<your server ip>:8000/getMacDetails/44:38:39:ff:ef:57

   # Response Output:
   {"mac_address": "44:38:39:ff:ef:57", "companyName": "Cumulus Networks, Inc"}  
 8. Added validation part if u enter wrong mac address with jsonresponse 
 9. API will be consume through below URL    
    #$http://<your server ip>:8000/getMacDetails/44:38:39:ff:ef:57
         

