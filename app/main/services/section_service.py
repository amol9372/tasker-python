from app.main import transaction
from app.main.business_models.section import AppSection
from app.main.business_models.task import AppTask
from app.main.db_models.task.sections import Section
from app.main.db_models.task.tasks import Task
from app.main.db_models.task.user_labels import UserLabels


class SectionService():

    def __init__(self) -> None:
        pass

    # def get_all_sections(self, user_id):
    #     user_labels: list[UserLabels] = UserLabels.get_user_labels(user_id)
    #     user_label_default: UserLabels = list(
    #         filter(lambda user_label: user_label.default == True, user_labels))[0]

    #     db_sections: list[Section] = Section.get_sections(
    #         user_label_default.label_id)
    #     appSections = SectionBuilder.get_sections(
    #         db_sections)
    #     return appSections

    def get_all_sections(self, label_id):
        db_sections: list[Section] = Section.get_sections(label_id)
        appSections = SectionBuilder.get_sections(db_sections)
        return appSections

    @transaction()
    def create_section(self, data):
        section = Section(name=data['name'], label_id=data['label_id'])
        return Section.create_section(section)

    @transaction()
    def delete_section(self, id):
        Section.delete_section(id)


class SectionBuilder():

    def __init__(self) -> None:
        pass

    def get_sections(sections):
        return list(map(lambda section: AppSection(section.id, section.name, SectionBuilder.convertDbTasks(section.tasks)).__dict__, sections))

    def convertDbTasks(tasks):
        return list(map(lambda task: AppTask(task.id, task.name, description="", priority=task.priority, status=task.completed).__dict__, tasks))
