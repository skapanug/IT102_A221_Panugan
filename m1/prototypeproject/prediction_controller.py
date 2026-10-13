class PredictionController:

    def __init__(
        self,
        predictor
    ):

        self.predictor = predictor

    def generatePrediction(
        self,
        amounts
    ):

        return self.predictor.predict(
            amounts
        )