#ignore
# seaborn 中文字體
if not os.path.exists("/usr/share/fonts/SimHei/simhei.ttf"):
  !mkdir /usr/share/fonts/SimHei
  !wget  http://d.xiazaiziti.com/en_fonts/fonts/s/SimHei.ttf
  !wget -O /usr/share/fonts/SimHei/simhei.ttf \
      "http://d.xiazaiziti.com/en_fonts/fonts/s/SimHei.ttf"
  !chmod 755 /usr/share/fonts/SimHei/*.ttf
  !sudo apt-get install ttf-mscorefonts-installer
  !sudo mkfontscale
  !sudo mkfontdir
  !fc-cache -fv
  !rm -rf ~/.cache/matplotlib
  clear_output()
import seaborn as sns
sns.set(font='SimHei')
plt.rcParams['font.sans-serif']=['SimHei']