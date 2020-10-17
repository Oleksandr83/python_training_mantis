from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def load_projects_list(self, username, password):
        project_list = []
        client = Client("http://localhost/mantisbt/api/soap/mantisconnect.php?wsdl")
        for row in client.service.mc_projects_get_user_accessible(username, password):
            #print(row)
            name = row[1]
            #id = row0]
            project_list.append(Project(project_name=name))
        return list(project_list)


            #for row in wd.find_elements_by_xpath("//tr[contains(@name, 'entry')]"):
            #    cells = row.find_elements_by_tag_name("td")
            #    id = cells[0].find_element_by_tag_name("input").get_attribute(
             #       "value")  # id = row.find_element_by_name("selected[]").get_attribute("value")
            #    lastname = cells[1].text