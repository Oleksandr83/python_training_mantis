from model.project import Project
import pytest
import string
import random

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5 #+ string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata =[Project(project_name=random_string("name", 10), project_description=random_string("description", 25))]


@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_add_project(app, project):
    old_project_list = app.project.get_projacts_list()
    print(old_project_list)
    app.project.create_project(project)
    new_project_list = app.project.get_projacts_list()
    old_project_list.append(project)
    assert sorted(str(old_project_list)) == sorted(str(new_project_list))
