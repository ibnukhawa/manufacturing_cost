{
  'name': 'Manufacturing Cost for innoGRAPH',
  'author': 'Ibnu Nur Khawarizmi',
  'version': '0.1',
  'depends': [
    'product','stock','mrp',
  ],
  'data': [
    'views/add_attrs_cost.xml',
    'views/add_cost.xml',
  ],
  'qweb': [
    # 'static/src/xml/nama_widget.xml',
  ],
  'sequence': 1,
  'auto_install': False,
  'installable': True,
  'application': True,
  'category': 'Manufacturing',
  'summary': 'Penambahan Cost dan Menjadikan Field Cost Menjadi Mandatory',
  'license': 'OPL-1',
  'website': 'https://www.innograph.com/',
  'description': '-'
}