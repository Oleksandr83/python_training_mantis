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

    def open_manage_projects_page(self):
        pass
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def open_create_project_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_project_field_value("name", project.project_name)
        self.change_project_field_value("description", project.project_description)

    def change_project_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("My View").click()