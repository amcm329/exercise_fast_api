"""
FastAPI service that receives: 

* A POST request with a boolean parameter that returns the current date in yyyy-mm-dd hh:ii:ss format if the parameter is true and returns the date in yyyy-dd-mm format if the parameter is false
* A GET request that obtains the value of a counter of times one of the two endpoints was called.
"""

from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

#File were the counter is persisted. 
sources_directory = "/home/sources/"

#We initialize a file (counter.txt) with 0.  
handler = open(f'{sources_directory}counter.txt',"w+")
handler.write("0\n") 
handler.close()

#App is initialized. 
app = FastAPI()



""" Auxiliary method that creates the datetime according to the mentioned constraints
 
    Parameters
    ------------
        boolean: idem
        
    Return
    -----------
        datetime : string/int
            * Complete datetime if boolean is true.
            * Partial datetime if boolean is false. 
            * -1 is there is no boolean. 
"""
async def create_datetime(boolean):
    final_date = ""
    now = datetime.now()
    
    #Complete format yyyy-mm-dd hh:ii:ss
    if boolean in (True, "True", "true"): 
       final_date = now.strftime("%Y-%m-%d %H:%M:%S")

    #Partial format yyyy-mm-dd  
    elif boolean in (False,"False", "false"): 
       final_date = now.strftime("%Y-%m-%d")
        
    #Invalid value. 
    else:
        final_date = -1 
        
    return final_date 


""" Auxiliary method that retrieves the current number of endpoints requests.  
        
    Return
    -----------
        current_number : int
              Current number of requests.  
"""
async def increase_count():

    #Reading the current number.
    handler = open(f'{sources_directory}counter.txt',"r+")
    files = handler.readlines()
    current_number = int(files[0][:-1])
    handler.close()
    
    #Increasing it by 1. 
    current_number += 1 
    
    #Persisting current number. 
    handler = open(f'{sources_directory}counter.txt',"w+")
    handler.write(f'{current_number}\n') 
    handler.close() 
    
    return current_number
    
    
""" Default endpoint.
        
    Return
    -----------
        response : Json
            It contains: 
             * Author's fullname.
             * Version.
             * Author's email.      
"""     
@app.get("/")
async def root():
      final_json = {
                    'Name': 'Aaron Martin Castillo Medina',
                    'Email': 'aaroncastillo329@gmail.com',
                    'Version': '1.0'
                   }
                   
      return JSONResponse(content=final_json) 
                  

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
@app.post("/get_date")
async def get_current_datetime(boolean: bool):
      #Values by default. 
      status = 200
      message = "OK"
      final_json = {}
      final_date = ""
      
      #We increase the counter. 
      value_count =  await increase_count()     

      try: 
        
         #We get the datetime according to the boolean. 
         final_date = await create_datetime(boolean) 
      
         #If boolean is not valid, a 404 status code is retrieved. 
         if final_date == -1: 
            status = 404 
            message = "Boolean not specified."
  
      #In case of any error during the process, a special set of 
      #messages is triggered. 
      except Exception as e: 
             status = 500
             message = str(e)
             final_date = "err"       
      
      #Returning the final json. 
      final_json = {
                    'timestamp': final_date,
                    'status': status,
                    'message': message, 
                    'mimetype': 'application/json'
                   }
      
      return JSONResponse(content=final_json) 


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
@app.get("/get_count")
async def get_current_count():
      #Values by default. 
      status = 200
      final_json = {}
      value_count = -1
      message = "OK"
      
      try: 
         #We get the count (and increase it).
         value_count = await increase_count()     

      #In case of any error during the process, a special set of 
      #messages is triggered.       
      except Exception as e: 
             status = 500
             message = str(e)
             value_count = -1 

      #Returning the final json.              
      final_json = {
                    'count': value_count,
                    'status': status,
                    'message': message, 
                    'mimetype': 'application/json'
                   }
      
          
      return JSONResponse(content=final_json) 


"""
   Main method. 
"""
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
