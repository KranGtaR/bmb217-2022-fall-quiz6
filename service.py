"""Quiz 6
Numara: 2020717042
Ad Soyad: Kasım Ünal
"""
from datetime import date 
 
class Service:

    toplam=0
    workmanship_rate:float=0.0
    service_name=" "
    price_list = {
        "yag":400,
        "yag_filtresi":75,
        "hava_filtresi":110,
        "polen_filtresi":60,
        "yikama":50,
        "motor_temizligi":100,
        "buji":600,
        "aku":1500,
        "balata":750,
        "disk":1600,
        "triger":1250,
    }

    def __init__(self, plate_no, name_surname, work_list=[]) -> None:

        self.plate_no=plate_no
        self.name_surname_=name_surname
        self.work_list=work_list
        self.tamamlanan_isler=[]
        

    @classmethod
    def onbin(cls,plate_no:str, name_surname:str, work_list=[]):

        work_list=["yag","yag_filtresi","hava_filtresi","polen_filtresi","yikama"]
        return cls(plate_no,name_surname,work_list)


    
    @classmethod
    def yirmibin(cls,plate_no:str, name_surname:str, work_list=[]):

        work_list=["motor_temizligi","balata","disk","yag","yag_filtresi","hava_filtresi","polen_filtresi","yikama"]
        return cls(plate_no,name_surname,work_list)
    
        
    
    @classmethod
    def otuzbin(cls,plate_no:str, name_surname:str, work_list=[]):

        work_list=["motor_temizligi","balata","disk","yag","yag_filtresi","hava_filtresi","polen_filtresi","yikama"]
        return cls(plate_no,name_surname,work_list) 
    


    @property
    def name_surname(self) -> str:

        __isim,__soyisim=self.name_surname_.split(" ")
        
        newisim=__isim[0:3]+"***"
        new_soyisim=__soyisim[0:3]+"***"
        return newisim+" "+new_soyisim
        


    @name_surname.setter
    def name_surname(self,value:str) -> None:

        a=value.split(" ")
        __isim=a[0]
        __soyisim=a[1]
        return __isim,__soyisim
        


    @classmethod
    def set_workmanship_rate(cls,workmanship_rate:float) -> None:

        cls.workmanship_rate=workmanship_rate
        


    @classmethod
    def set_service_name(cls,service_name) -> None:

        cls.service_name=service_name
        
    

    def do_worklist(self):

        ücretler=[]

        for i in self.work_list:

            ücretler.append(self.price_list[i])
            self.tamamlanan_isler.append(i)

        for j in ücretler:

            self.toplam=self.toplam+(j*self.workmanship_rate)+j
            
            

    def print(self) -> None:

        tarih=date.today()
        print("-"*20)
        print("{}-{}-{}".format(self.plate_no,self.name_surname,tarih))

        for i in self.work_list:
            print("*{} , {} tl , {} tl".format(i,self.price_list[i],self.price_list[i]*self.workmanship_rate))

        print("*İşçilik orani : {}".format(self.workmanship_rate))
        print("*Toplam : {} tl".format(self.toplam))
        print("*Servis : {}".format(self.service_name))
        print("-"*20)

    

    def anonymize(_in) -> str:

        new=_in[0:3]+"***"
        return new
         
