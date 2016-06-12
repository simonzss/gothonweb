from gothonweb import map
import web

urls = (
    '/game','GameEngine',
    '/','Index'
)

app = web.application(urls, globals())
web.config.debug = False

if web.config.get('_session') is None:
    store=web.session.DiskStore('sessions')
    session=web.session.Session(app,store,initializer={'room':None,'count':0})
    web.config._session=session
else:
    session=web.config._session

render = web.template.render('templates/',base="layout")


class Index(object):
    def GET(self):
        session.room=map.START
        #session.count=0
        web.seeother("/game")

class GameEngine(object):

    def GET(self):
        if session.room:
            if session.room.name=="The End Good":
                return render.show_good_room(room=session.room)
            elif session.room.name=="Laser Weapon Armory":
                return render.show_count_room(room=session.room,count=5-session.count)
            else:
                return render.show_room(room=session.room)
        else:
            return render.you_died()

    def POST(self):
        form=web.input(action=None)

        if session.room and form.action:
            if session.room.name=="Laser Weapon Armory" and session.count<4 and form.action!="123":
                session.room=session.room.go("repeat")
                session.count+=1
            else:
                session.room=session.room.go(form.action)
                session.count=0

        web.seeother("/game")

if __name__=="__main__":
    app.run()

