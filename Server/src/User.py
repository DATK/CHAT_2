from Server.src.modules import json,os

class User:
    
    def __init__(self,login,password):
        self.login=login
        self.password=password
        self.path=f"./Server/users/"
        self.path_user=f"./Server/users/{self.login}.json"
        
    def have_user(self):
        files=os.listdir(self.path)
        if f"{self.login}.json" in files:
            return 1
        else:
            return 0
        
    def reg_user(self,name):
        if self.have_user():
            return ("HavingUsers",0)
        else:
            self.usr={"login":self.login,"password":self.password,"rules":{"READ": 1, "WRITE": 1,"CREATE":1,"CREATE_MAX":2, "CREATE_NOW":0},"parm":{"name": name}}
            with open(self.path_user,"w",encoding="UTF-8") as f:
                json.dump(self.usr,f)
            return ("Succses",1)
            

    def chek_reg(self):
        if self.have_user():
            with open(self.path_user,"r",encoding="UTF-8") as f:
                tmp_us=json.load(f)
            if tmp_us["password"]==self.password and tmp_us["login"]==self.login:
                self.usr=tmp_us
                return ("Succses",1)
            else:
                return ("Login or password is uncorrect",0)
        else:
            return ("No this user",0)

    def get_rules(self):
        return self.usr
    
    
    def change_(self,rule,znach):
        if rule=="name":
            self.usr["parm"]["name"]=znach
            with open(self.path_user,"w",encoding="UTF-8") as f:
                json.dump(self.usr,f)
            return "Succses"
        
        elif rule=="password":
            self.usr["password"]=znach
            with open(self.path_user,"w",encoding="UTF-8") as f:
                json.dump(self.usr,f)
            return "Succses"
        