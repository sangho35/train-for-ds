import matplotlib
from matplotlib import font_manager, rc
import platform

try : 
    if platform.system() == 'Windows':
    # 윈도우인 경우
        font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
        rc('font', family=font_name)
    else:    
    # Mac 인 경우
        rc('font', family='AppleGothic')
except : 
    pass
matplotlib.rcParams['axes.unicode_minus'] = False   


## pandas 출력 옵션 설정
pd.set_option('display.float_format', '{:.2f}'.format)

## 그래프 라벨 실수형 설정(Y좌표)
plt.ticklabel_format(axis='y', useOffset=False, style='plain')  # 방법1
plt.gca().set_yticklabels(['{:.0f}'.format(x) for x in plt.gca().get_yticks()]) #방법2 
