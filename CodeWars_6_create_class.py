
class Ball(object):
    def __init__(self,ball_type="regular"):
        self.ball_type = ball_type


ball = Ball()
ball1 = Ball("same")

print(ball1.ball_type)