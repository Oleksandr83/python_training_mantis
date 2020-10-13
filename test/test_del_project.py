from model.project import Project
import random


def test_del_projekt(app):
    # взять из системы списко существующих проектов
    old_project_list = app.project.get_projacts_list()
    # выбор произвольного проекта из списка существующих проектов для удаления
    project =random.choice(old_project_list)
    print(project.project_name)
    app.project.del_project(project.project_name)
    new_project_list = app.project.get_projacts_list()
    old_project_list.remove(project)
    assert sorted(str(old_project_list)) == sorted(str(new_project_list))

