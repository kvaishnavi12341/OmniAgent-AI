class Metrics:
    requests = 0
    p1_count = 0

    @classmethod
    def track(cls, severity):
        cls.requests += 1
        if severity == "P1":
            cls.p1_count += 1