from core import DNS_Lookup


class Cleaner(object):

    def __init__(self, thing):
        self.item = thing

    def clean(self):
        a = str(self.item)
        b = a[18:-2]
        c = DNS_Lookup(b)
        d = c.resolve()
        e = str(d)
        f = e.split()
        for i in f:
            if len(i) > 8:
                if 'AddressFamily' not in i:
                    g = str(i)
                    print(g[2:-2])

if __name__ == "__main__":
    pass