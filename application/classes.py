

class SessionUser:
    def __init__(self, django_user):
        self.user = django_user

    def full_name(self):
        return self.user.get_full_name()

    def id(self):
        return self.user.id


class Psychic:
    def __init__(self, user, rating):
        self.user = user
        self.rating = rating

    def recalculation_rating(self, is_success):
        if not is_success:
            self.rating = self.rating - self.rating/10


class UserHistory:
    def __init__(self, user, number, date_sending):
        self.user = user
        self.number = number
        self.date_sending = date_sending


class HistoryPsychic:

    def __init__(self, user_history, psychic, estimated_number, date_sending):
        self.user_history = user_history
        self.psychic = psychic
        self.estimated_number = estimated_number
        self.date_sending = date_sending