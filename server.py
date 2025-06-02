from fastapi import FastAPI,Request
import json
import time
app = FastAPI()

@app.get("/pvestate/")
def read_root(request: Request):
    client_ip = request.client.host
    
    with open("serverip.json", "r") as file:
        ips = file.read()
        ips = json.loads(ips)
        

    with open("state.json", "r") as file:
        data = file.read()
    data = json.loads(data)
    # print(data['state'])
    
    if client_ip in ips['ips']:
        if data['state']== "ok":
            data['state']= "running"
        elif data['state']== "fuck":
            time.sleep(30) 
        elif data['state']== "fuckedup":
            time.sleep(60)
            
        return data

@app.get("/test/")
def root(request: Request):
    client_ip = request.client.host
    with open("serverip.json", "r") as file:
        data = file.read()
        data = json.loads(data)
    if client_ip in data['ips']:
        return {"message": "bad request"}
