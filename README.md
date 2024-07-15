# <center> Fast API Exercise </center> 
### Full Name: Aarón Martin Castillo Medina 
### Email: aaroncastillo329@gmail.com

<br>

The following project consists in the development of a system that creates a API REST.

The tool used for API REST is Fast API (0.111.0) and Docker.

It's important to install Docker before this execution, whose instructions are not included in this README.

The project's structure is the following: 

```
.
|-- app
| ´-- app.py 
| ´-- requirements.txt 
|-- sources
| `-- foo.txt
|-- Dockerfile
|-- simulation_interactions.py

```

<br>

I briefly explain each one of these elements: 

* **app.py** - the file that contains the Fast Api server. 
* **requirements.txt** - Python libraries that are required for the project. 
* **foo.txt** - file required to maintain the sources folder. 
* **Dockerfile** - file requested to initialize the server.
* **simulation_interactions.py** - file created to emulate the actions from the user perspective (requests).

<br>

In order to execute the code by using docker, you should utilize the following commands: 

<br>

```console
**docker build --tag docker_fast_api .**
```

<br>

<center> (Don't forget the dot at the end) </center> 

<br>
<br>

And then:

**docker run -d --name fast_api_final -p 80:80 docker_fast_api**

<br>

Regarding the considerations mentioned for the project:

## PERSISTANCE
* In the container, the number of counts per endpoint are stored in a file called counter.txt, so everything will be modified and stored there..

## SECURITY
* I am keen on security by obscurity, which means that each one of the functionalities does exactly what it's needed, even the script simulation_interactions.py contains this essence as it represents only the necessary actions that a user or a client-side script would carry out.

## WAYS OF TESTING
* As I mentioned before, I included some functionalities within the file simulation_interactions.py, but in case the tester wants to try another path, I include (assuming that the server is located in 127.0.0.1)
  
* http://127.0.0.1/get_count
* http://127.0.0.1:80/get_date?boolean=False
* http://127.0.0.1:80/get_date?boolean=True
* http://127.0.0.1:80/get_date?boolean=x

Or there's even the possibility of carry out some tests by using Postman por instance (functionality not included in this code): 

![imagen](https://github.com/amcm329/fast_api_exercise/assets/35039222/438928d5-d6e8-4ee7-9ff3-8b2193d4c8ac)

![imagen](https://github.com/amcm329/fast_api_exercise/assets/35039222/a856455b-1d3a-4971-abbb-7eedb4796305)

![imagen](https://github.com/amcm329/fast_api_exercise/assets/35039222/b0126094-fb64-41fb-a5ae-bf94221f34a1)


<br>
