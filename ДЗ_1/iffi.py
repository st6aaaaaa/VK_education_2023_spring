class SomeModel:
    def predict(self, message: str) -> float:
        # реализация не важна
        pass


def predict_message_mood(message: str, model: SomeModel,
                         bad_thresholds: float = 0.3,
                         good_thresholds: float = 0.8) -> str:

    if model.predict(message) < bad_thresholds:
        return 'неуд'
    if model.predict(message) > good_thresholds:
        return 'отл'
    return 'норм'
