from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers, status
from .serializers import TodolistSerializer
from .models import Todolist

#   GET Data


@api_view(['GET'])
def all_todolist(request):
    # ดึงข้อมูลจาก model todolist คือ "select * from Todolist"
    alltodolist = Todolist.objects.all()
    # many=True หมายถึงจะมีค่ามากกว่า 1
    serializer = TodolistSerializer(alltodolist, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#   POST Data (save data to database)


@api_view(['POST'])
def post_todolist(request):
    if request.method == 'POST':
        serializer = TodolistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

#   Update(edit) data
@api_view(['PUT'])
def update_todolist(request, TID):
    # localhost:8000/api/update-todolist/TID => (id ใน json data)
    todo = Todolist.objects.get(id=TID)

    if request.method == 'PUT':
        data = {}
        serializer = TodolistSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['status'] = 'updated'
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

#   Delete data
@api_view(['DELETE'])
def delete_todolist(request, TID):
    todo = Todolist.objects.get(id=TID)

    if request.method == 'DELETE':
        delete = todo.delete()
        data = {}
        if delete:
            data['status'] = 'deleted'
            statuscode = status.HTTP_200_OK
        else:
            data['status'] = 'failed'
            statuscode = status.HTTP_400_BAD_REQUEST
        
        return Response(data=data, status=statuscode)

data = [
    {
        "title": " แล็ปท็อปคืออะไร?",
        "subtitle": "คอมพิวเตอร์ คือ อุปกรณ์ที่ใช้สำหรับการคำนวณและทำงานอื่นๆ?",
        "image_url": "https://raw.githubusercontent.com/MPR2014v8/BasicAPI/main/home-office-1867761_960_720.jpg",
        "detail": "คอมพิวเตอร์ (อังกฤษ: computer) หรือศัพท์บัญญัติราชบัณฑิตยสภาว่า คณิตกรณ์[2][3] เป็นเครื่องจักรแบบสั่งการได้ที่ออกแบบมาเพื่อดำเนินการกับลำดับตัวดำเนินการทางตรรกศาสตร์หรือคณิตศาสตร์ โดยอนุกรมนี้อาจเปลี่ยนแปลงได้เมื่อพร้อม ส่งผลให้คอมพิวเตอร์สามารถแก้ปัญหาได้มากมาย\n\nคอมพิวเตอร์ถูกประดิษฐ์ออกมาให้ประกอบไปด้วยความจำรูปแบบต่าง ๆ เพื่อเก็บข้อมูล อย่างน้อยหนึ่งส่วนที่มีหน้าที่ดำเนินการคำนวณเกี่ยวกับตัวดำเนินการทางตรรกศาสตร์ และตัวดำเนินการทางคณิตศาสตร์ และส่วนควบคุมที่ใช้เปลี่ยนแปลงลำดับของตัวดำเนินการโดยยึดสารสนเทศที่ถูกเก็บไว้เป็นหลัก อุปกรณ์เหล่านี้จะยอมให้นำเข้าข้อมูลจากแหล่งภายนอก และส่งผลจากการคำนวณตัวดำเนินการออกไป"
    },
    {
        "title": "Flutter คือ?",
        "subtitle": "Tools สำหรับออกแบบ UI ของ Google",
        "image_url": "https://raw.githubusercontent.com/MPR2014v8/BasicAPI/main/phone-292994_960_720.jpg",
        "detail": "Flutter คือ Cross-Platform Framework ที่ใช้ในการพัฒนา Native Mobile Application (Android/iOS) พัฒนาโดยบริษัท Google Inc. โดยใช้ภาษา Dart ในการพัฒนา ที่มีความคล้ายกับภาษา C# และ Javaอีกหนึ่งจุดเด่นของ Flutter คือ การปรับแต่ง UI (User Interface) ที่มีความยืนหยุ่น แยกการออกแบบเพื่อเน้นไปที่ประสบการณ์ของผู้ใช้งาน UX (User Experience) โดย UI จะใกล้เคียงกับ Native และตรงตาม Design Guideline ที่ถูกต้อง และมีความสามารถในการทำ Hot Reload\n\n ที่ทำให้การแก้ไขโค้ดสามารถแสดงผลได้ทันทีในระหว่างที่รันแอปพลิเคชัน และยังรวมไปถึงมี Widget ที่พร้อมให้เลือกใช้มากมาย ทำให้พัฒนาแอปพลิเคชันได้ไวเหมาะสำหรับองค์กรที่ต้องการแอปที่สวยงามและมีประสิทธิภาพในหลักสูตรมีการสอน State Management โดยใช้ BLoC (Business Logic Component) ที่นิยมในกลุ่มนักพัฒนา Flutter ในการจัดการ Local/Global State เพื่อรองรับระบบที่มีขนาดใหญ่และซับซ้อน ดูเป็นมืออาชีพ รวมถึงการเขียนโค้ดที่ทำงานร่วมกับ Native API โดยใช้ภาษาสมัยใหม่อย่าง Kotlin และ Swift เพื่อให้ผู้เข้าอบรมสามารถรับมือกับ Requirement ที่ต้องเชื่อมต่อกับ Native Android และ iOS"
    },
    {
        "title": "Python คือ?",
        "subtitle": "ภาษาเขียนโปรแกรมชนิดหนึ่ง สร้างขึ้นเมื่อ 1991",
        "image_url": "https://raw.githubusercontent.com/MPR2014v8/BasicAPI/main/coding-924920_1920.jpg",
        "detail": "ภาษาไพทอน (Python programming language) หรือที่มักเรียกกันว่าไพทอน เป็นภาษาระดับสูงซึ่งสร้างโดยคีโด ฟัน โรสซึม โดยเริ่มในปีพ.ศ. 2533 การออกแบบของภาษาไพทอนมุ่งเน้นให้ผู้โปรแกรมสามารถอ่านชุดคำสั่งได้โดยง่ายผ่านการใช้งานอักขระเว้นว่าง (whitespaces) จำนวนมาก นอกจากนั้นการออกแบบภาษาไพทอนและการประยุกต์ใช้แนวคิดการเขียนโปรแกรมเชิงวัตถุในตัวภาษายังช่วยให้นักเขียนโปรแกรมสามารถเขียนโปรแกรมที่เป็นระเบียบ อ่านง่าย มีขนาดเล็ก และง่ายต่อการบำรุง[3]/n/nไพทอนเป็นภาษาแบบไดนามิกพร้อมตัวเก็บขยะ ไพทอนรองรับกระบวนทัศน์การเขียนโปรแกรมหลายรูปแบบ ซึ่งรวมถึงแต่ไม่จำกัดเพียงการเขียนโปรแกรมตามลำดับขั้น การเขียนโปรแกรมเชิงวัตถุ หรือการเขียนโปรแกรมเชิงฟังก์ชัน นอกจากนี้ไพทอนเป็นภาษาที่มักถูกอธิบายว่าเป็นภาษาโปรแกรมแบบ มาพร้อมถ่าน (batteries included) กล่าวคือไพทอนมาพร้อมกับไลบรารีมาตรฐานจำนวนมาก เช่นโครงสร้างข้อมูลแบบซับซ้อน และไลบรารีสำหรับคณิตศาสตร์"
    }
]


def Home(request):
    return JsonResponse(data=data, safe=False, json_dumps_params={'ensure_ascii': False})
