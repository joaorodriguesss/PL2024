
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'SLR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEASSIGN DIVIDE IDENTIFIER INPUT LPAREN MINUS NUMBER OUTPUT PLUS RPAREN TIMESstatement : INPUT expressionstatement : OUTPUT expressionstatement : IDENTIFIER ASSIGN expressionexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expressionexpression : LPAREN expression RPARENexpression : NUMBERexpression : IDENTIFIER'
    
_lr_action_items = {'INPUT':([0,],[2,]),'OUTPUT':([0,],[3,]),'IDENTIFIER':([0,2,3,6,10,11,12,13,14,],[4,8,8,8,8,8,8,8,8,]),'$end':([1,5,7,8,9,16,17,18,19,20,21,],[0,-1,-9,-10,-2,-3,-4,-5,-6,-7,-8,]),'LPAREN':([2,3,6,10,11,12,13,14,],[6,6,6,6,6,6,6,6,]),'NUMBER':([2,3,6,10,11,12,13,14,],[7,7,7,7,7,7,7,7,]),'ASSIGN':([4,],[10,]),'PLUS':([5,7,8,9,15,16,17,18,19,20,21,],[11,-9,-10,11,11,11,-4,-5,-6,-7,-8,]),'MINUS':([5,7,8,9,15,16,17,18,19,20,21,],[12,-9,-10,12,12,12,-4,-5,-6,-7,-8,]),'TIMES':([5,7,8,9,15,16,17,18,19,20,21,],[13,-9,-10,13,13,13,13,13,-6,-7,-8,]),'DIVIDE':([5,7,8,9,15,16,17,18,19,20,21,],[14,-9,-10,14,14,14,14,14,-6,-7,-8,]),'RPAREN':([7,8,15,17,18,19,20,21,],[-9,-10,21,-4,-5,-6,-7,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([2,3,6,10,11,12,13,14,],[5,9,15,16,17,18,19,20,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> INPUT expression','statement',2,'p_statement_input','script.py',63),
  ('statement -> OUTPUT expression','statement',2,'p_statement_output','script.py',67),
  ('statement -> IDENTIFIER ASSIGN expression','statement',3,'p_statement_assignment','script.py',71),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','script.py',75),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','script.py',76),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','script.py',77),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','script.py',78),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','script.py',82),
  ('expression -> NUMBER','expression',1,'p_expression_number','script.py',86),
  ('expression -> IDENTIFIER','expression',1,'p_expression_identifier','script.py',90),
]
