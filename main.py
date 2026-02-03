from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.navigationrail import MDNavigationRail, MDNavigationRailItem
from kivymd.uix.button import MDIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.uix.videoplayer import VideoPlayer
import threading
import yt_dlp

class AdityaProApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        
        layout = MDBoxLayout(orientation='horizontal')
        
        # Sidebar
        rail = MDNavigationRail(width="80dp", md_bg_color=(0.1, 0.1, 0.1, 1))
        rail.add_widget(MDNavigationRailItem(text="Home", icon="home"))
        rail.add_widget(MDNavigationRailItem(text="Search", icon="magnify"))
        layout.add_widget(rail)
        
        # Main UI
        content = MDBoxLayout(orientation='vertical', padding="10dp", spacing="10dp")
        content.add_widget(MDLabel(text="ADITYA PRO PLAYER", halign="center", font_style="H5", size_hint_y=None, height="50dp"))
        
        self.player = VideoPlayer(source="", state='pause', options={'allow_stretch': True})
        content.add_widget(self.player)
        
        search_box = MDBoxLayout(size_hint_y=None, height="50dp", spacing="10dp")
        self.inp = MDTextField(hint_text="Search song name...", mode="round")
        search_box.add_widget(self.inp)
        search_box.add_widget(MDIconButton(icon="magnify", on_release=self.search))
        content.add_widget(search_box)
        
        layout.add_widget(content)
        return layout

    def search(self, *args):
        query = self.inp.text
        threading.Thread(target=self.get_video, args=(query,), daemon=True).start()

    def get_video(self, query):
        try:
            with yt_dlp.YoutubeDL({'format': 'best', 'nocheckcertificate': True}) as ydl:
                info = ydl.extract_info(f"ytsearch1:{query}", download=False)['entries'][0]
                self.player.source = info['url']
                self.player.state = 'play'
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    AdityaProApp().run()
