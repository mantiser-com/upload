# Upload

This app upload data from our bots to diffrent endpoints. 
As defualt it uplaod to our API and to store into clients account.


The app runs and lissen to a NATS que. Json then posted to that que is uplaoded to the clients account.



## Build and run

To start local dev build and start with docker-compose


```
docker-compose build
docker-compose run
```


