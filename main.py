from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FallOutTransition, FadeTransition

from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import FadeTransition
from kivy.clock import Clock
# import brower

Window.size = (330, 560)
user_accout = ['', '', '', '']
go_now = [-1, -1, -1, -1]
now = 1
total_number = 0

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        Clock.schedule_once(self.callNext, 3)


    def callNext(self,dt):
        self.manager.current = 'main_screen_name'
        print "Hi this is call Next Function of loading 1"
    pass

class Main_Screen(Screen):
    twitter = ObjectProperty(None)
    facebook = ObjectProperty(None)
    foursqure = ObjectProperty(None)
    instagram = ObjectProperty(None)
    now_account = ObjectProperty(None)
    total_account = ObjectProperty(None)
    warning = ObjectProperty(None)
    account_input = ObjectProperty(None)
    previous = ObjectProperty(None)
    go_next = ObjectProperty(None)
    text_username = ObjectProperty(None)

    def insert_data(self):
        total = 0
        if self.twitter.active:
            print('twitter')
            total += 1
            go_now[0] = 0
        if self.facebook.active:
            print('facebook')
            total += 1
            go_now[1] = 1
        if self.foursqure.active:
            print('foursqure')
            total += 1
            go_now[2] = 2
        if self.instagram.active:
            print('instagram')
            total += 1
            go_now[3] = 3
        total_number = total
        if total > 0:
            self.total_account.text = str(total)
            self.warning.opacity = 0
            self.now_account.text = str(now)
            self.account_input.opacity = 1
            self.go_next.disabled = False
            self.previous.disabled = False
        else:
            self.total_account.text = str(total)
            self.now_account.text = str(total)
            self.account_input.opacity = 0
            self.warning.opacity = 1
            self.go_next.disabled = True
            self.previous.disabled = True

    def goto_next(self, args):
        global now
        global total_number
        j = now
        for i in range(0, 4):
            if go_now[i] != -1:
                j -= 1
            if j == 0:
                break
        print "asdasd"
        # print args
        user_accout[go_now[i]] = args
        now += 1
        if now < total_number:
            self.text_username.text = ""
            self.now_account.text = str(now)
            self.go_next.disabled = False
        else:
            self.go_next.disabled = True
        print user_accout

    def go_previous(self):
        global now
        now -= 1
        j = now
        for i in range(0, 4):
            if go_now[i] != -1:
                j -= 1
            if j == 0:
                break
        print "asdasd"
        # print args
        self.text_username.text = user_accout[go_now[i]]
        self.now_account.text = str(now)
        if now <= total_number:
            self.go_next.disabled = False


class Analysis_Detail_Screen(Screen):
    pass


class Analysis_Result_Screen(Screen):
    # Detail_label = ObjectProperty(None)
    # def go_search(self):
    #     brower.get_content_from_url("https://news.google.com/news/?ned=en_sg&gl=SG&hl=en-SG", Detail_label.text)
    pass


class Screen_Management(ScreenManager):
    pass


presentation = Builder.load_file("screen3.kv")
# sm = ScreenManager(transition= FallOutTransition())
# sm.add_widget(LoginScreen(name='login_screen'))
# sm.add_widget(Main_Screen(name='main_screen_name'))
# sm.add_widget(Analysis_Detail_Screen(name='analysis_result_screen_id'))
# sm.add_widget(Analysis_Result_Screen(name='analysis_detail_screen'))




class Screen3App(App):

    def build(self):
        # print sm.screen_names
        # return sm
        return presentation


if __name__ == "__main__":
    Screen3App().run()