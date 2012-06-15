# -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the Affero GNU General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    Affero GNU General Public License for more details.
#
#    You should have received a copy of the Affero GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

from osv import fields, osv

class product_product_insulation(osv.osv):
    _inherit = 'product.product'
    _columns = {
        'insulation' : fields.boolean('Insulation product', change_default=True),
        'rvalue' : fields.integer('R-Value',help="Thermal resistance"),
        'sprayfoam' : fields.boolean('SPF', help="SPray Foam product uses square foot and R-value to compute the board foot. Choose board foot as the UoS"),
    }

product_product_insulation()