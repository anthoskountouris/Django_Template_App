# Django_Template_App

<h2> Start a project </h2>
python3 -m django startproject smartnotes .
<h2> Run the local server </h2>
python3 manage.py runserver
<h2> Create new app </h2>
python3 -m django startapp home
# add the new app in the settings.py of the main app (smartnotes)

<h2> Database </h2>
database -> python3 manage.py migrate </br>
create admin user -> python3 manage.py createsuperuser </br>
Creating migration -> python3 manage.py makemigrations </br>
then -> python3 manage.py migrate </br>
working on shell ->  </br>
    python3 manage.py shell </br>
    from notes.models import Notes </br>
    mynote = Notes.objects.get(pk='1') # Notes.object is the main way if accessing data from the notes in the database. </br>
                                       # The .get() method will search for one object whicj the pk =1 and returns it </br>
    mynote.title </br>
    mynote.text </br>
    Notes.objects.all() </br>

    # creating new node
    new_note = Notes.objects.create(title="A second note", text="This is a second note")
    Notes.objects.all()

    # Quering/filtering
    Notes.objects.filter(title__startswith="My")
    Notes.objects.filter(text__icontains="Django")
    Notes.objects.exclude(text__icontains="Django")
    Notes.objects.filter(text__icontains="Django").exclude(title__icontains="Django")
