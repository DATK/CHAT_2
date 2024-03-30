import requests as r

ip="127.0.0.1:5000"

adresa={"reg":f"http://{ip}/regestration/qedsfw342refd/",
        "vhod":f"http://{ip}/vhod/dsadi3dijap213d",
        "mes":f"http://{ip}/get/messenge/",
        "chg": f"http://{ip}/changes/users/who/",
        "name":f"http://{ip}/get_usr_name/shaudipfl/fds"}

class Sender:
    
    def __init__(self,adresa = adresa,ip = ip) -> None:
        self.adresa=adresa
        self.ip=ip
        
    def reg(self,js):
        try:
            return r.post(self.adresa["reg"],json=js).text
        except:
            return "NoServerConnection"
    
    def vhod(self,js):
        try:
            return r.post(self.adresa["vhod"],json=js).text
        except:
            return "NoServerConnection"
    
    def mes(self,id,js):
        try:
            return r.post(f'{self.adresa["mes"]}{id}',json=js).text
        except:
            return "NoServerConnection"
    
    def chg(self,js):
        try:
            return r.post(f'{self.adresa["chg"]}',json=js).text
        except:
            return "NoServerConnection"
        
    def getname(self,js):
        try:
            return r.post(f'{self.adresa["name"]}',json=js).text
        except:
            return "NoServerConnection"
    
    def ip_upd(self,ip):
        self.adresa={"reg":f"http://{ip}/regestration/qedsfw342refd/",
        "vhod":f"http://{ip}/vhod/dsadi3dijap213d",
        "mes":f"http://{ip}/get/messenge/",
        "chg": f"http://{ip}/changes/users/who/",
        "name":f"http://{ip}/get_usr_name/shaudipfl/fds"}
        