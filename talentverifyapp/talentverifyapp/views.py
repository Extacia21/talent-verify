import csv
from rest_framework.views import APIView
from rest_framework.response import Response
from talentverifyapp.models import Employee
from talentverifyapp.serializers import EmployeeSerializer
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def post(request):
    file = request.FILES.get('file')
    if not file:
        return Response({'error': 'No file provided'}, status=400)

    if not file.name.endswith('.csv'):
        return Response({'error': 'Invalid file format'}, status=400)

    decoded_file = file.read().decode('utf-8').splitlines()
    csv_reader = csv.DictReader(decoded_file)

    new_employees = []
    for row in csv_reader:
        serializer = EmployeeSerializer(data=row)
        if serializer.is_valid():
            new_employees.append(serializer.validated_data)
        else:
            error_message = "Invalid data in CSV row: {serializer.errors}"
            return Response({'error': error_message}, status=400)

    employees = Employee.objects.bulk_create([Employee(**data) for data in new_employees])
    employee_serializer = EmployeeSerializer(employees, many=True)
    return Response({'employees': employee_serializer.data}, status=201)


class BulkEmployeeUploadView(APIView):
    pass
