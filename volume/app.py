import web
from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')

urls = (
    '/', 'controllers.index.Index',
    '/list', 'controllers.agenda.Agenda',
    '/insert', 'controllers.insert.Insert',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()