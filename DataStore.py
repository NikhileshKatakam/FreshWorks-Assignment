class DataStore:
    def __init__(self,path=None):
        self.dictionary = dict()
        self.dirty = False
        if(path == None):
            self.path = "C:\\DataStore\\"
        else:
            self.path = path
        self.file = None
        self.__create()
    def __parseContent(self,content):
        items = content[0][1:-1].split(",")
        data = list(map(lambda x:x.split(":"),items))
        for i in range(len(data)):
            data[i][0] = data[i][0][1:-1]
            try:
                data[i][1] = int(data[i][1][1:])
            except:
                data[i][1] = None



        #print(data)
        keys = []
        vals = []
        #for item in data:
        x = dict(data)
        #print(x)
        
    def __create(self):
        # CREATE A BASIC FILE
        self.file = open(self.path+"datastore.txt",'a+')
        self.file.seek(0)
        content = self.file.readlines()
        self.__parseContent(content)
        self.file.close()
        try:
            os.mkdir(self.path+"Files")
        except FileExistsError:
            pass
    def __update(self):
        DataStoreFile = open(self.path+"datastore.txt",'w')
        DataStoreFile.write(str(self.dictionary))
        DataStoreFile.close()
        self.dirty = False
        print("DataStore's current size is : "+str(os.stat(self.path+"datastore.txt").st_size)+" bytes")

    def create(self,obj):
        obj = str(obj)        
        key = str(hash(obj))
        if(len(key)>32):
            raise "Key length exceeded!"

        if(key in self.dictionary):
            #Need not create a new record
            return
        tempFile = open(self.path+"Files\\"+key+".txt","w+")
        tempFile.write(obj)
        tempFile.close()
        self.dictionary.update({key:None})
        self.dirty = True
        self.__update()

    def delete(self,key):
        if(key not in self.dictionary):
            print("Unable to find the given key")
            return
        del self.dictionary[key]
        self.__update()
        print("File deleted!")

    def read(self,key):
        if(key not in self.dictionary):
            print("Unable to find the given key")
            return
        #return json.loads(self.dictionary[key])
        tempFile = open(self.path+"Files\\"+key+".txt","r")
        tempFile.seek(0)
        data =  tempFile.readlines()
        tempFile.close()
        return str(data[0])