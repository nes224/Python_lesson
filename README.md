'''
OOP มีแนวคิดแบบโลกความจริงมีพื้นฐานเป็นวัตถุหรือ Object หมายถึงโครงสร้างการเขียนโปรแกรมมีลักษณะเลียนแบบหรือจำลองวัตถุที่มีอยู่จริง
ประกอบด้วย Attribute เก็บค่าสถานะของวัตถุ
และสมาชิก function หรือ method มีการทำงานบางอย่างเป็นพฤติกรรมของวัตถุ
เป็นชนิดข้อมูลนามธรรม (Data abstraction) นำมาเขียนโปรแกรมให้มีความสามารถมากขึ้นใช้ในการแก้ไขปัญหาซับซ้อน โดยมีหลัการสำคัญคือ

- Encalsulation เป็นการนำ attribute ที่เป็นชนิดข้อมูล (data type) และมีพฤติกรรมเป็นการปฏิบัติการ Operation นำมาห่อหุ้มรวมไว้ด้วยกัน
  โดยปิดบังรายละเอียดและปกป้องข้อมูล
- Inheritance เป็นการนำวัตถุมีอยู่แล้วมีคุณสมบัติแบบทั่วไป นำมาใช้สร้างเป็นวัตถุใหม่ให้มีคุณสมบัติเฉพาะเจาะจงโดยการเพิ่มเติมขึ้นจากเดิม เป็นการนำมากลับมาใช้ใหม่
- Polymorphism เป็นการให้การปฏิบัติการตัวเดียว สามารถมีการทำงานได้หลายรูปแบบโดยการ Overriding และการ Overloading

คลาสและออบเจ็กต์
การเขียนโปรแกรมเชิงวัตถุมีเอ็นแคปซูเลชั่นเป็นหลักการสำคัญในเรื่องรวมข้อมูลและ function ห่อหุ้มเป็นก้อนเดียว
โดยมีส่วนประกอบพื้นฐานคือคลาส Class ออบเจ็กต์ Object และ เมธอด Method ซึ่ง Object เป็บบางสิ่งเก็บในหน่วยความจำมีสถานะ (state)
เป็นข้อมูลมีตัวแปรเป็นตัวแทนในการเก็บค่าไม่สามารถเรียกใช้งานจากภายนอก
มีชุดฟังก์ชั่น เรียกว่า method มีหน้าที่ในการทำงานและจัดการกับสถานะ

เมื่อต้องการใช้ object ต้องสร้างต้นแบบขึ้นมาก่อนเรียกว่า class เพื่อกำหนดรูปแบบสถานะและพฤติกรรมให้กับ object ที่สร้างขึ้นมาเรียก instantiate และมีตัวแปรเรียกว่า instance อ้างอิงไปยัง object (นิยมเรียกตัวแปร instance เป็น object)
แต่ละ object มีบุคลิกลักษณะเฉพาะตัวแตกต่างกันโดยมีสถานะใช้กำหนดคุณลักษณและพฤติกรรมใช้กำหนดการกระทำ (attribute) อย่างเช่นแต่ละคนเป็น object ประเภทเดียวกันแต่มีสถานะรูปร่างหน้าตาไม่เหมือนกัน มีพฤติกรรมต่างกันบางคนอาจเดิน วิ่ง นอน กิน object จึงแยกออกเป็นแต่ละประเภท
Classify มีคุณสมบัติเหมือนหรือคล้ายกันเรียกว่า class หากแตกต่างไม่เหมือนกันจะแยกไปเป็น class ประเภทอื่น เช่น ประเภทของ มนุษย์ รถยนต์ และรูปทรง กำหนดได้เป็น class Animal, Car, และ Shape

---

## | Human | ชื่อ class

| name |
| gender | ตรงกลางเป็นคุณลักษณะเป็น attribute
| height |
| weight |

---

| talk |
| eat | ส่วนล่างคือการกระทำเป็น method
| walk |
| run |

---

'''
การสร้าง Object มีคุณลักษณะและการกระทำเหมือนกัน คลาสต้นแบบจะใช้การ instantiate
มีการประกาศแบบเดียวกับตัวแปร เป็นไดอาแกรม object diagram ของ object man
โดนอิน instantiate มาจากคลาส Human มีสถานะเป็นชื่อสมชาย เพศชาย ส่วนสูง 176 น้ำหนัก 79

                       InstanceOf (หมายถึง object Man เป็น instance ของ class Human)

---

| Human | <-------------------> | Man : Human |

---

| name | |name = 'Somchai'|
| gender | |gender='M' |
| height | |height = 176 |
| weight | |weight = 79 |

---

การกำหนด Class
class เป็นแบบจำลอง object ให้ผู้เขียนโปรแกรมใช้เป็นต้นแบบ object ประกอบด้วย attribute เป็นสมาชิกข้อมูลและ พฤติกรรมเป็นสมาชิก function หรือ method การสร้าง class เป็นต้นแบบให้ object ต้องกำหนดขึ้นมาก่อน เพื่อกำหนด instantiate ค่าเริ่มต้นให้กับ class

class class_name:
"""this is document string """

    # initialzer method or constructor
    def __init__(self):
        # attribute declaration and inital value
        self.attribute_name = initial_value

    # methods
    def method_name(self):
        body_block_statement

ส่วนหัวคลาสเริ่มด้วย keyword class ตามด้วยชื่อ class_name และปิดท้ายด้วยสัญลักษณ์ : บรรทัดถัด
และ ถัดมากำหนด attribute ให้ class โดยใช้ method **init**() เรียกว่า constructor
ใช้ประกาศ attribute หรือ สมาชิกข้อมูลเป็นตัวแปร (attribute_name) และกำหนดค่าเริ่มต้น (initial_value) ให้
จากนั้นเป็นการกำหนด method (method_name) ให้ class เป็นสมาชิก function ทำงานตามที่ต้องการใช้จัดการกับ attribute

class Person:
"""<<< The Person Class 1.0 >>> """
def **init**(self):
self.name = ''
self.height = 0
self.weight = 0

    def person_info(self):
        return 'Name: {}, Height: {}, Weight: {}'.format(
            self.name,self.height, self.weight )

สร้าง class Person โดยใช้ constructor กำหนด attribute ทั้งสามตัวคือ name, height, weight พร้อมกับกำหนดค่าเริ่มต้น
'', 0, 0 และกำหนด method person_info() เป็น function ใช้ส่งค่า attribute ทั้งสามตัวคืนกลับมาให้รูปของ string

แอตทริบิวต์
attribute กำหนดขึ้นมามีคำว่า self และสัญลักษณ์ . นำหน้าใช้เป็นตัวแทนของ object ที่ประกาศสร้างขึ้นมา ทำให้ ทราบว่า
attribute ดังกล่าวเก็บค่าให้ object ตัวนั้น และเรียกว่า instance attribute ถูกเรียกมาใช้หลังจากประกาศสร้าง object เท่านั้น attribute อีกประเภท เรียกว่า class attribute
สรุป instance attribute คือ self.name, self.height, self.weight

เมธอด
class มี method และ constructor กำหนดขึ้นมา หากนำมาใช้งานเป็นของ object ต้องกำหนด parameter อย่างน้อยหนึ่งตัวคือ self ใช้อ้างอิง object ที่ถูกใช้งานขณะนั้น และไม่ต้องส่งผ่านค่า argument เข้ามาเรียกว่า instance method หากมีการส่งค่า argument เข้ามาจะเป็นการส่งให้ parameter ลำดับถัดไป ยังมี method อีกสองประเภทคือ static method และ class method
สรุป instance method คือ person_info(self)

การนำ class สร้างขึ้นมารวมกับส่วนทำงานอยู๋ในไฟล์หรือ module เดียวกันเหมาะกับโปรแกรมขนาดเล็กและมี class ไม่มาก
หากโปรแกรมขนาดใหญ่มี class จำนวนมาก ควรมีการบริหารจัดการโดยแยก class เก็บไว้ใน module ต่างหาก
และ import เข้ามาใช้งาน ยังทำให้หลายโปรแกรมสามารถเรียกไปใช้งานได้จาก class Person ที่สร้างขึ้นมา

การสร้าง object
หลังจากสร้าง class เป็นชนิดข้อมูลแบบใหม่ จะประกาศสร้าง object ขึ้นมาใช้โดยมีคุณลักษณะแบบเดียวกับ class ใน การประกาศสร้าง object ใช้ constructor โดยมีสัญลักษณ์ () ต่อท้ายได้ object ส่งคืนกลับมาให้กับตัวแปรที่รอรับเรียกว่า instance อ้างอิงใช้งาน person = Person()
instance person อ้างไปยัง object สร้างขึ้นมาอยู๋ในหน่วยความจำได้พื้นที่ใช้เก็บค่า attribute เมื่อต้องการใช้งาน attribute จะใช้ชื่อ instance ตามด้วยดำเนินการ . เพื่ออ้างไปบัง attribute ที่ต้องการนำมาใช้ เช่นกำหนดค่าให้กับ attribute ได้
person.name = 'Suchada Srisawat'
person.height = 157
person.weight = 54
หรืออ้าง method เพื่อนำค่าของ attribute ส่งคืนกลับมาแสดงผลได้
person.person_info()

การเข้าถึงสมาชิก object
หลักการ encalsulation นอกจากรวม attribute และ method ไว้ด้วยกันใน class แล้วยังมีการปกป้องข้อมูลไม่อนุญาติให้ภายนอก class เข้ามาจัดการ attribute ได้โดยตรง เป็นการปิดบังเอาไว้เรียกกว่าซ่อนสารสนเทศและปิดบังรายละอียดการทำงานของ method จากภายนอก

การปกป้อง attribute
เพื่อปกป้องกันการเข้าถึงจากภายนอกกำหนด attribute เป็น Private โดย python จะใช้ชื่อ attribute นำหน้าด้วยอักษรขีดเส้นใต้สองขีดเรียกว่า
ดันเดอร์ Double Underscore, Dunder จาก attribute name, height, weight เป็น public เปลี่ยนเป็น private ได้โดย __name, __height, __weight
class Person:
    def __init__(self):
        self.__name = ''
        self.__height = 0
        self.__weight = 0

หากต้องการเข้าถึง attribute จะใช้แบบทางออ้อมดดยเรียกผ่าน method ที่กำหนดขึ้นมาให้จัดการแทน เรียกว่าการส่งผ่านข้อมูล (Message Passing)

Method Getter and Setter 
เมื่อปกป้องข้อมูลให้ attributeเป็น private ภายนอก class หากต้องการใช้งานต้องเข้าถึงทางออ้อมโดยผ่าน method ที่เป็น public เรียกว่า method getter and setter, method getter ทำหน้าที่ส่งค่าของ attribute คืนกลับไปให้ภายนอก class นำไปใช้งาน นิยมให้ชื่อว่า method มีคำว่า get นำหน้าด้วยชื่อ attribute ที่ส่งค่าคืนกลับไปให้ ช่วยให้เข้าใจสื่อความหมาย ปกติไม่กำหนด parameter รับค่า
class Person:
    def get_name(self):
        return self.__name
    
    def get_height(self):
        return self.__height
    
    def get_weight(self):
        return self.__weight

การใช้ method getter เพื่อยืนยันว่าภายนอก class รับค่า attribute ไปใช้งานได้อย่างเดียวไม่สามารถเปลี่ยนแปลงแก้ไขค่าได้ ส่วน method setter ทำหน้าที่รับค่าจากภายนอกให้กับ attribute เก็บไว้โดยกำหนด parameter ใช้รับค่าเข้ามา นิยมให้ชื่อ method มีคำว่า set นำหน้าชื่อ attribute ที่ต้องการเก็บค่าช่วยสื่อควาหมาย
class Person:
    def set_name(self, name):
        self.__name = name
    
    def set_height(self, height):
        self.__height = height
    
    def set_weight(self, weight):
        self.__weight = weight

การเก็บค่า attribute ผ่าน method setter ยังช่วงปกป้องข้อมูลกรณีค่าที่ส่งเข้ามาให้ไม่ถูกต้อง เช่น attribute __height กำหนดค่าความสูงน้อยกว่า 50 เขียน method ให้ตรวจสอบความถูกต้องของค่าที่รับเข้ามาก่อนนำไปเก็บไว้
class Person:
    def set_height(set, height):
        if height >= 50:
            self.__height = height
        else:
            print('Invalid height.')

