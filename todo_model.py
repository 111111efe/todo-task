# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TodoTask(models.Model): 
	_name = 'todo.task' 

	_description = 'To-do Task'
	name = fields.Char('Description', required=True) 
	is_done = fields.Boolean('Done?') 
	active = fields.Boolean('Active?', default=True)

	#Logica de los botones

	#Cambiar el valor de actividad de una tarea en especifico
	@api.multi
	def do_toggle_done(self):
		for task in self:
			task.is_done = not task.is_done

		return True

	@api.multi
	def do_clear_done(self): 
		dones = self.search([('is_done', '=', True)])
		dones.write({'active': False}) #paso a falso todos los registos en true
		return True