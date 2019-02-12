# from game.sound.echo import echo_test
from ..sound.echo import echo_test # 상위는 게임, 게임에 사운드, 에코 임포트

def render_test():
    print("render")
    echo_test()