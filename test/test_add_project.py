from model.project import Project

def test_add_project(app):
    #app.session.login("administrator", "root")
    project = Project(project_name="New projekt1", project_description="Some description")
    app.project.create_project(project)
