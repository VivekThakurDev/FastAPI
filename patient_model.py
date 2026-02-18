from pydantic import BaseModel, EmailStr,AnyUrl,Field
from typing import List,Dict,Optional


class Patient(BaseModel):
    name:str
    age:int
    Email:EmailStr
    linkedin:AnyUrl
    weight:float=Field(gt=20,le=100)
    married:bool
    allergies:Optional[list[str]] 
    contact_detail:Dict[str,str]
     
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.Email)
    print(patient.linkedin)
    print(patient.weight)
    print(patient.allergies)
    print(patient.married)
    print(patient.contact_detail)
    print('inserted')

# def update_patient_data(patient:Patient):
#     print(patient.name)
#     print(patient.age)
#     print('updated')

patient_info = {'name':'vivek',
'age':30,
'Email':'kvivek21754@gmail.com ',
'linkedin':'http://www.linked.com/',
'weight':5.3,
'married': True,
'allergies':['dama','jadu','mirgi'], 
'contact_detail':{'phone':'46646464'} }

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
# update_patient_data(patient1)