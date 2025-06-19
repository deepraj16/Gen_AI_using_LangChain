from pydantic import BaseModel ,EmailStr,Field
from typing import Optional 

class Student(BaseModel): 
    name : str ='deepraj'  #by default value in student class 
    age: Optional[int] = None 
    email:EmailStr
    cgpa : float = Field(gt=0,lt=10,default=4,description="A decimal repsent")

 
new_student={'age':'32','email':"abc@gmail.com",'cgpa':5.5}
student=Student(**new_student)

student_info=dict(student) 

student_json=student.model_dump_json()

print()
print(student_json)


    
