class DemoDBRouter():
    def db_for_read(self, model, **hints):
        # print(model, flush=True)
        if hasattr(model, 'database_name'):
            # print(model.database_name, flush=True)
            return model.database_name

        return None

    def db_for_write(self, model, **hints):
        return self.db_for_read(model, **hints)
