# names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
nordic_countries = names[:5]
es, ru = names[5], names[6]
print(f"Nordic Countries: {nordic_countries}, Estonia: {es}, Russia: {ru}")

*nordic_countries1, es, ru = names
print(f"nordic countries: {nordic_countries1}, {es}, {ru}")
