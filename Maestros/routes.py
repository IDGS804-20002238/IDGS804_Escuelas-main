from flask import Blueprint
maestros= Blueprint('maestros',__name__)
from db import get_connection
from flask import redirect, render_template, url_for
from flask import request
import forms 
from model import db,Maestros


@maestros.route("/getMaestros")
def getMaestros():
    create_forms=forms.UseForm(request.form)
    maestros_list = []
    try:
        connection=get_connection()
        with connection.cursor() as cursor:
                cursor.execute('call get_maestros()')
                resultset=cursor.fetchall()
                for row in resultset:
                    maestro = {
                        'id': row[0],
                        'nombre': row[1],
                        'apellidos': row[2],
                        'email': row[3],
                        'create_date': row[4]                  
                        }
                    maestros_list.append(maestro)
        connection.close()
    except Exception as ex:
        print(ex)
        pass
    return render_template('ABCompletoMaestros.html',form=create_forms,maestros=maestros_list)

@maestros.route("/eliminarMaestro",methods=['GET','POST'])
def eliminarMaestro():
    create_forms=forms.UseForm(request.form)
    if request.method=='GET':
        try:
            id=request.args.get('id')
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call get_maestro(%s)',(id))
                resultset=cursor.fetchall()            
                create_forms.id.data=resultset[0][0]
                create_forms.nombre.data= resultset[0][1]
                create_forms.apellidos.data=resultset[0][2]
                create_forms.email.data= resultset[0][3]                          
            connection.close()
            print()
        except Exception as ex:
                print(ex)
                pass
    if request.method=='POST':
        try:
            id=create_forms.id.data
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call eliminar_maestro(%s)',(id))
                connection.commit()
            connection.close()


        except Exception as ex:
                print(ex)
                pass
        return redirect(url_for('maestros.getMaestros'))
  
    return render_template('eliminarMaestro.html',form=create_forms)

@maestros.route("/agregarMaestro",methods=['GET','POST'])
def agregarMaestro():
    create_forms=forms.UseForm(request.form)
    if request.method=='POST':
        try:
            nombre=create_forms.nombre.data,
            apellidos=create_forms.apellidos.data,
            email=create_forms.email.data
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call insertar_maestro(%s,%s,%s)',(nombre,apellidos,email))
                connection.commit()
            connection.close()
        except Exception as ex:
                print(ex)
                pass
        return redirect(url_for('maestros.getMaestros'))
    
    return render_template('agregarMaestro.html',form=create_forms)

@maestros.route("/modificarMaestro",methods=['GET','POST'])
def modificarMaestro():
    create_forms=forms.UseForm(request.form)
    if request.method=='GET':
        try:
            id=request.args.get('id')
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call get_maestro(%s)',(id))
                resultset=cursor.fetchall()            
                create_forms.id.data=resultset[0][0]
                create_forms.nombre.data= resultset[0][1]
                create_forms.apellidos.data=resultset[0][2]
                create_forms.email.data= resultset[0][3]                          
            connection.close()
        except Exception as ex:
                print(ex)
                pass
        
    if request.method=='POST':
        try:
            id=create_forms.id.data
            nombre=create_forms.nombre.data,
            apellidos=create_forms.apellidos.data,
            email=create_forms.email.data
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call editar_maestro(%s,%s,%s,%s)',(id,nombre,apellidos,email))
                connection.commit()
            connection.close()
        except Exception as ex:
                print(ex)
                pass
        return redirect(url_for('maestros.getMaestros'))
  
    return render_template('modificarMaestro.html',form=create_forms)
