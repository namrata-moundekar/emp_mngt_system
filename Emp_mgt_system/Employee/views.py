from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Department, Position
from django.db import connection
from django.db import IntegrityError
from django.core.files.storage import FileSystemStorage
# from django.contrib import messages


# Create your views here.

def dashboard_page(request):

    with connection.cursor() as cursor:
        cursor.execute('SELECT COUNT(*) FROM EMPLOYEE_INFO')
        count = cursor.fetchone()[0]

    print(count)
    #
    if request.method == "POST":

        q = request.POST.get("name")
        q = q.lower()

        posts = Employee.objects.raw(
            'SELECT 1 as id, code, first_name, last_name, salary, email, dob, gender, upload_file, status, position_id, dept_id, phone, hire_date  FROM EMPLOYEE_INFO WHERE first_name LIKE \'%' + q + '%\' OR phone LIKE \'%' + q + '%\' OR LOWER(email) LIKE \'%' + q + '%\'  ')


        context = {'count': count,'posts': posts}
        return render(request, 'Dashboard/Dashboard.html' ,context)
    else:
        posts = Employee.objects.raw(
            'SELECT 1 as id, code, first_name, last_name, salary, email, dob, gender, upload_file, status, position_id, dept_id, phone, hire_date  FROM EMPLOYEE_INFO  ')

        context = {'count': count,'posts': posts}
        return render(request, 'Dashboard/Dashboard.html', context)


def add_or_update_emp(request, emp_id=None):
    if emp_id is None:
        # Adding a new record
        if request.method == 'POST':
            code = request.POST['code']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            salary = request.POST['salary']
            email = request.POST['email']
            dob = request.POST['dob']
            gender = request.POST['gender']
            upload_file = request.FILES.get('upload_file')
            status = request.POST['status']
            position = request.POST['position']
            dept = request.POST['dept']
            phone = request.POST['phone']
            hire_date = request.POST['hire_date']


            fs = FileSystemStorage(location='media/images/')
            saved_file = fs.save(upload_file.name, upload_file)

            positions = Position.objects.all()
            departments = Department.objects.all()


            try:
                if upload_file and upload_file.name.lower().endswith('.pdf'):
                    with connection.cursor() as cursor:
                        query = f"INSERT INTO EMPLOYEE_INFO (code, first_name, last_name, salary, email, dob, gender, upload_file, status, position_id, dept_id, phone, hire_date) VALUES ('{code}', '{first_name}', '{last_name}', '{salary}','{email}', '{dob}', '{gender}', '{saved_file}', '{status}', '{position}', '{dept}', '{phone}', '{hire_date}')"

                        cursor.execute(query)

                    return redirect('/emp/')
                else:
                    error_message = 'Please upload pdf file only !.....'
                    return render(request, 'Dashboard/addshow_emp.html',
                                  {'error_message': error_message, "emp_data": Employee.objects.all(),
                                   'positions': positions, 'departments': departments})



            except (IntegrityError) as e:
                error_message = f"An error occurred: {e}"
                return render(request, 'Dashboard/addshow_emp.html', {'error_message': error_message, "emp_data": Employee.objects.all(), 'positions': positions, 'departments': departments})

        else:
            # Render your add form template
            # Fetch positions and departments for rendering in the form
            positions = Position.objects.all()
            departments = Department.objects.all()


            return render(request, 'Dashboard/addshow_emp.html',{ "emp_data" : Employee.objects.all(), 'positions': positions, 'departments': departments})
    else:
        # Updating an existing record
        emp = get_object_or_404(Employee, id=emp_id)

        if request.method == 'POST':
            # Handle form data and create a new record
            code = request.POST['code']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            salary = request.POST['salary']
            email = request.POST['email']
            dob = request.POST['dob']
            gender = request.POST['gender']
            upload_file = request.FILES.get('upload_file')
            status = request.POST['status']
            # position = request.POST.get('position')
            # dept = request.POST.get('dept')
            phone = request.POST['phone']
            hire_date = request.POST['hire_date']


            try:
                query = f"UPDATE EMPLOYEE_INFO SET code='{code}', first_name='{first_name}', last_name='{last_name}', salary='{salary}', email='{email}', dob='{dob}', gender='{gender}', upload_file='{upload_file}', status='{status}', phone='{phone}', hire_date='{hire_date}' WHERE id={emp_id}"
                with connection.cursor() as cursor:
                    cursor.execute(query)
                return redirect('/emp/')  # Redirect to your record list view

            except IntegrityError as e:
                #     print("IntegrityError: {e}")
                error_message = 'Duplicate code !.....'
                #     # Handle the unique constraint violation (e.g., show an error message)
                return render(request, 'Dashboard/updateemp.html',
                              {'error_message': error_message})

        # Render your update form template with the existing record data
        return render(request, 'Dashboard/updateemp.html', {'emp': emp })


def delete_emp(request, emp_id):
    query = f"DELETE FROM EMPLOYEE_INFO WHERE id={emp_id}"
    with connection.cursor() as cursor:
        cursor.execute(query)
    return redirect('/emp/')


def add_or_update_dept(request, dept_id=None):
    if dept_id is None:
        # Adding a new record
        if request.method == 'POST':
            name = request.POST['name']
            description = request.POST['description']
            # Handle form data and create a new record
            query = f"INSERT INTO DEPARTMENT_INFO (name, description) VALUES ('{name}', '{description}')"
            with connection.cursor() as cursor:
                cursor.execute(query)

            return redirect('/dept/')  # Redirect to your record list view
        else:
            # Render your add form template
            return render(request, 'Dashboard/addshow_project.html',{ "dept_data" : Department.objects.all(),})
    else:
        # Updating an existing record
        dept = get_object_or_404(Department, id=dept_id)

        if request.method == 'POST':
            # Handle form data and create a new record
            name = request.POST['name']
            description = request.POST['description']
            query = f"UPDATE DEPARTMENT_INFO SET name='{name}', description='{description}' WHERE id={dept_id}"
            with connection.cursor() as cursor:
                cursor.execute(query)

            return redirect('/dept/')  # Redirect to your record list view

        # Render your update form template with the existing record data
        return render(request, 'Dashboard/updateproject.html', {'dept': dept })


def delete_dept(request, dept_id):
    query = f"DELETE FROM DEPARTMENT_INFO WHERE id={dept_id}"
    with connection.cursor() as cursor:
        cursor.execute(query)
    return redirect('/dept/')


def add_or_update_role(request, role_id=None):
    if role_id is None:
        # Adding a new record
        if request.method == 'POST':
            # Handle form data and create a new record
            name = request.POST['name']
            description = request.POST['description']
            # Handle form data and create a new record
            query = f"INSERT INTO POSITION_INFO (name, description) VALUES ('{name}', '{description}')"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return redirect('/role/')  # Redirect to record list view
        else:
            # Render your add form template
            return render(request, 'Dashboard/addshow_role.html',{ "role_data" : Position.objects.all(),})
    else:
        # Updating an existing record
        role = get_object_or_404(Position, id=role_id)

        if request.method == 'POST':
            name = request.POST['name']
            description = request.POST['description']

            query = f"UPDATE POSITION_INFO SET name='{name}', description='{description}' WHERE id={role_id}"
            with connection.cursor() as cursor:
                cursor.execute(query)


            return redirect('/role/')  # Redirect to your record list view

        # Render your update form template with the existing record data
        return render(request, 'Dashboard/updaterole.html', {'role': role })


def delete_role(request, role_id):
    query = f"DELETE FROM POSITION_INFO WHERE id={role_id}"
    with connection.cursor() as cursor:
        cursor.execute(query)
    return redirect('/role/')




