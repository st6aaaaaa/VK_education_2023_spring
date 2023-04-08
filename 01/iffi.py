class SomeModel:
    def predict(self, message: str) -> float:
        # реализация не важна
        pass


def predict_message_mood(message: str, model: SomeModel,
                         bad_thresholds: float = 0.3,
                         good_thresholds: float = 0.8) -> str:
    
    tmp = model.predict(message)
    if tmp < bad_thresholds:
        return 'неуд'
    if tmp > good_thresholds:
        return 'отл'
    return 'норм'
