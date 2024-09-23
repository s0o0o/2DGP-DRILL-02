from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
while(x<800):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,90)
    
    x+=15 #게임 로직 부분.. 객체의 상호작용을 시뮬레이션
    delay(0.01)

close_canvas()

#게임루프는 시뮬레이션(로직)과 렌더링의 반복

#JPG는 투명화사진이 x... PNG는 가능
#jpg는 손실압축. png는 비손실압축
#jpg는 일부러 화질을 안좋게해서 압축시킴
#png는 원래 화질을 유지하면서 파일 사이즈는 좀 커도 화질은 유지 ㄱㄴ
#png를 써야.. 화질이 유지(퀄리티 위해서)! 배경은 jpg가능 
