from app import app
from flask import render_template,flash, request, redirect, url_for
from .forms import CalculatorForm, ButtonForm
from app import db, models
import datetime

@app.route('/')
def index():
    greeting = "Hello World!!!"
    title = "Homepage"
    # return redirect(url_for('create_assessment'))
    return render_template('index.html',
                            title=title,
                            greeting=greeting)

@app.route('/create_assessment', methods=['GET','POST'])
def create_assessment():
    title = "Create Assessment"
    header = "Create Assessment"
    form = CalculatorForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            p = models.Assessments(title=form.title.data, module_code=form.module_code.data, deadline=form.deadline.data, description=form.description.data)
            db.session.add(p)
            db.session.commit()
            flash('Succesfully submitted data')
            return redirect(url_for('create_assessment'))

    return render_template('create_assessment.html',
                            title=title,
                            header=header,
                            form=form)

@app.route('/all_assessments')
def all_assessments():
    title = "All Assessment"
    header = "All Assessments"
    form = CalculatorForm()
    data = models.Assessments.query.all()
    return render_template('all_assessments.html',
                            title=title,
                            header=header,
                            form=form,
                            data=data)


@app.route('/completed_assessments', methods=['GET', 'POST'])
def completed_assessments():
    title = "Completed Assessments"
    header = "Completed Assessments"
    data = models.Assessments.query.filter_by(status='Completed').all()
    form = CalculatorForm()

    #check if request method is POST
    if request.method == 'POST':
        try:
            #get the button id & convert it to an integer
            id = request.form['button']
            id = int(id)

            #retrieve the id from the button & update assessment status
            p = models.Assessments.query.get(id)
            p.status = 'Uncompleted'
            db.session.commit()
            flash("Assessment Marked As 'Incomplete'")
            return redirect(url_for('completed_assessments'))

        except:
            flash("Unable to mark assessment as 'Incomplete'", "danger")
            return redirect(url_for('completed_assessments'))

    return render_template('completed_assessments.html',
                            title=title,
                            header=header,
                            form=form,
                            data=data)


@app.route('/uncompleted_assessments', methods=['GET', 'POST'])
def uncompleted_assessments():
    title = "Uncompleted Assessments"
    header = "Uncompleted Assessments"
    data = models.Assessments.query.filter_by(status='Uncompleted').all()
    form = CalculatorForm()

    #check if request methos is POST
    if request.method == 'POST':
        # when a specific button is clicked on, mark as completed & reload the page
        try:
            #get the button id & convert it to an integer
            id = request.form['button']
            id = int(id)

            #retrieve the id from the button & update assessment status
            p = models.Assessments.query.get(id)
            p.status = 'Completed'
            db.session.commit()
            flash("Assessment Marked As 'Complete'")
            #refreshs the page after adding to database
            return redirect(url_for('uncompleted_assessments'))

        except:
            flash("Unable to mark assessment as 'Complete'", "danger")
            return redirect(url_for('uncompleted_assessments'))
    return render_template('uncompleted_assessments.html',
                            title=title,
                            header=header,
                            form=form,
                            data=data)
