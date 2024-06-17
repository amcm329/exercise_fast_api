"""
   This snippet of code acts a simulation for using the endpoints created through the Fast API server.
   
"""

import requests 

#Creating the headers section for all the following requests. 
headers = {
            'Content-type':'application/json', 
            'Accept':'application/json'
          }


""" Endpoint that gets the datetime according to a boolean.
 
    Parameters
    ------------
        boolean: idem
        
    Return
    -----------
        response : Json
            It contains: 
             * timestamp.
             * status.
             * message.  
             * mimetype.                          
""" 
def test_retrieve_date(boolean): 
    response = requests.post('http://127.0.0.1:80/get_date?boolean=' + str(boolean), headers=headers)    
    return response.json()


""" Endpoint that gets the current endpoints count.

    Return
    -----------
        response : Json
            It contains: 
             * count.
             * status.
             * message.  
             * mimetype.                          
"""
def test_get_count():                   
    response = requests.get('http://127.0.0.1:80/get_count',  headers=headers)
    return response.json()



"""
   This is the section related to the tests. 
"""
print(test_retrieve_date(True))
print(test_retrieve_date(False))
print(test_retrieve_date("x"))
print(test_get_count())


#docker build --tag docker_fast_api .
#docker run -d --name fast_api_final -p 80:80 docker_fast_api

#http://127.0.0.1/get_count
#http://127.0.0.1:80/get_date?boolean=False