from flask import Blueprint
alumnos= Blueprint('alumnos',__name__)
from flask import redirect, render_template, url_for
from flask import request
import forms 
from model import Alumnos,db


@alumnos.route("/agregar",methods=['GET','POST'])
def index():
    create_forms=forms.UseForm(request.form)
    if request.method=='POST':
        alumn= Alumnos(nombre=create_forms.nombre.data,
                       apellidos=create_forms.apellidos.data,
                       email=create_forms.email.data)
        db.session.add(alumn)
        db.session.commit()
        return redirect(url_for('alumnos.ABCompleto'))
    return render_template('index.html',form=create_forms)

@alumnos.route("/ABCompleto",methods=['GET','POST'])
def ABCompleto():
    create_forms=forms.UseForm(request.form)
    alumnosAll=Alumnos.query.all()
    return render_template('ABCompleto.html',form=create_forms,alumnos=alumnosAll)

@alumnos.route("/modificar",methods=['GET','POST'])
def modificar():
    create_forms=forms.UseForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        alumn1= db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_forms.id.data=alumn1.id
        create_forms.nombre.data= alumn1.nombre
        create_forms.apellidos.data= alumn1.apellidos
        create_forms.email.data= alumn1.email

    if request.method=='POST':
        id=create_forms.id.data
        alumn= db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alumn.id=create_forms.id.data
        alumn.nombre=create_forms.nombre.data
        alumn.apellidos=create_forms.apellidos.data
        alumn.email=create_forms.email.data
        db.session.add(alumn)
        db.session.commit()
        return redirect(url_for('alumnos.ABCompleto'))

    return render_template('modificar.html',form=create_forms)

@alumnos.route("/eliminar",methods=['GET','POST'])
def eliminar():
    create_forms=forms.UseForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        alumn1= db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_forms.id.data=alumn1.id
        create_forms.nombre.data= alumn1.nombre
        create_forms.apellidos.data= alumn1.apellidos
        create_forms.email.data= alumn1.email

    if request.method=='POST':
        id=create_forms.id.data
        alumn= db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alumn.id=create_forms.id.data
        alumn.nombre=create_forms.nombre.data
        alumn.apellidos=create_forms.apellidos.data
        alumn.email=create_forms.email.data
        db.session.delete(alumn)
        db.session.commit()
        return redirect(url_for('alumnos.ABCompleto'))

    return render_template('eliminar.html',form=create_forms)


