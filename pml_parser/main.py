from exceptions import PymlSyntaxError


class Parser:
    def __init__(self):
        self.filename = None 
        self.ptn = None
        self.ctn = None
    def parse(self,filename):
        self.filename = filename
        filename = self.filename
        class PS():
            def __init__(self):
                self.filename = filename
                
                
                with open(self.filename) as file:
                    self.data = file.readlines()
            def get_tag_value(self,tag_name):
                dt = self.data
                wd = ""
                for i in dt:
                    for l in i:
                        if l != "\n":
                            wd = wd+l         
                try:
                         
                    value = wd.split(f"[{tag_name}")[1].split(f"]",maxsplit=1)[1].split(f"[/{tag_name}]")[0]
                except IndexError:
                    raise PymlSyntaxError("Syntax Error Occurred")
                self.value = value
                return value                        
            def get_sub_tag_value(self, parent_tag_name,child_tag_name,parent_tag_is_subtag=False):
                sbv = self.get_sub_tag_value
                sptv = self.get_tag_value
                stp = self.get_sub_tag_property
                sdata = self.data
                class SubTagValue():
                    def __init__(self, parent_tag_name,child_tag_name,parent_tag_is_subtag):
                        dt = sdata
                        wd = ""
                        for i in dt:
                            for l in i:
                                if l != "\n":
                                    if l.isspace():
                                        wd = wd.strip()+l
                                    else:
                                        wd = wd+l
                        val = ""                
                        if not parent_tag_is_subtag:                
                            val = sptv(parent_tag_name)
                        else:
                            try:
                                val = wd.split(f"[<{child_tag_name}>")[1].split("]",maxsplit=1)[1].split(f"[</{child_tag_name}>]")[0].replace(f"[</{child_tag_name}>","")
                            except:
                                pass
                        try:    
                            value = val.split(f"[<{child_tag_name}>")[1].split("]",maxsplit=1)[1].split(f"[</{child_tag_name}>]")[0].replace(f"[</{child_tag_name}>","")
                        except:
                            value = val
                        svalue = value
                        self.value = value
                        self.svalue = svalue
                        ptn = parent_tag_name
                        class Value:
                            def __init__(self):
                                pass
                            def get_sub_tag_value(self,child_tag_name):
                                return sbv(ptn,child_tag_name,True) 
                            def get_sub_tag_property(self,child_tag,key):
                                return stp(ptn,child_tag,key)
                        self.bsv = Value()    
                    def get_sub_tag_value(self,child_tag_name):
                        return self.bsv.get_sub_tag_value(child_tag_name) 
                    def get_sub_tag_property(self,child_tag_name,key):
                        return self.bsv.get_sub_tag_property(child_tag_name,key)      
                    def get_value(self):    
                        return self.svalue.strip()
                        
                return SubTagValue(parent_tag_name,child_tag_name,parent_tag_is_subtag)   
            def focus_sub_tag(self, parent_tag_name,child_tag_name):
                self.ptn = parent_tag_name
                self.ctn = child_tag_name
                msl = self
                class ST(PS):
                    def __init__(self):
                        self.ptn = msl.ptn
                        self.ctn = msl.ctn
                    def get_sub_tag_value(self,child_tag):

                        return msl.get_sub_tag_value(self.ctn,child_tag,True)      
                    def focus_sub_tag(self, child_tag_name):
                        return msl.focus_sub_tag(self.ptn, child_tag_name) 
                    def get_value(self):
                        return msl.get_sub_tag_value(self.ptn,self.ctn).get_value()
                    def get_sub_tag_property(self,child_tag,key):
                        return msl.get_sub_tag_property(self.ptn,child_tag,key) 
                    def get_property(self,key):
                        return msl.get_sub_tag_property(self.ptn,self.ctn,key)
                return ST()    
            def get_sub_tag_property(self,parent_tag_name,child_tag_name,key):
                dt = self.data
                wd = ""
                for i in dt:
                    for l in i:
                        if l != "\n":
                            wd = wd+l
                try:                       
                    value = self.get_tag_value(parent_tag_name)
                    svalue = ""
                    if ";" in value.split(f"[<{child_tag_name}>")[1].split(f"{key}=")[1].split("]",maxsplit=1)[0]:
                        svalue = value.split(f"[<{child_tag_name}>")[1].split(f"{key}=")[1].split(";")[0] 
                    else:
                        raise PymlSyntaxError(f"Semicolon not found after key..")    
                    value = svalue
                    
                except IndexError:
                    raise PymlSyntaxError("Invalid Syntax of Tag") 
                if value == None:
                    pass                   
                elif value.isnumeric():
                    return int(value)
                elif '"' in value or "'" in value or "`" in value:
                    try:
                        return value[1:][:len(value) - 2]
                    except:
                        raise PymlSyntaxError("Invalid Syntax")       
                elif value.strip().lower() == "false" or value.strip().lower() == "true":
                    return bool(value)                                                                                                           
                else:
                    return value                                  
            def get_tag_property(self,tag_name,key):
                dt = self.data
                wd = ""
                for i in dt:
                    for l in i:
                        if l != "\n":
                            wd = wd+l
                try:                       
                    value = wd.split(f"[{tag_name}")[1].split("]")[0].split(f"{key}=")[1].split(";")[0]  
                
                except IndexError:
                    raise PymlSyntaxError("Invalid Syntax of Tag or Tag does not exists")
                if value == None:
                    pass                   
                elif value.isnumeric():
                    return int(value)
                elif '"' in value or "'" in value or "`" in value:
                    try:
                        return value[1:][:len(value) - 2]
                    except:
                        raise PymlSyntaxError("Invalid Syntax")    
                elif value.strip().lower() == "false" or value.strip().lower() == "true":
                    return bool(value)                                                                                            
                else:
                    raise PymlSyntaxError("Unknown type of Property String and Integers are only supported") 
        ps = PS()          
        return ps                                       