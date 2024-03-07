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
ดันเดอร์ Double Underscore, Dunder จาก attribute name, height, weight เป็น public เปลี่ยนเป็น private ได้โดย **name, **height, **weight
class Person:
def **init**(self):
self.**name = ''
self.**height = 0
self.**weight = 0

หากต้องการเข้าถึง attribute จะใช้แบบทางออ้อมดดยเรียกผ่าน method ที่กำหนดขึ้นมาให้จัดการแทน เรียกว่าการส่งผ่านข้อมูล (Message Passing)

Method Getter and Setter
เมื่อปกป้องข้อมูลให้ attributeเป็น private ภายนอก class หากต้องการใช้งานต้องเข้าถึงทางออ้อมโดยผ่าน method ที่เป็น public เรียกว่า method getter and setter, method getter ทำหน้าที่ส่งค่าของ attribute คืนกลับไปให้ภายนอก class นำไปใช้งาน นิยมให้ชื่อว่า method มีคำว่า get นำหน้าด้วยชื่อ attribute ที่ส่งค่าคืนกลับไปให้ ช่วยให้เข้าใจสื่อความหมาย ปกติไม่กำหนด parameter รับค่า
class Person:
def get_name(self):
return self.\_\_name

    def get_height(self):
        return self.__height

    def get_weight(self):
        return self.__weight

การใช้ method getter เพื่อยืนยันว่าภายนอก class รับค่า attribute ไปใช้งานได้อย่างเดียวไม่สามารถเปลี่ยนแปลงแก้ไขค่าได้ ส่วน method setter ทำหน้าที่รับค่าจากภายนอกให้กับ attribute เก็บไว้โดยกำหนด parameter ใช้รับค่าเข้ามา นิยมให้ชื่อ method มีคำว่า set นำหน้าชื่อ attribute ที่ต้องการเก็บค่าช่วยสื่อควาหมาย
class Person:
def set_name(self, name):
self.\_\_name = name

    def set_height(self, height):
        self.__height = height

    def set_weight(self, weight):
        self.__weight = weight

การเก็บค่า attribute ผ่าน method setter ยังช่วงปกป้องข้อมูลกรณีค่าที่ส่งเข้ามาให้ไม่ถูกต้อง เช่น attribute **height กำหนดค่าความสูงน้อยกว่า 50 เขียน method ให้ตรวจสอบความถูกต้องของค่าที่รับเข้ามาก่อนนำไปเก็บไว้
class Person:
def set_height(set, height):
if height >= 50:
self.**height = height
else:
print('Invalid height.')

พร็อพเพอตี้
การปกป้องข้อมูลโดย attribute เป็น private ภายนอก class เข้าถึงโดยผ่าน method getter and setter อาจไม่สะดวก หากต้องการเข้าถึง attribute โดยตรงแบบ public และยังคงมีการปกป้องข้อมูลแบบเดียวกับ method getter and setter จะนำ Property มาใช้โดยนำทั้งสองแบบมารวมกันทำให้ method ถูกมองเหมือนเป็น attribute

class Person:
@property
def name(self):
return self.\_\_name

    @property
    def height(self):
        return self.__height

    @property
    def weight(self):
        return self.__weight

property name, height, weight ทำงานแบบเดียวกันกับ method getter แต่เรียกใช้งานเป็นชื่อ instance ตามด้วยตัวดำเนินการ . การใช้ชื่อ property มีลักษณะแบบเดียวกับการเข้าถึง attribute แบบ public

เมื่อ property ที่มี method getter ก็ต้องมั property ที่เป็น method setter ด้วยเช่นกัน เป็นการใช้ เดคคอร์เรเตอร์
@property_name.setter (property_name คือชื่อ property เป็น method getter)
class Person:
@name.setter
def name(self, name):
self.\_\_name = name

    @height.setter
    def height(self, height):
        if height >= 50:
            self.__height = height
        else:
            print('Invalid height.')

    @weight.setter
    def weight(self, weight):
        if weight >= 3:
            self.__weight = weight
        else:
        print('Invalid weight.)

Property เป็น method setter ที่มีชื่อเดียวกับ property method getter เมื่อส่งค่าให้ attribute เก็บไว้เป็นการใช้ชื่อ instance ตามด้วยตัวดำเนินการ . และชื่อ property พร้อมกับค่าที่ส่งให้
person2.name = 'Chaiyanan Pagdee'
person2.height = 176
person2.weight = 74
การสร้างproperty ดังกล่าวอาจยุ่งยากหากให้ class มีทั้ง method getter และ property ด้วย จะใช้การประกาศสร้าง property โดยรับค่า argument เข้ามาเป็น method getter setter มีอยู่แล้ว
name = property( get_name, set_name )
height = property( get_height, set_height )
weight = property( get_weight, set_weight )
ได้ property name, height, weight ใช้แบบเดียวกับตัวอย่างที่ผ่านมา และภายนอก class ยังสามารถเข้าถึง attribute ได้ทั้งสองแบบ
person1.name = 'Worapong Tanasilp'
person1.set_height(179)
person1.weight=82

คอนสตรักเตอร์และดีสตรักเตอร์
python กำหนด method **init**() ทำหน้าเป็น Constructor ให้กับ class เพื่อประกาศ attribute ให้กับ object
และกำหนด method **del**() ทำหน้าเป็นดีสตรักเตอร์ (destructor) ให้ class คืนทรัพยากรที่ขอมาจากระบบเมื่อ object ถูกทำลาย

สมาชิก Class
python มี attribute และ method เป็นของ object ที่ประกาศสร้างขึ้นมาเรียกว่า instance attribute ซึ่งมีคำว่า self นำหน้า
และ instance method คำว่า self เป็น parameter ตัวแรก ยังมี attribute และ method ที่เป็นของ class สามารถเรียกใช้งานโดยไม่ต้องมี object
ประกาศสร้างขึ้นมาก่อนและ object ทั้งหมดเรียกมาใช้ร่วมกันได้เรียกว่า class attribute ส่วน method แบ่งเป็นสแตติกเมธอด (Static Method)
และ class method (class method)

class attribute
instacne attribute เก็บค่าให้แต่ละ object กำหนดขึ้นใน constructor มีตำว่า self นำหน้า มีหลายตัวตามจำนวน
object ส่วน class attribute กำหนดขึ้นเป็นของ class ไม่มีคำว่า self นำหน้า มีเพียงตัวเดียวให้แต่ละ object เรียก
ใช้งานร่วมกันได้ class attribute เป็นแบบเดียวกับตัวแปรทั่วไปกำหนดอยู่นอก method และ constructor มีคุณสทบัติ
เป็น public ภายนอก class มองเห็นเรียกใช้งานได้โดยตรง
class Circle:
PI = 3.14159
object_count = 0

    def __init__(self, radius):
        self.__radius = radius
        Circle.object_count += 1

    def get_area(self):
        return Circle.PI * self.__radius * self.__radius

    def __del__(self):
        Circle.object_count -= 1

สแตติก method
python มี method 2 แบบเรียกมาใช้งานโดยไม่ต้องประกาศสร้าง object ขึ้นมาก่อน แบบแรกคือ static method เป็นของ class ให้แต่ละ object เรียกใช้งานร่วมกันได้ การกำหนดเหมือนกับ general function ไม่มีคำว่า self เป็น parameter ตัวแรก แต่มี decorator @staticmethod
กำหนดไว้ก่อนหน้า method เพื่อให้ interpreter ได้ทราบ
class Circle:
@staticmethod
def area( radius ):
return Circle.PI _ redius _ radius

    @staticmethod
    def circumference( radius ):
        return 2 * Circle.PI * radius

Class method
class method เป็นของ class เช่นกันเรียกมาใช้งานโดยไม่ต้องประกาศสร้าง object ก่อน class method
ใช้งานแบบเดียวกับ static method แต่มีจุดมุ่งหมายแตกต่างกัน static method กำหนดให้เป็นการทำงานของ class โดยไม่
มี object มาเกี่ยวของ เช่นตัวอย่าง class Circle มี static method area() และ circumference() หาพื้นที่และเส้นรอบ
วงของวงกลมใดๆไม่ต้องเป็น object
ส่วน class method มีจุดประสงค์อย่างหนึ่งคือใช้เป็น Factory Method เป็น method ใช้ประกาศ
ส่วน object มีชนิดข้อมูลต่างกันหรือ attribute ต่างกันส่งคืนกลับมาให้ โดยมีตัวแปร instance รอรับนำไปใช้งาน การ
กำหนด class method มี decorator @classmethod กำหนดไว้ก่อนหน้าและมี parameter ตัวแรกคือ cls เป็นการส่ง
ผ่าน class ที่ใช้อยู่ขณะนั้นมาให้แต่ใช้ keyword class ไม่ได้จึงใช้ cls แทนนำมาประกาศสร้าง object
class Circle:
@classmethod
def from_area(cls, area):
radius = math.sqrt(area/Circle.PI)
return cls(radius)

    @classmethod
    def from_circumference(cls, circumference):
        radius = circumference / Circle.PI / 2
        return cls(radius)

classmethod from_area() และ from_curcumference() มี parameter ตัวแรกคือ cls รับค่าเป็น class Circle
เข้ามาอัตโนมัติโดยไม่ต้องส่งค่า argument มีพารามิเตอร์ถัดมาคือ area และ circumference รับค่า argument เป็นขนาดพื้นที่และความยาว
เส้นรอบวงใช้คำนวณหาค่ารัศมีและนำมาประกาศสร้าง object ส่งคืนกลับมาให้กับ instance ที่รอรับใช้งาน
circle1 = Circle.from_area(314.159)
circle2 = Circle.from_circumference(125.6636)

การสืบทอด
การเขียนโปรแกรม oop มีหลัการ encalsulation ยังมีหลัการ inheritance เป็นการนำกลับมาใช้ใหม่ Reusable โดยให้ object หนึ่ง
ขอคุณสมบัติของ object อื่นมาใช้ class ที่ถ่ายทอดคุณสมบัติให้เรียกว่า super class ส่วน class ที่ได้รับคุณสมบัติจากการถ่ายทอดลงมาเรียกว่า sub class และ super class ของ class อื่นที่ถ่ายทอดต่อลงมาเป็น sub class
ในลักษณะระดับชั้น super class มีคุณสมบัติทั่วไป Generalize เมื่อถ่ายทอดให้ sub class และเพิ่มเติมคุณสมบัติใหม่เกิดความ
แตกต่างเป็นคุณสมบัติเฉพาะ Specialize ซึ่งเป็นหลักการนำกลับมาใช้ใหม่ การสืบทอดใน python มีโครงสร้างดังนี้

class super_class:
attributes_super_class
methods_super_class
class sub_class( super_class ):
attributes_super_class # attributes get by derive from super_class
methods_super_class # methods get by derive from super_class
attributes_sub_class # attributes declared in sub_class
methods_sub_class # methods defined in sub_class

sub class สืบทอดจาก super class กำหนดในสัญลักษณ์ และ ต่อจากชื่อ sub class เป็นการถ่ายทอดคุณสมบัติ attributes_super_class และ
methods_super_class มาให้และเพิ่มคุณสมบัติใหม่ attributes_sub_class และ methods_sub_class
class Point:
def **init**(self, x, y):
self.**x = x
self.**y = y

    def set_point(self, x=0, y=0):
        pass

    def get_x(self):
        pass

    def get_y(self):
        pass

    def __str__(self):
        pass

class point กำหนด attributes **x, **y เป็น private มี method set_point(), get_x(), get_y(), **str**()
เป็น super class นำคุณสมบัติถ่ายทอดให้กับ class Line สืบทอดลงมาเป็น sub class ก็จะได้ attribute และ method มาใช้งาน

class Line( Point ):
def **init**(self, x, y, length):
Point.**init**(self, x, y)
self.\_\_length = length

    def set_line(self, x=0, y=0, length=0 ):
        Point.set_point(self, x, y)
        if length > 0:
            self.__length = length

    def __str__(self):
        return Point.__str__(self) + ', length:{}'.format( self.__length )

class line สืบทอดจาก class Point ใช้ constructor class Point กำหนด attributes **x, **y และเพิ่ม attributes **length ทำให้ class line
ได้ตำแหน่งสุดที่สืบทอดลงมาและมีความยาวเส้น เนื่องจาก attribute **x, **y เป็น private เข้าถึงข้อมูลต้องผ่าน constructor และ method ของ super class ที่ชื่อ superclass และกำหนดคำว่า self หมายถึง object ของ sub class เป็น parameter ตัวแรก
Point.**init**(self, x, y)
...
Point.set_point(self, x, y)
หรือใช้ function super() อ้างอิงไปยัง super class และไม่ต้องกำหนดคำว่า self
super().**init\_\_( x, y )
...
super().set_point( x, y )

เนื่องจาก attribute class Point เป็น private ทำให้ class Line ที่ Inheritance ไม่สะดวกเข้าถึงข้อมูล จึงเปลี่ยน attribute class Point เป็น Protected ทำให้ sub class เข้าถึงข้อมูล super class โดยตรงแบบ public และภายนอก class ยังเป็น private attribute point เป็น protect นำหน้าชื่อด้วยตัวอักษรขีดเส้นใต้หนึ่งขัด Single Underscore การกำหนด attribute class Point

class Point:
def **init**(self, x, y):
self.\_x = x
self.\_y = y

class Line inheritance ลงมาสามารถเข้าถึง attribute **x, **y ได้โดยตรง เช่น method set_line() ในการทำงาน
เข้าถึงได้โดยตรงไม่ต้องผ่าน method set_point()

class Linr( Point ):
def set_line(self, x=0, y=0, length=0 ):
if x > 0:
self.\_x = x
if y > 0:
self.\_y = y
if length > 0:
self.\_\_length = length

การเข้าถึงข้อมูลโดยตรงนำมาใช้กรณีต้องการจัดการกับ attribute เพียงบางตัว แต่ยังคงใช้การเข้าถึงข้อมูลผ่าน constructor และ method ของ super class ในแบบ private ซึ่งจะสะดวกกว่า

การสืบทอดหลายคลาส
การสืบทอดใน python ใน sub class มี super class ได้หลาย class เรียกว่าการสืบทอดหลายคลาส Multiple Inheritance
ทำให้ sub class มี attribute ได้จากหลาย class รวมกัน

class sub_class( super_class1, super_class2, super_class3, ...):
attributes_and_method_super_class1
attributes_and_method_super_class2
attributes_and_method_super_class3
...
attributes_and_method_super_class(n)

sub class inheritance จากหลาย super class แยกคั่นด้วย , รวมอยู่ในสัญลักษณ์ และ จึงได้
คุณสมบัติจาก super class ทั้งหมดถ่ายทอดมาให้ใช้งาน

class Cylinder ( Circle, Line ):
def **init**(self, radius, x, y, length ):
Circle.**init**(self, radius )
Line.**init**(self,x,y,length)

Class Cylinder มีคุณสมบัติเป็นรูปทรงกระบอก inheritance from class Circle and Line อยู่ใน module CircleClass
และ InheriteLine โดย constructor เรียกใช้ constructor ของ class Circle กำหนด attribute **radius
และ constructor ของ class Line กำหนด attribute **x, **y, **length ได้เป็นรูปทรงกระบอก

การสืบทอดหลาย Class มี super class จำนวนมากและ complex ทำให้เกิดปัญหาเรียกว่า Diamond Problem เมื่อ sub class
ได้คุณสมบัติจาก super class ที่เป็นตัวเดียวกันจะมีคุณสมบัติซ้ำกันมากกว่าหนึ่ง เช่น คลาส D
ได้รับคุณสมบัติจาก class A สองชุด aa ถ่ายทอดผ่าน class B และ C ซึ่งทั้งสองมี attribute a ทำให้ class D มี attribute aa สองตัว
เพื่อหลีกเลี่ยงปัญหาการสืบทอด multi class จึงเปลี่ยนให้ super class มาเป็นส่วนประกอบของ sub class โดยการผ่าน object ที่กำหนดเป็น
attribute sub class ทำให้ sub class มีคุณสมบัติ super class ได้มาโดยทางอ้อม การกำหนด มีได้สองแบบ คือ Composition และ Aggregation

Composition
เป็นการนำคุณสมบัติ super class ใช้เป็นส่วนประกอบโดยผ่าน object แบบ composition สร้างเป็น attribute ใน sub class
เมื่อ object sub class ถูกทำลายจะทำให้ object composition ถูกทำลายไปด้วย อย่างเช่น object window ซึ่ง มี object
Button และ TextBox ถูกทำลายไปด้วย

class Cylinder():
    def __init__(self, radius, x, y, length ):
        self.__circle = Circle(radius)
        self.__line = Line( x, y, length)

class Cylinder มี constructor กำหนด attribute __circle เป็น object สร้างจาก class Circle และ attribute __line 
เป็น object สร้างจาก class Line ทำหน้าที่เป็น composition อยู่ภายใน class Cylinder 
