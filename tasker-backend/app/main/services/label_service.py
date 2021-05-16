from app.main.business_models.shared_label import SharedLabel
from app.main.db_models.task.label_detail import LabelDetail
from app.main.db_models.task.user_labels import UserLabels
from app.main.business_models.label import Label
from app.main import transaction


class LabelService():

    def __init__(self) -> None:
        pass

    def get_labels(self, user_id) -> list[Label]:
        user_labels: list[UserLabels] = UserLabels.get_user_labels(user_id)
        label_dict: dict[int, list[UserLabels]] = {}
        # get label details
        for user_label in user_labels:
            # if label_dict.get(user_label.)
            label_list = label_dict.get(user_label.id)
            if label_list == None:
                label_list = []

            label_list.append(user_label)
            label_dict[user_label.label_id] = label_list

        label_data: list[Label] = []
        for label_id in label_dict.keys():
            label_detail: LabelDetail = LabelDetail.get_label(label_id)

            # convert UserLabels to SharedLabels
            shared_label = self.get_shared_labels(
                label_dict.get(label_id), user_id)
            label = Label(label_detail.id, label_detail.name,
                          label_detail.color, False, shared_label.__dict__)
            print(type(label_detail.sections))
            # label.id = label_detail.id
            label_data.append(label.__dict__)

        return label_data

    def get_shared_labels(self, user_labels: list[UserLabels], user_id):
        users = list(map(lambda user_label: {
                     "user_id": user_label.user_id, "email": user_label.user.email, "primary": user_label.primary_user}, user_labels))

        if len(users) == 1:
            return SharedLabel([], primary=users[0]['primary'])

        for user_label in user_labels:
            if(user_label.user_id == user_id):
                return SharedLabel(users, primary=user_label.primary_user)

        return SharedLabel(users)

    @transaction()
    def create_label(self, label_data, user_id) -> int:
        # create label detail
        # label_data = json.dumps(label_data)
        label_detail = LabelDetail(label_data["name"], label_data['color'])
        label_id = LabelDetail.create_label(label_detail)

        # create user labels
        user_label = UserLabels(label_id, user_id,
                                primary_user=True, default=label_data['default'])
        UserLabels.create_user_label(user_label)
        return label_id

    @transaction()
    def delete_label(self, id):
        user_labels: list[UserLabels] = UserLabels.get_user_labels_by_label_id(
            id)
        if len(user_labels) == 1:
            UserLabels.delele_user_label(user_labels[0])
            LabelDetail.delete(id)
        else:
            user_label_to_delete = list(
                filter(lambda user_label: user_label.label_id == id, user_labels))[0]
            UserLabels.delele_user_label(user_label_to_delete)

    def edit_label(self):
        pass
