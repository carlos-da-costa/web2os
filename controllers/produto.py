# -*- coding: utf-8 -*-

@auth.requires_login()
def index():
    return dict(grid=SQLFORM.grid(db.produto))

def api():
    return db(db.produto.id == request.args(0)).select().as_json()
