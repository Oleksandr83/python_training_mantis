from model.project import Project
import random


def test_del_projekt(app):
    old_project_list = app.soap.load_projects_list("administrator", "root")
    if len(old_project_list) == 0:
        app.project.create_project(Project(project_name="Test_project", project_description="Test_project"))
        old_project_list = app.project.get_projacts_list()
        return old_project_list
    project =random.choice(old_project_list)
    print(project.project_name)
    app.project.del_project(project.project_name)
    new_project_list = app.soap.load_projects_list("administrator", "root")
    old_project_list.remove(project)
    assert sorted(str(old_project_list)) == sorted(str(new_project_list))

