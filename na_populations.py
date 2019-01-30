import pygal

wm = pygal.Worldmap()
wm.titla = 'populations of countries in NA'
wm.add('north america', {'ca':34126000, 'us':309349000, 'mx':113423000})
wm.render_to_file('na_populations.svg')