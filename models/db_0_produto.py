# -*- coding: utf-8 -*-

db.define_table('produto',
                Field('descricao', label='Descrição'),
                Field('valor_unitario', 'double', default=0.0),
                format='%(descricao)s'
                )

db.define_table('servico',
                Field('descricao', label='Descrição'),
                Field('valor_unitario', 'double', default=0.0),
                format='%(descricao)s'
                )
