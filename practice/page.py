class page:
    def __init__(self,page,perpage):
        self.page = page
        self.perpage = perpage
    @property
    def startpage(self):
        return self.perpage*(self.page-1)+1
    @property
    def endpage(self):
        return self.perpage*self.page+1
obj = page(12,80)
for pageone in range(obj.startpage,obj.endpage):
    print(pageone)