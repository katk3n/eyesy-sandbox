import pygame

# 背景画像を入れる変数
# setup() と draw() の両方で使うのでグローバル変数として宣言
bg_image = None


# 描画前の準備用関数
# プログラムを動かすときに最初に1回だけ呼ばれる
def setup(screen, etc):
    global bg_image

    # 背景画像用のファイルを読み込む
    # etc.mode_root は main.py がある場所
    bg_image = pygame.image.load(etc.mode_root + "/Images/waterfall_quarter.png")


# 描画するための関数
# 毎フレームこの関数が呼ばれることで、パラパラ漫画の要領でアニメーションになる
def draw(screen, etc):
    global bg_image

    # knob5 で背景色を変更
    etc.color_picker_bg(etc.knob5)

    # setup() で読み込んだ背景画像 (bg_image) をスクリーンの高さ (etc.yres) にあわせて拡大
    bg = pygame.transform.rotozoom(bg_image, 0, etc.yres / bg_image.get_height())

    # 拡大した背景画像 (bg) を半透明にする (64)
    bg.fill((255, 255, 255, 64), None, pygame.BLEND_RGBA_MULT)

    # 背景画像 (bg) を画面の中央に描画する
    # 描画する座標は画像の左上の頂点の場所で指定する
    # 画面の中央に描画するには、左上の頂点を
    # ((スクリーンの幅 - 画像の幅) / 2, (スクリーンの高さ - 画像の高さ) / 2)
    # にすればいい
    screen.blit(bg, ((etc.xres - bg.get_width()) / 2, (etc.yres - bg.get_height()) / 2))
