# game 폴더에 sound폴더와 graphic 폴더를 만들고 각각에 __init__.py를 생성
# sound 폴더에는 echo.py라는 파일 생성
# graphic 폴더에는 render.py라는 파일 생성
import game.sound.echo
game.sound.echo.echo_test()

from game.sound import echo
echo.echo_test()

from game.sound.echo import echo_test
echo_test()

from game.sound import *
echo.echo_test()
echo2.echo2_test()

from game.graphic import render
render.render_test()