import socket

class DNS_Lookup(object):
    
    def __init__(self, domain_name):
        self.name = str(domain_name)
        
    def resolve(self):
        
        ip_address = socket.getaddrinfo(self.name, 80, proto=socket.IPPROTO_TCP)

        

        return ip_address
    


if __name__ == "__main__":
    pass