class ReviewsRouter:
    route_app_labels = {'reviews', 'custom_cakes'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'reviews_db'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'reviews_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        db_set = {'default', 'reviews_db'}
        if obj1._meta.app_label in self.route_app_labels and obj2._meta.app_label in self.route_app_labels:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'reviews_db'
        return db == 'default'
