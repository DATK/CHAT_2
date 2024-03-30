from Server.src.modules import datetime,os,json

class Messange:
    
    def __init__(self,text,user_name,login):
        self.sms={"from":user_name,"content":text,"login":login}
        
    def get(self):
        return self.sms
    
class Storer:
    
    def __init__(self,id):
        self.id=id
        self.path="D://CHAT_2/Server/messanges/"
        self.path_f=f"D://CHAT_2/Server/messanges/{self.id}.json"
    
    def set_mes(self,mes):
        self.mes=mes.get()
    
    def is_id(self):
        files=os.listdir(self.path)
        if f"{self.id}.json" in files:
            return 1
        else:
            return 0   
        
    def write(self):
        if self.is_id():
            with open(self.path_f,"r",encoding="UTF-8") as f:
                tmp=json.load(f)
            tmp[f"{datetime.datetime.now()}"]=self.mes
            with open(self.path_f,"w",encoding="UTF-8") as f:
                json.dump(tmp,f)
        else:
            tmp={}
            tmp[f"{datetime.datetime.now()}"]=self.mes
            with open(self.path_f,"w",encoding="UTF-8") as f:
                json.dump(tmp,f)
    
    def read(self):
        if self.is_id():
            with open(self.path_f,"r",encoding="UTF-8") as f:
                tmp=json.load(f)
            i=0
            ln=len(tmp)-1    
            for key in tmp:
                if i==ln:    
                    return f"{tmp[key]["content"]}"
                else:
                    i+=1
                  

                


        