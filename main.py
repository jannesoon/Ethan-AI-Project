from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # 添加背景图片（改成完整的绝对路径）
        img = Image(source=r"C:\Users\27310\Desktop\Ethan 的文档\界面1.png")
        layout.add_widget(img)

        # 添加按钮（位置微调）
        btn = Button(
            text="点我一下！",
            size_hint=(0.4, 0.1),  # 调整按钮的大小
            font_name=r"C:\Windows\Fonts\msyh.ttc",  # 尝试用系统字体路径
            pos_hint={'center_x': 0.5, 'center_y': 0.05}  # 让按钮更靠下居中
        )
        btn.bind(on_press=self.show_popup)
        layout.add_widget(btn)

        return layout

    def show_popup(self, instance):
        # 定义弹窗内容
        content = Label(
            text="你点到我啦！",
            font_name=r"C:\Windows\Fonts\msyh.ttc",  # 尝试用系统字体路径
            font_size=20,
            color=(0, 0, 0, 1)
        )
        popup = Popup(
            title="提示",
            content=content,
            size_hint=(None, None),
            size=(300, 200)
        )
        popup.open()

# 运行
MyApp().run()