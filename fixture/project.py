from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app


    def create_project(self, project):
        wd = self.app.wd
        self.open_manage_projects_page()
        self.open_create_project_form()
        self.fill_project_form(project)
        # submit project creation
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.return_to_home_page()


    def del_project(self, project_name):
        wd = self.app.wd
        self.open_manage_projects_page()
        self.select_project_by_name(project_name)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.return_to_home_page()


    def open_manage_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()


    def open_create_project_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()


    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_project_field_value("name", project.project_name)
        #self.change_project_field_value("description", project.project_description)


    def change_project_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def select_project_by_name(self, project_name):
        wd = self.app.wd
        wd.find_element_by_link_text(project_name).click()


    def get_projacts_list(self):
        wd = self.app.wd
        self.open_manage_projects_page()
        projects_list = []
        table = wd.find_element_by_css_selector("table.width100:nth-child(6)")
        for row in table.find_elements_by_css_selector("tr.row-1,tr.row-2"):
            cells = row.find_elements_by_tag_name("td")
            name = cells[0].text
            description = cells[4].text
            projects_list.append(Project(project_name=name, project_description=description))
        return projects_list


    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("My View").click()