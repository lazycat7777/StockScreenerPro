class AppRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'screener_daily_USA':
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'screener_daily_USA':
            return 'default'
        return None

    def get_queryset(self, model, **hints):
        if model._meta.app_label == 'screener_daily_USA':
            return super().get_queryset(model, **hints).using('default')
        return super().get_queryset(model, **hints)    