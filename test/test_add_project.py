from model.project import Project

def test_add_project(app):
    old_project_list = app.project.get_projacts_list()
    print(old_project_list)
    #app.session.login("administrator", "root")
    project = Project(project_name="New 3", project_description="kjbk")
    app.project.create_project(project)
    new_project_list = app.project.get_projacts_list()
    old_project_list.append(project)
    assert sorted(str(old_project_list)) == sorted(str(new_project_list))
