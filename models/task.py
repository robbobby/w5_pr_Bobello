class Task:

    def __init__(self, name, description, id=None, completed_amount=0, completed=False, company_id=None):
        self.name = name
        self.description = description
        self.id = id
        self.completed_amount = completed_amount
        self.completed = completed
        self.company_id = company_id
