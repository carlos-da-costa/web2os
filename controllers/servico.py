# -*- coding: utf-8 -*-

@auth.requires_login()
def index():
    return dict(grid=SQLFORM.grid(db.servico))

def api():
    return db(db.servico.id == request.args(0)).select().as_json()
