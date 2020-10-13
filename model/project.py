class Project:

    def __init__(self, project_name=None, project_description=None):
        self.project_name = project_name
        self.project_description = project_description


    def __repr__(self):
        return "%s:%s" % (self.project_name, self.project_description)

    def __eq__(self, other):
        return self.project_name == other.project_name and self.project_description == other.project_description
        #return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name